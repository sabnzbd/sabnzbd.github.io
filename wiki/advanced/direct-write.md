---
title: Direct Write
---

Direct Write is SABnzbd's optimized way of assembling files. SABnzbd keeps articles in the Article Cache until it can write larger chunks to the final file at the correct positions, preferring contiguous writes when possible but not requiring them.

This can significantly reduce disk I/O and CPU overhead on fast local storage, but it has a few important requirements and limitations.

In classic append mode, SABnzbd only writes data sequentially from the start of the file onwards. With Direct Write, the assembler can use the known offsets of yEnc articles so that bytes land at their intended positions earlier. This means that, even when some articles are missing or delayed, the layout of the file on disk more closely matches the original posting, which can sometimes give repair a better chance at recovery.

SABnzbd does not normally stream articles straight from the network into random positions in the destination file. The Article Cache remains the primary staging area, and Direct Write mainly controls how (and when) cached data is written out.

# When to use Direct Write

Use Direct Write when:

- Your Internet connection and Usenet servers are fast enough that disk activity becomes a bottleneck (see [High speed Downloading](/wiki/advanced/highspeed-downloading)).
- Your `Temporary Download Folder` and `Completed Download Folder` are on a fast local disk (SSD, NVMe, or fast HDD).
- You have configured a reasonable [Article Cache Limit](/wiki/configuration/{{ site.wiki_version }}/general#toc2) so that SABnzbd can buffer articles in memory.

Avoid enabling Direct Write when:

- The download or complete folders point to network shares (SMB/NFS) or slow USB drives.
- You are very limited in RAM and cannot afford to dedicate memory to the article cache.

# How it works

Usenet posts files as many small "articles". For each file SABnzbd needs to:

1. Download and decode all articles.
2. Assemble them into the final file in the correct order.

Without Direct Write (append mode):

- Decoded articles are held in the Article Cache until there is enough contiguous data to append.
- Writes are always performed in order from the beginning of the file, so SABnzbd cannot skip ahead to "fill holes"; it can only grow the file as contiguous data becomes available.

With Direct Write enabled and supported by the filesystem:

- SABnzbd creates the destination file up front as a **sparse file** with the expected total size.
- Articles are still decoded into the Article Cache first; once there is enough contiguous data ready, SABnzbd writes it out to the destination file.
- As long as the cache has room, writes are usually contiguous, which improves write speeds and helps avoid heavily fragmented files.
- When the cache is under pressure SABnzbd can force non-contiguous writes into the sparse file to free space, but this is the exception rather than the normal path.
- When append mode runs out of memory it may write to temporary-files, with Direct Write this extra I/O is skipped, improving throughput on capable disks.

If for any reason Direct Write cannot be used for a specific file or article, SABnzbd automatically falls back to the normal append/write logic.

# Configuration

Direct Write relies on two main settings:

1. **Article Cache Limit**

   - Location: [Config-&gt;General](/wiki/configuration/{{ site.wiki_version }}/general#toc2), option <strong>Article Cache Limit</strong>.
   - Must be set to a non-zero value for Direct Write to be effective.
   - SABnzbd enables Direct Write only when there is enough cache to hold a meaningful amount of data.

   Recommended values:

   - For typical desktop systems: start with <code>500M</code>–<code>1000M</code>.
   - For very fast lines and SSD/NVMe storage: consider higher values if you have free RAM.
   - As a rule of thumb, try to size the cache so that it can hold at least one of your "typical" files in memory.

2. **Direct Write switch**
   - Location: [Config-&gt;Special](/wiki/configuration/{{ site.wiki_version }}/special#toc0), option <code>direct_write</code>.
   - Enable this to allow SABnzbd to use Direct Write when the Article Cache Limit and filesystem support allow it.

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

The Article Cache and Direct Write are tightly coupled:

- The Article Cache holds decoded articles in memory until there is enough data ready to write efficiently.
- SABnzbd uses internal thresholds (based on the configured cache limit and time since last write) to decide when to trigger Direct Write versus simple append writes.
- By default SABnzbd prefers sequential writes from the cache, only performing non-contiguous writes when cache pressure forces it.
- If the Article Cache Limit is disabled (<code>0</code>), Direct Write may never be activated and SABnzbd will behave like the traditional append-based assembler.

In other words, Direct Write in SABnzbd is a cache-driven optimization layer on top of the normal assembler, not a mode that bypasses the cache entirely.

<span class="label label-info">TIP</span> For high-speed setups, first tune the Article Cache Limit (see [High speed Downloading](/wiki/advanced/highspeed-downloading)), then enable Direct Write and monitor CPU, disk and RAM usage in the Status window.

# Troubleshooting

If you enable Direct Write and do not observe any change in disk activity or performance:

1. Confirm that **Article Cache Limit** is non-zero and large enough.
2. Verify that the Temporary and Completed folders are on local storage, not a network share.
3. Check the SABnzbd logs (in <strong>Debug</strong> level) for messages about sparse file creation failures or Direct Write being disabled.
4. If problems persist, you can safely disable <code>direct_write</code> again; SABnzbd will continue to work using the standard assembly method.
