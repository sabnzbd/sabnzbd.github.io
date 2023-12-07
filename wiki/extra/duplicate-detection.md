---
title: Duplicate detection
redirect_from:
    - /wiki/duplicate-detection
---

# Introduction

If you use RSS feeds or other kinds of automation, you might want to prevent the same file being downloaded twice.
In order to prevent that, SABnzbd has 2 kinds of automation built-in:

* [Identical download detection](#identical-download-detection)
* [Smart duplicate detection](#smart-duplicate-detection)

Both types of detection will follow these steps when a new job is added to the Queue:
1. Check if a similar job (see details) is already present in the Queue or the History.
2. If a similar job was already downloaded successfully and is present in the history, perform the configured action right away.
3. If a similar job is present in the Queue, the new job will be paused and marked `ALTERNATIVE` to the original job.
   * When the original job succeeds, the alternatives will be handled as configured.
   * If the original job fails, the first alternative will automatically start downloading.

## Identical download detection

This type of detection will check the History and the Queue for an exact match of the NZB name or NZB content. 
It will also compare the NZB name to the files in your [.nzb Backup Folder](/wiki/configuration/{{site.wiki_version}}/folders), if you have one configured. 

Use this option if you only want to prevent identical jobs.

## Smart duplicate detection

If you want to prevent multiple versions of the same movie or show to be downloaded, SABnzbd can analyse the name of the job using the GuessIt module.

Specifically, we support detecting duplicates for Movies, Series and Daily shows.

For each type, here are some examples that would be detected as **duplicate**:

### Movies

1. `The.New.Movie.2023.XviD.AC3`
2. `The.new.movie.4k.hdr.2023`

### Series

1. `Show.Name.S11E23.1080p.AC3`
2. `Show.Name.s11e23.The.One.That.Was.Funny.480p.x264`

### Daily shows

1. `Funny.Daily.Standup.2023.11.09`
2. `Funny.daily.standup.2023-11-09`

----

## Notes

* With `Allow proper releases` [Switch](/wiki/configuration/{{site.wiki_version}}/switches) enabled, Smart duplicate detection is bypassed _once_ if `PROPER`, `REAL` or `REPACK` is found. 
If a second _proper_ job is added, it will be seen as a duplicate of the first _proper_ job.
* You can prevent checking against the `.nzb Backup Folder` by disabling the [Special](/wiki/configuration/{{site.wiki_version}}/special) setting `backup_for_duplicates`.
* If a [Pre-queue script](/wiki/configuration/{{site.wiki_version}}/scripts/pre-queue-scripts) changes the name of a job, duplicate detection will be triggered again.
* Notifications about duplicate jobs can be enabled or disabled by the [Special](/wiki/configuration/{{site.wiki_version}}/special) setting `warn_dupl_jobs`.