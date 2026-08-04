---
title: Job options
---

For each download job you can set post-processing options. While the download is still in the queue, you can change them on-the-fly.

| Option | Description |
|--------|-------------|
| `Download` | No post-processing at all. Just download all the files (including all PAR2) and move them to the final folder. The user has to do all post-processing manually. |
| `+Repair` | Download files and do a PAR2 verification. If the verification fails, download more PAR2 files and attempt to repair the files. |
| `+Unpack` | Download all files, do a PAR2 verification and unpack the files. The final folder will also include the RAR and ZIP files. |
| `+Delete` | Download all files, do a PAR2 verification, unpack the files to the final folder and delete the source files. |
