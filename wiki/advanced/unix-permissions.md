---
title: Unix Permissions
---

*Linux, Unix, macOS only*

When SABnzbd runs on a Unix-like server, the download result must often be made available for other users.
Normally files that are created by a user account are private. This is also true for the files created by SABnzbd.
This is OK for the internal administration files, but not always for the downloaded files.

In [Config->Folders](/wiki/configuration/{{ site.wiki_version }}/folders) you can specify which access rights SABnzbd should give the end result, using the same octal notation as the [chmod](http://en.wikipedia.org/wiki/Chmod) command.

You specify the pattern for *folders*. For files, SABnzbd always removes the execute bits (and the setuid/setgid bits), because downloaded files should not be executable. So a folder pattern of `0755` results in `0644` on the files inside it.

Typical values:

| Value | Access |
|-------|--------|
| `0777` | full access for everyone |
| `0700` | only private access |
| `0755` | private read/write access, others only read access |
| `0750` | private read/write access, group read access, others no access |

## When the setting is empty

If you leave the permissions setting empty, SABnzbd does not force a specific mode. Folders and files keep the permissions the operating system gives them, which are determined by the process `umask`. Even then, SABnzbd still removes the execute bits from the completed files.

<span class="label label-warning">NOTE</span> On startup SABnzbd warns if the `umask` is more restrictive than `077`, because that can deny SABnzbd access to the files and folders it creates.
