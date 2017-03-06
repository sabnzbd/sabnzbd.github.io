---
title: SABYenc
redirect_from: "/sabyenc"
---

# Introduction to SAByenc

In SABnzbd 2.0.0 we introduce a new module called `sabyenc` to increase the download speed on CPU-limited devices.

The Windows- and MacOS-packages of SABnzbd automatically contain that module.

On other platforms (like Linux) you have to make sure the module is installed. The information below is for packagers and source code users on those platforms.

## Installation on Ubuntu via PPA

For Ubuntu there is a PPA with python-sabyenc, by the same creator (jcfp) as the SABnzbd PPA. Install it like this:
```
sudo add-apt-repository ppa:jcfp/sab-addons
sudo apt-get update
sudo apt-get install python-sabyenc
```
## Installation on Ubuntu (without PPA)

On Ubuntu/Debian the full installation is:
```
sudo apt-get install python-dev python-pip
sudo -H pip install sabyenc --upgrade
```

## Installation on Fedora / RedHat

All as root:
```
yum install -y python python-devel gcc redhat-rpm-config
pip install --upgrade pip
pip install sabyenc --upgrade
```

## Installation on OpenSuSE
All as root

Short (with precompiled sabyenc):
```
zypper install -y python python-pip
pip install --upgrade pip
pip install sabyenc --upgrade
```
Long, with your own compiling:

```
zypper install -y python python-pip python-devel gcc
pip install --upgrade pip
pip install sabyenc --upgrade
```

## Installation on Linux in general

Currently the module can only be installed via Python's packaging manager (pip) by running:

```
pip install sabyenc
```
We created pre-compiled packages for x86 and x64 platforms, if you use another platform you might need to install additional extra packages, `pip` will throw an error in those cases.

## Installation on FreeBSD

<!-- Info from github @gregf -->


```
su - <password>

pkg install python
pkg install python27-2.7.13_1
pkg install py27-pip-9.0.1
ln -s /usr/local/bin/python /usr/bin/python
pip install --upgrade sabyenc
```

## Check if sabyenc is correctly installed

To check if sabyenc is correctly installed, run this python oneliner:
```
python -c "import sabyenc ; print sabyenc.__version__ "
```
It should print the version of the installed sabyenc module, without any errors.


## SABnzbd's Checking & Logging

SABnzbd 2.0.0 and higher will check if SAByenc is installed. 
If SAByenc is installed, and the version is correct, sabnzbd.log will print:

```SABYenc module (v2.7.0)... found!```


Not having the `sabyenc` module installed will result in an error 

```SABYenc module... NOT found! Expecting v2.7.0```
 
on start-up to make users aware of the change. You can still download, but not with the improved speed.

## Notes

<span class="label label-warning">NOTE</span> The regular `_yenc` module will stay supported and download speed will stay the same as in SABnzbd 1.x.

## Issues

If you experience any issues, please let us know on our [Forums](https://forums.sabnzbd.org/) or [Github](https://github.com/sabnzbd/sabnzbd/issues)!
