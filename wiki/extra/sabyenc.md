---
title: SABYenc
redirect_from: "/sabyenc"
---

# Introduction to SAByenc

In SABnzbd 2.0.0 we introduce a new module called `sabyenc` to increase the download speed on CPU-limited devices.

The Windows- and MacOS-packages of SABnzbd automatically contain that module.

On other platforms (like Linux) you have to make sure the module is installed. The information below is for packagers and source code users on those platforms.

## Installation

Currently the module can only be installed via Python's packaging manager (pip) by running:

```
pip install sabyenc
```

On Ubuntu/Debian the full installation sequence is:
```
sudo apt-get install python-dev python-pip
sudo -H pip install sabyenc --upgrade
```
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
 
on start-up to make users aware of the change.

## Notes

<span class="label label-warning">NOTE</span> The regular `_yenc` module will stay supported and download speed will stay the same as in SABnzbd 1.x.

## Issues

If you experience any issues, please let us know on our [Forums](https://forums.sabnzbd.org/) or [Github](https://github.com/sabnzbd/sabnzbd/issues)!