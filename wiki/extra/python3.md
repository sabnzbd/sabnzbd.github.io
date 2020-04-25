---
title: Python 3 - SABnzbd 3.0.0
redirect_from:
    - /python3
    - /sabnzbd3
---

## Background

SABnzbd has long relied on using Python 2.7, which will no longer be supported in [2020](https://pythonclock.org/). Therefore, we have been working on the switch to Python 3.
Although it sounds like an easy update, the way Python 3 deals with data input and output is quite different from Python 2.
Additionally, we also had to put a lot of effort in unit and functional testing, something that was never before part of the project.

The good news is that after the transition is complete, we are future proof and can use the latest versions of some Python packages that we rely on.

The not so good news is that for a regular user, not much changes. We are not expecting any real increases in performance or adding any new features as of now.
After the switch we can once again look at ways to increase performance by utilizing new features of Python 3.

## How to get SABnzbd 3.x.x for Python 3 to work prebuilt

SABnzbd 3.x.x for Python 3 is prebuilt available for the following platforms:

- Ubuntu Linux 18.04: via jcfp's private PPA. See https://forums.sabnzbd.org/viewtopic.php?f=16&t=24447
- Linuxserver SABnzbd docker image under the tag `unstable`: see https://hub.docker.com/r/linuxserver/sabnzbd/
- Windows: to be announced

There is not yet a prebuilt image for MacOS

## How to get SABnzbd 3.x.x for Python 3 to work from source

If you know how to run SABnzbd "from source" (so `git clone https://github.com/sabnzbd/sabnzbd.git`), you can run SABnzbd 3 as described below.

We support Python 3.5 and above.

### General Installation

You will need python3 and python3's pip module installed (the Python 3 version is sometimes linked to `pip3`). 

Check your python3 and python3's pip with this one command:
```
python3 -m pip
```
which should not give an error.
More specifically, on Linux/Macos/Unix/BSD: python3 must be in /usr/bin/python3, so test like this:
```
/usr/bin/python3  -m pip
```


Installation:
```
git clone https://github.com/sabnzbd/sabnzbd.git
cd sabnzbd/
python3 -m pip install -r requirements.txt -U
tools/make_mo.py
./SABnzbd.py
```

### MacOS

Install python3 and the module pip, for example via homebrew.
Make sure python3 is in /usr/bin/python3, or that is a link to the python3 binary in some other location.
Then follow the General Installation instructions

## Linux

#### Ubuntu specific instruction

On Ubuntu (and probably Debian), the Howto is:

From the `sabnzbd` directory of the github source:
```
sudo apt install python3-pip
python3 -m pip install -r requirements.txt -U
tools/make_mo.py
```

#### Ubuntu docker instruction
Start the Ubuntu docker:
```
sudo docker run -it ubuntu:latest /bin/bash
```
in the Ubuntu docker:
```
apt-get update
apt-get install git par2 unrar python3-setuptools python3-pip
apt-get install libffi-dev libssl-dev

git clone https://github.com/sabnzbd/sabnzbd.git 
cd sabnzbd/

pip3 install -r requirements.txt -U
tools/make_mo.py 
./SABnzbd.py -b0

```

#### fresh Fedora (docker) instruction
```
sudo docker run -it fedora:latest /bin/bash
```
In the docker:
```
dnf install git-core python3-pip
git clone https://github.com/sabnzbd/sabnzbd.git
cd sabnzbd/
python3 -m pip install -r requirements.txt -U
./SABnzbd.py -b0
```
PS: to add unrar and par2:
```
dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm 
dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
dnf install unrar
dnf install par2cmdline
```
#### Centos 7
```
yum -y install git python3-pip
python3 -m pip install --upgrade pip
git clone https://github.com/sabnzbd/sabnzbd.git
cd sabnzbd/
python3 -m pip install -r requirements.txt -U
./SABnzbd.py -b0
```


#### fresh OpenSuSE (docker) instruction

OpenSuSE Tumbleweed

```
sudo docker run -it opensuse/tumbleweed /bin/bash
```
or OpenSuSE Leap:
```
sudo docker run -p 8080:8080 -it opensuse/leap:15.1 /bin/bash
```
and then
```
zypper install -y git python3-pip
git clone https://github.com/sabnzbd/sabnzbd.git
cd sabnzbd/
pip3 install -r requirements.txt
./SABnzbd.py -b0
```




### Run

After this you can just run SABnzbd regularly:
```
python3 SABnzbd.py
```
or (from the sabnzbd directory):
```
./SABnzbd.py
```



## Something is broken on the Python 3 version?

Please create an issue at [Github](https://github.com/sabnzbd/sabnzbd/issues/new). Please check if the issue is unique for sabnzbd-python3, or also happens with sabnzbd-python2.

If you don't report the bugs, we can't fix them!




