---
title: Direct Write
---

Direct Write is SABnzbd's optimized way of assembling files. When an Article Cache is configured, SABnzbd keeps articles in the cache until it can write larger chunks to the final file at the correct positions, preferring contiguous writes when possible but not requiring them. Direct Write can also operate without an Article Cache, writing decoded articles directly to their final positions on disk.

This can significantly reduce disk I/O and CPU overhead on fast local storage, but it has a few important requirements and limitations.

In classic append mode, SABnzbd only writes data sequentially from the start of the file onwards. With Direct Write, the assembler can use the known offsets of yEnc articles so that bytes land at their intended positions earlier. This means that, even when some articles are missing or delayed, the layout of the file on disk more closely matches the original posting, which can sometimes give repair a better chance at recovery.

# When to use Direct Write

Use Direct Write when:

- Your Internet connection and Usenet servers are fast enough that disk activity becomes a bottleneck (see [High speed Downloading](/wiki/advanced/highspeed-downloading)).
- Your `Temporary Download Folder` and `Completed Download Folder` are on a fast local disk (SSD, NVMe, or fast HDD).

Configuring an [Article Cache Limit](/wiki/configuration/{{ site.wiki_version }}/general#toc2) alongside Direct Write is recommended because it allows SABnzbd to buffer articles in memory and perform larger, more contiguous writes, reducing overall disk activity. Running Direct Write without a cache is only recommended when using an SSD or NVMe, since the many small random writes will not significantly impact performance on flash storage.

Avoid enabling Direct Write when:

- The download or complete folders point to network shares (SMB/NFS) or slow USB drives.
- You are using a spinning hard drive (HDD) without an Article Cache, as the random write pattern will hurt performance.

# How it works

Usenet posts files as many small "articles". For each file SABnzbd needs to:

1. Download and decode all articles.
2. Assemble them into the final file in the correct order.

Without Direct Write (append mode):

- Decoded articles are held in the Article Cache until there is enough contiguous data to append.
- Writes are always performed in order from the beginning of the file, so SABnzbd cannot skip ahead to "fill holes"; it can only grow the file as contiguous data becomes available.

With Direct Write enabled and supported by the filesystem:

- SABnzbd creates the destination file up front as a **sparse file** with the expected total size.
- If an Article Cache is configured, articles are decoded into the cache first; once there is enough contiguous data ready, SABnzbd writes it out to the destination file in larger, more efficient chunks.
- As long as the cache has room, writes are usually contiguous, which improves write speeds and helps avoid heavily fragmented files.
- When the cache is under pressure SABnzbd can force non-contiguous writes into the sparse file to free space, but this is the exception rather than the normal path.
- If no Article Cache is configured, decoded articles are written directly to their correct positions in the sparse file as they arrive. This results in many small random writes, which performs well on SSDs but can be slow on spinning disks.
- When append mode runs out of memory it may write to temporary-files, with Direct Write this extra I/O is skipped, improving throughput on capable disks.

If for any reason Direct Write cannot be used for a specific file or article, SABnzbd automatically falls back to the normal append/write logic.

# Configuration

Direct Write relies on the following settings:

1. **Direct Write switch**

   - Location: [Config-&gt;Special](/wiki/configuration/{{ site.wiki_version }}/special#toc0), option <code>direct_write</code>.
   - Enable this to allow SABnzbd to use Direct Write when the filesystem supports it.

2. **Article Cache Limit** (recommended)

   - Location: [Config-&gt;General](/wiki/configuration/{{ site.wiki_version }}/general#toc2), option <strong>Article Cache Limit</strong>.
   - While Direct Write can operate without a cache, configuring one is recommended as it reduces disk activity by allowing SABnzbd to batch articles into larger writes.
   - Running without a cache is only recommended on SSD/NVMe storage.

   Recommended values:

   - For typical desktop systems: start with <code>500M</code>–<code>1000M</code>.
   - For very fast lines and SSD/NVMe storage: consider higher values if you have free RAM.
   - As a rule of thumb, try to size the cache so that it can hold at least one of your "typical" files in memory.

# Requirements and limitations

## Filesystem support (sparse files)

Direct Write depends on the ability to create **sparse files** on the destination filesystem:

- SABnzbd asks the operating system to allocate a sparse file of the final size and then writes articles into it.
- Most modern filesystems (such as NTFS on Windows and ext4/xfs/btrfs on Linux) support sparse files.
- Some filesystems do not support sparse files correctly (for example certain legacy or network filesystems).

If creating a sparse file fails, SABnzbd will:

- Log a debug message that the sparse call failed.
- Automatically disable <code>direct_write</code> in the configuration.
- Fall back to the normal append-based write mode for subsequent downloads.

In practice this means:

- Place the Temporary and Completed folders on a filesystem with good sparse-file support for best results.
- If you see that Direct Write silently "turns off" after enabling it, check whether the target filesystem supports sparse files.

## Interaction with Article Cache

When an Article Cache is configured, Direct Write and the cache work together:

- The Article Cache holds decoded articles in memory until there is enough data ready to write efficiently.
- SABnzbd uses internal thresholds (based on the configured cache limit and time since last write) to decide when to flush data to disk.
- By default SABnzbd prefers sequential writes from the cache, only performing non-contiguous writes when cache pressure forces it.

When no Article Cache is configured (set to <code>0</code>), Direct Write operates independently by writing each decoded article directly to its position in the sparse file. This avoids the need for temporary files but produces many small random writes. This mode is only recommended on SSD/NVMe storage where random write performance is not a concern.

<span class="label label-info">TIP</span> For high-speed setups, first tune the Article Cache Limit (see [High speed Downloading](/wiki/advanced/highspeed-downloading)), then enable Direct Write and monitor CPU, disk and RAM usage in the Status window.

# Troubleshooting

If you enable Direct Write and do not observe any change in disk activity or performance:

1. Verify that the Temporary and Completed folders are on local storage, not a network share.
2. Check the SABnzbd logs (in <strong>Debug</strong> level) for messages about sparse file creation failures or Direct Write being disabled.
3. If using an HDD, make sure the **Article Cache Limit** is configured to a reasonable value to avoid excessive random writes.
4. If problems persist, you can safely disable <code>direct_write</code> again; SABnzbd will continue to work using the standard assembly method.
