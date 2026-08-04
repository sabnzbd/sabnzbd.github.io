---
title: Unix Permissions
---

*Linux, Unix, macOS only*

When SABnzbd runs on a Unix-like server, the download result must often be made available for other users.
Normally files that are created by a user account are private. This is also true for the files created by SABnzbd.
This is OK for the internal administration files, but not always for the downloaded files.

In [Config->Folders](/wiki/configuration/{{ site.wiki_version }}/folders) you can specify which access rights SABnzbd should give the end result.
This parameter is passed to the [chmod](http://en.wikipedia.org/wiki/Chmod) command. It uses the octal notation supported by `chmod`.
You need to specify the settings for *folders*, so with the X bits set, SABnzbd will automatically remove any X bits for all files.

Typical values:

| Value | Access |
|-------|--------|
| `0777` | full access for everyone |
| `0700` | only private access |
| `0755` | private read/write access, others only read access |
| `0750` | private read/write access, group read access, others no access |
