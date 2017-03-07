---
title: SABYenc
redirect_from: "/sabyenc"
---

# Introduction to SAByenc

In SABnzbd 2.0.0 we introduce a new module called `sabyenc` to increase the download speed on CPU-limited devices.

The Windows- and MacOS-packages of SABnzbd automatically contain that module.

On other platforms (like Linux and FreeBSD) you have to make sure the module is installed. The information below is for packagers and source code users on those platforms.

# Installation on Linux 

### Installation in general

With Linux on x86 and x86-64, the module can be installed via Python's packaging manager "pip" by running

```
pip install sabyenc
```
or more generic:
```
pip install sabyenc --upgrade
```

On other platforms (ARM, MIPS, etc), you need to first install the python-development module (python-dev or python-devel), and then run the above pip command.


### Installation on Ubuntu via PPA

For Ubuntu there is a PPA with python-sabyenc, by the same creator (jcfp) as the SABnzbd PPA. Install it like this:
```
sudo add-apt-repository ppa:jcfp/sab-addons
sudo apt-get update
sudo apt-get install python-sabyenc
```
This will work on both X86, X86-64 and ARM architectures.

### Installation on Ubuntu (without PPA)

Short method, only works on X86 and X86-64
```
sudo apt-get install python-pip
sudo -H pip install sabyenc --upgrade
```

Long method:
```
sudo apt-get install python-dev python-pip
sudo -H pip install sabyenc --upgrade
```

### Installation on Fedora / RedHat

Short method, only works on X86 and X86-64

All as root:
```
pip install --upgrade pip
pip install sabyenc --upgrade
```

Long method:
```
yum install -y python-devel gcc redhat-rpm-config
pip install --upgrade pip
pip install sabyenc --upgrade
```

### Installation on OpenSuSE
All as root

Short, works on X86 and X86-64
```
zypper install -y python-pip
pip install --upgrade pip
pip install sabyenc --upgrade
```
Long, with your own compiling:

```
zypper install -y python-pip python-devel gcc
pip install --upgrade pip
pip install sabyenc --upgrade
```


# Installation on FreeBSD

<!-- Info from github @gregf -->

```
su - <password>

pkg install py27-pip-9.0.1
pip install --upgrade sabyenc
```

# Checking and Logging

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

# Notes

<span class="label label-warning">NOTE</span> The regular `_yenc` module will stay supported and download speed will stay the same as in SABnzbd 1.x.

# Issues

If you experience any issues, please let us know on our [Forums](https://forums.sabnzbd.org/) or [Github](https://github.com/sabnzbd/sabnzbd/issues)!
