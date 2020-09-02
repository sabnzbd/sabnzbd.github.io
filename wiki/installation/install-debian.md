---
title: SABnzbd installation on Debian
---


There are a few ways to install SABnzbd on Debian.

## From the standard Debian contrib repository

First make sure you have the Debian repository `contrib` activated. Then

```
sudo apt-get install sabnzbdplus
```

This is an easy way, but note that this version of SABnzbd can be old and **outdated**. Nevertheless, this way is always a good **first** step because it is easy, and it takes care of dependencies if running SABnzbd from source/github.

Run SABnzbd like this:
```
sabnzbdplus
```


## From the PPA for Ubuntu

Starting with version 3.0.0, direct use of the PPA on Debian is no longer an option. If you have such as setup, remove the PPA from your sources.list and go with creating a backport instead. The source packages from the PPA are an excellent basis for those, and that remains the case for 3.0.0.


## From source

You can run SABnzbd releases from source. Get the SABnzbd package from [the download page](https://sabnzbd.org/downloads) and unpack it in some writable directory (for example your home directory).

```
tar xvzf SABnzbd-2.3.2RC1-src.tar.gz
```

Tip: an easy way to solve dependencies, is to first install `sabnzbdplus` from the Debian contrib repository. See above.

Run SABnzbd like this, from the directory where you installed SABnzbd:
```
./SABnzbd.py
```



## From github

This is like running from source but you can update easily:

```
git clone https://github.com/sabnzbd/sabnzbd.git
cd sabnzbd
git checkout master
```
To update, go into the `sabnzbd` git directory, and type:
```
git pull
```
Run SABnzbd like this, from the directory where you installed SABnzbd:
```
./SABnzbd.py
```
