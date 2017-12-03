---
title: SABnzbd installation on Debian
---


There are a few ways to install SABnzbd on Debian.

## From the standard Debian contrib repository

First make sure you have the Debian repository 'contrib' activated. Then

```
sudo apt-get install sabnzbdplus
```

This is an easy way, but note that this version of SABnzbd can be old and **outdated**. Nevertheless, this way is always a good **first** step because it is easy, and it takes care of dependencies if running SABnzbd from source/github.

Run SABnzbd like this:
```
sabnzbdplus
```


## From the PPA for Ubuntu

The PPA for SABnzbd for Ubuntu seems to work for Debian too. At least: without warranties, and you need to read and follow the instruction by the author of the Ubuntu PPA (jcfp): see [this forum thread](https://forums.sabnzbd.org/viewtopic.php?f=16&t=9844).

The advantage of this method is that you get SABnzbd updates automatically when updating your Debian system.

Run SABnzbd like this:
```
sabnzbdplus
```


## From source

You can run SABnzbd releases from source: get SABnzbd (official release, or a pre-release) from [the SABnzb download page](https://sabnzbd.org/downloads) and unpack it in some writable directory (for example your home directory).

Unpack from the command line:
```
tar xvzf SABnzbd-2.3.2RC1-src.tar.gz
```

Tip: an easy way to solve dependencies, is to first install sabnzbdplus from the Debian contrib repository. See above.

Run SABnzbd like this, from the directory where you installed SABnzbd:
```
./SABnzbd.py
```



## From github

This is like running from source, but with not-yet-released code (so be aware).

```
git clone https://github.com/sabnzbd/sabnzbd.git
```
To update, go into the sabnzbd git directory, and type:
```
git pull
```
Run SABnzbd like this, from the directory where you installed SABnzbd:
```
./SABnzbd.py
```




