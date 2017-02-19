---
title: SABYenc
redirect_from: "/sabyenc"
---

In SABnzbd 2.0.0 we introduce a new `sabyenc` module to increase the download speed on CPU-limited devices. The Windows- and MacOS-versions of SABnzbd automatically contain that module. On other platforms (like Linux) you have to make sure the module is installed.

Currently this module can only be installed via Python's packaging manager (pip) by running:

```
pip install sabyenc
```
On Ubuntu/Debian this is the full sequence:
```
sudo apt-get install python-dev python-pip
sudo -H pip install sabyenc --upgrade
```
To check if sabyenc is installed, run this:
```
python -c "import sabyenc ; print sabyenc.__version__ "
```
It should print the version of the installed sabyenc module.

<span class="label label-warning">NOTE</span> The regular `_yenc` module will stay supported and download speed (should) stay the same.

In SABnzbd 2.0.0 and higher, not having the `sabyenc` module installed will result in an error `SABYenc module... NOT found! Expecting v2.7.0` on start-up to make test-users aware of the change.

If you experience any issues, please let us know on our [Forums](https://forums.sabnzbd.org/) or [Github](https://github.com/sabnzbd/sabnzbd/issues)!