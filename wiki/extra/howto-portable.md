---
title: How to make a portable installation
---

*Only for Windows*

Portable means that you can:

* Have an installation on an external medium (like a USB drive).
* Plug it into any PC and use it as is.
* You don't need to install anything on the PC.
* You don't need to change the setup.

# Use the official portable release

Download the "Windows Portable" ZIP from the [download page](/downloads) and unpack it to any location where you have write access, for example a USB drive.

Start SABnzbd by running the included `portable.cmd`. This starts SABnzbd with its settings file (`sabnzbd.ini`) stored inside the SABnzbd folder itself, so the installation is fully self-contained.

Any extra command line parameters you give to `portable.cmd` are passed on to SABnzbd. For example, to set the web interface address and port:

```
portable.cmd -s 127.0.0.1:8080
```

# Tips

* Make sure that all folders in the configuration are relative paths, starting from the folder where the INI file is.
* Use `127.0.0.1`, `localhost` or `0.0.0.0` as the web server address.
* Choose a port number that is free on all systems (`8080` or `8088` is a good choice).

# Firewalls

You may encounter software firewalls which you will have to teach about SABnzbd.
SABnzbd has two types of network access: port 563 or 119 for communicating with the Usenet server, and port 8080 (or whatever else you choose) to communicate with the web browser.
