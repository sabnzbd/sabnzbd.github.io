---
title: SABnzbd installation on Debian
---


There are two ways to install SABnzbd on Debian.

## Debian contrib repository

First make sure you have the Debian repository `contrib` activated. Then

```
sudo apt-get install sabnzbdplus
```

This is an easy way, but note that this version of SABnzbd can be old and **outdated**. 

Nevertheless, this way is always a good **first** step because it is easy, and it takes care of dependencies if running SABnzbd from source/github.

Run SABnzbd like this:
```
sabnzbdplus
```

## Alternatives

You can use any of the other Linux based installation methods liken [Docker, Snap or Flatpak](/wiki/installation/install-unix).

Or, you can run SABnzbd [from sources](/wiki/installation/install-off-modules).