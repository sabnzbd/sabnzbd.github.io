---
title: SABCTools 3
redirect_from:
    - /sabctools
---

# Introduction to SABCTools

In SABnzbd 4.0.0 we introduced a new module called `sabctools` to optimise (essential) CPU intensive tasks.

The Windows- and macOS-packages of SABnzbd automatically contain that module. On other platforms (like Linux and FreeBSD) you have to make sure the module is installed. The information below is for packagers and source code users on those platforms.

# Installation with Python's packaging manager `pip` 

<div class="alert alert-warning">
    These instructions assume that <code>python</code> and <code>pip</code> refer to the Python 3 installation on your system.<br>On some older systems Python 2 is the default <code>python</code> and you should instead use the <code>python3</code> and <code>pip3</code> commands.
</div>

<hr/>

Inside the source directory of SABnzbd, run this command

```
pip install -r requirements.txt
```

It will take care of installing the right version of `sabctools`. This will work for x86 and ARM.

You might need to first install the python-development module (`python3-dev` or `python3-devel`), and then run the above `pip` command.

If you need to install a specific version to match your version of SABnzbd, you can specify this in the command:

```
pip install sabctools==7.0.1
```

<hr/>


# Installation on Linux

**Jump to: [Ubuntu (via PPA)](#installation-on-ubuntu-via-ppa), [Ubuntu](#installation-on-ubuntu-without-ppa), [Fedora / RedHat](#installation-on-fedora--redhat), [OpenSuSE](#installation-on-opensuse) or [FreeBSD](#installation-on-freebsd).**

### Installation on Ubuntu via PPA

For Ubuntu there is a PPA with `sabctools`, by the same creator (JCFP) as the SABnzbd PPA. This will work on X86, X86-64, ARM (32bit) and ARM64 architectures.
Install it like this:
```
sudo add-apt-repository ppa:jcfp/sab-addons
sudo apt-get update
sudo apt-get install sabctools
```

### Installation on Ubuntu (without PPA)

Short method, only works on X86 and X86-64
```
sudo apt-get install python3-pip
sudo -H pip install sabctools --upgrade
```

Long, with your own compiling:
```
sudo apt-get install python3-dev python3-pip
sudo -H pip install sabctools --upgrade
```

### Installation on Fedora / RedHat

Short method, only works on X86 and X86-64

All as root:
```
pip install --upgrade pip
pip install sabctools --upgrade
```

Long, with your own compiling:

```
yum install -y python-devel gcc redhat-rpm-config
pip install --upgrade pip
pip install sabctools --upgrade
```

### Installation on OpenSuSE
All as root

Short, works on X86 and X86-64
```
zypper install -y python-pip
pip install --upgrade pip
pip install sabctools --upgrade
```

Long, with your own compiling:

```
zypper install -y python-pip python-devel gcc
pip install --upgrade pip
pip install sabctools --upgrade
```

<hr/>

## Multiple installations of python

If you have multiple installations of Python on your machine (<code>python</code>/<code>python2</code>/<code>python3</code> or different versions of Python 3), you have to make sure SABCTools is installed into the correct Python environment. And 'correct' means the Python installation used by SABnzbd. The command is then:

```
/path/to/correct/python -m pip install sabctools
```

## Check if SABCTools is correctly installed

To check if SABCTools is correctly installed, run this Python oneliner:
```
python -c "import sabctools; print(sabctools.__version__, sabctools.__file__);"
```
It should print the version of the installed `sabctools` module, without any errors.


## SABnzbd's Checking & Logging

SABnzbd will check if SABCTools is installed.
If SABCTools is installed, and the version is correct, SABnzbd will print in the log:

```
SABCTools module (v7.0.1)... found!
```

If your version of `sabctools` does not match the version required by SABnzbd, you get:
```
SABCTools disabled: no correct version found! (Found v6.0.0, expecting v7.0.1)
```

## Issues

If you experience any issues, please let us know on our [Forums](https://forums.sabnzbd.org/) or [Github](https://github.com/sabnzbd/sabnzbd/issues)!
