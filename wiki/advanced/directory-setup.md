---
title: Folder Setup
---

SABnzbd uses a number of folders for different purposes, some are just for internal administration.
Given that some folders can become very large, you may want to relocate them. The following tables explain the purpose of each folder, its default location and its keyword in the INI file.
All folders can also be changed through the Web-GUI.

On Windows, the expression `%userprofile%` is your personal folder in `C:\Users\`, which can be directly entered in Run (`WindowsKey+R`).
For Posix (Linux) `~` means your home folder.

<span class="label label-warning">NOTE</span> The paths of the `log_dir` and `admin_dir` will be relative to the location of the `sabnzbd.ini` file unless a fixed path is set.
The `download_dir`, `complete_dir` and `dirscan_dir` are relative to the current user's home directory.

<span class="label label-warning">NOTE</span> You can set fixed paths such as `D:\Downloads`, or `/Volumes/nameofdrive/Downloads`.
However, the path must be accessible to SABnzbd **when it is launched**, otherwise it will be reset to the default path.

----

### Configuration file `sabnzbd.ini`

| Operating System | Path |
|------------------|------|
| Windows | `%userprofile%\AppData\Local\sabnzbd\sabnzbd.ini` |
| Posix | `~/.sabnzbd/sabnzbd.ini` |
| macOS | `~/Library/Application Support/SABnzbd/sabnzbd.ini` |

----

### Temporary Download Folder `download_dir`

Here SABnzbd collects the data for each download and error correction (par2) is done. When complete, the data is moved to the `complete_dir`. There should be enough space to contain the largest complete job + 10% for error correction data.

| Operating System | Path |
|------------------|------|
| Windows | `%userprofile%\Downloads\incomplete` |
| Posix | `~/Downloads/incomplete` |
| macOS | `~/Downloads/incomplete` |

----

### Complete Download Folder `complete_dir`

Here all completed download jobs are stored. Each job is placed in a separate folder, named after the NZB file that started it. You want to put this on a volume with plenty of room.

| Operating System | Path |
|------------------|------|
| Windows | `%userprofile%\Downloads\complete` |
| Posix | `~/Downloads/complete` |
| macOS | `~/Downloads/complete` |

----

### Administrative directory `admin_dir`

Used for the internal administration of the job-queue and history.

| Operating System | Path |
|------------------|------|
| Windows | `%userprofile%\AppData\Local\sabnzbd\admin` |
| Posix | `~/.sabnzbd/admin` |
| macOS | `~/Library/Application Support/SABnzbd/admin` |

----

### Log directory `log_dir`

Here SABnzbd's logging is stored. Although only needed for troubleshooting, you must have this folder. Growth of this folder is normally limited to 5 MB.

| Operating System | Path |
|------------------|------|
| Windows | `%userprofile%\AppData\Local\sabnzbd\logs` |
| Posix | `~/.sabnzbd/logs` |
| macOS | `~/Library/Application Support/SABnzbd/logs` |
