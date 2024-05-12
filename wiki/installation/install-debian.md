---
title: SABnzbd installation on Debian
---


There are two ways to install SABnzbd on Debian.

## From the official Debian repository

Make sure you have the `contrib` and `non-free` repositories activated, then run:

```
sudo apt install sabnzbdplus
```

While this is the easiest install method, the version of SABnzbd can be old and **outdated**. Nevertheless, this way is always a good **first** step because it is easy, and it takes care of dependencies and system integration (desktop menu, autocomplete, system service, etc.).

Several options for installing newer releases on Debian via apt are listed in [this](https://forums.sabnzbd.org/viewtopic.php?p=60238) forum post.

To start the program, execute:
```
sabnzbdplus
```

## Alternatives

You can use any of the other Linux based installation methods such as [Docker, Snap or Flatpak](/wiki/installation/install-unix), or run SABnzbd [from sources](/wiki/installation/install-off-modules) entirely.
