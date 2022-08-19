---
title: External internet access
redirect_from:
    - /access-denied
---

This article is about the message `External internet access denied` (or `Access denied`) when trying to access SABnzbd and how to solve it.

# Introduction

When your SABnzbd is exposed (open) to the internet without a username and password, it could give a person with bad intentions the ability to download files to anywhere on your system that SABnzbd can access.
On Windows, such a person would also be able to download a script and execute it to gain full control over your system.

If you try to access SABnzbd and you get `External internet access denied`, the cause is that you or the software/services that you are using are trying to access SABnzbd from a device on the internet.
By default, because of the security reasons mentioned above, SABnzbd refuses such connections from sources on the internet.

# Quick fix for `External internet access denied`

If you want to give devices on the internet access to the full SABnzbd interface, go to [General](/wiki/configuration/{{site.wiki_version}}/general) page of the Config,
and at `External internet access`, select `Full Web interface`  or `Full Web interface - Only external access requires login`.

# Definition of internet versus non-internet/local

Internet is defined as "a public IP address". That access is denied by default.

Local means a private IP address (`192.168.x.x`, `10.x.x.x` and `172.16.x.x`). Access from your LAN, virtual machine, docker container, or similar will not lead to `External internet access denied` unless [`local_ranges` have been defined](#define-local-ranges).

# Advanced options
## Commandline parameter

From the command line, you can set `External internet access` with:

```
--inet_exposure <0..5>  Set external internet access
```

## Setting in `sabnzbd.ini`

The relevant setting in sabnzbd.ini is `inet_exposure`, with these values:

```
    0 = No access (default)
    1 = Add NZB files
    2 = API (no Config)
    3 = Full API
    4 = Full Web interface
    5 = Full Web interface - Only external access requires login
```


## Only allow API access from the internet

If you only want to give access to the API interface (so no Web access), select one of the first "API" options in the SABnzbd's WebGUI.
If you don't know what this means, don't use this option.


## Define local ranges

For the very advanced users: on the [Specials](/wiki/configuration/{{site.wiki_version}}/special) page of the Config you can define your own local ranges if you want to overrule what SABnzbd defines as local. Make sure to read the documentation on how to specify them.

## Disabling the error message

If you just want to disable the error message, you can do so by turning off `api_warnings` on the [Special](/wiki/configuration/{{site.wiki_version}}/special) page of the Config.
