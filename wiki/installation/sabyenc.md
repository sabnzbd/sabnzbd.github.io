---
title: SABYenc
redirect_from:
    - /sabyenc
    - /wiki/extra/sabyenc.html
---

# Introduction to SAByenc

In SABnzbd 2.0.0 we introduced a new module called `sabyenc` to increase the download speed on CPU-limited devices, which was further improved in SABnzbd 2.3.0.

The Windows- and macOS-packages of SABnzbd automatically contain that module. On other platforms (like Linux and FreeBSD) you have to make sure the module is installed. The information below is for packagers and source code users on those platforms.

<hr/>

**Jump to: [Ubuntu (via PPA)](#installation-on-ubuntu-via-ppa), [Ubuntu](#installation-on-ubuntu-without-ppa), [Fedora / RedHat](#installation-on-fedora--redhat), [OpenSuSE](#installation-on-opensuse) or [FreeBSD](#installation-on-freebsd).**

<hr/>

# Installation on Linux

### Installation in general



With Linux on x86 and x86-64, the latest version of the module can be installed via Python's packaging manager `pip` by running

```
pip install sabyenc --upgrade
```

On other platforms (ARM, MIPS, etc), you need to first install the python-development module (`python-dev` or `python-devel`), and then run the above `pip` command.

If you need to install a specific version to match your version of SABnzbd, you can specify this in the command:

```
pip install sabyenc==3.3.1
```

<div class="alert alert-warning">
    These instructions assume that <code>python</code> and <code>pip</code> refer to the Python 2.7 installation on your system.<br>On some systems Python 3 is the default <code>python</code> and you should instead use the <code>python2</code> and <code>pip2</code> commands.
</div>

<hr/>

### Installation on Ubuntu via PPA

For Ubuntu there is a PPA with `python-sabyenc`, by the same creator (JCFP) as the SABnzbd PPA. This will work on X86, X86-64, ARM (32bit) and ARM64 architectures.
Install it like this:
```
sudo add-apt-repository ppa:jcfp/sab-addons
sudo apt-get update
sudo apt-get install python-sabyenc
```


### Installation on Ubuntu (without PPA)

Short method, only works on X86 and X86-64
```
sudo apt-get install python-pip
sudo -H pip install sabyenc --upgrade
```

Long, with your own compiling:
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

Long, with your own compiling:

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


### Installation on FreeBSD and NAS4Free

<!-- Info from sabnzbd-forum amaroney-->
Short: installation of pre-made sabyenc package
```
pkg install py27-sabyenc
```
<!-- Info from github @gregf -->


Longer, with self compiling, thus needs cc:
```
su - <password>

pkg install py27-pip-9.0.1
pip install --upgrade sabyenc
```
<hr/>

## Multiple installations of python 

If you have multiple installations of python on your machine (python/python2 versus python3, or different versions of python 2.7), you have to make sure SAByenc is installed into the correct python enviroment. And 'correct' means the python installation used by SABnzbd (see SAB's logfile). The command is then:

```
/path/to/correct/python /path/to/pip install sabyenc
```




## Check if sabyenc is correctly installed

To check if sabyenc is correctly installed, run this Python oneliner:
```
python -c "import sabyenc ; print sabyenc.__version__ "
```
It should print the version of the installed `sabyenc` module, without any errors.


## SABnzbd's Checking & Logging

SABnzbd 2.0.0 and higher will check if SAByenc is installed.
If SAByenc is installed, and the version is correct, SABnzbd will print in the log:

```
SABYenc module (v2.7.0)... found!
```

If you have no `sabyenc` module installed, or an incorrect version (too low or too high (!)), you will get a warning:

```
SABYenc module... NOT found! Expecting v2.7.0
```

on start-up to make users aware of the change. You can still download, but not with the improved speed.

## Notes

<span class="label label-warning">NOTE</span> The regular `_yenc` module will stay supported and download speed will stay the same as in SABnzbd 1.x.

## Issues

If you experience any issues, please let us know on our [Forums](https://forums.sabnzbd.org/) or [Github](https://github.com/sabnzbd/sabnzbd/issues)!
