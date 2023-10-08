---
title: Installing par2cmdline-turbo
redirect_from: /wiki/installation/multicore-par2
---

`par2cmdline-turbo` is a drop-in replacement for the original `par2cmdline` and it's forks (`mt` and `tbb`). 
It greatly improves verification and repair performance by using optimizations on x86 and ARM platforms.

## Installation on Ubuntu via PPA

For Ubuntu there is a PPA by the same creator (JCFP) as the SABnzbd PPA that has `par2cmdline-turbo`.

Run these commands to install the PPA and `par2cmdline-turbo`:

```
sudo add-apt-repository ppa:jcfp/sab-addons
sudo apt-get update
sudo apt-get install par2-turbo
```

-------------------

## Installation of pre-built binaries

On https://github.com/animetosho/par2cmdline-turbo/releases you can find pre-built binaries for different Linux (plus MacOS and Windows) versions. Download the correct version, unpack, and install.

Example of unpacking and putting into `/usr/local/bin/` on Linux x86_64:

```
xz -dv par2cmdline-turbo-v1.1.0-linux-amd64.xz
sudo mv /usr/local/bin/par2 /usr/local/bin/par2.old
sudo cp par2cmdline-turbo-v1.1.0-linux-amd64 /usr/local/bin/par2
```

-------------------


## Installation on other distributions

Tools required: `git`, `automake` and `make` (install via your distribution's package manager)

```
git clone https://github.com/animetosho/par2cmdline-turbo.git
cd par2cmdline-turbo
aclocal
automake --add-missing
autoconf
./configure
make
make install
```
<span class="label label-warning">NOTE</span> You might need to run the last command as `sudo` because it will install the `par2` command in the `bin` directory.

<span class="label label-warning">NOTE</span> Safest to uninstall your existing `par2` first!

After this, you can delete the `par2cmdline-turbo` folder.
