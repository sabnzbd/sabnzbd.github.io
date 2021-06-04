# "Access Denied" when trying to access SABnzbd

# Introduction

If you try to access SABnzbd and you get "access denied", the cause is that you're trying to access SABnzbd from an device on Internet. 
By default, because of security reasons, SABnzbd refuses such connections from Internet

# Quick fix for "access denied"

If you want to give SABnzbd WebGUI access to devices on Internet, go into SABnzbd's WebGUI -> Config -> General, 
and at "External internet access", select "Full Web interface"  or "Full Web interface - Only external access requires login"

# Definition of Internet versus non-Internet/local

Internet is defined as "a public IP address". That access is denied by default.

Local means a private IP address (192.168.x.x, 10.x.x.x and 172.16.x.x). Access from your LAN, virtual machine, docker container or similar will not lead to "access denied" unless "local ranges" has been defined (see #define-local-ranges).

# Advanced options
## Commandline parameter

From the commandline, you can specify the internet exposure parameter with:

```
--inet_exposure <0..5>  Set external internet access
```

## Setting in sabnzbd.ini

The relevant setting in sabnzbd.ini is `inet_exposure`, with these values:

```
    0=no access (default)
    1=nzb
    2=api
    3=full_api
    4=webui
    5=webui with login for external
```


## Only allow API access from Internet (no WebGUI)

If you only want to give access to the API interface (so no Web access), select one of the first "API" options in the SABnzbd's WebGUI.
If you don't know what this means, don't use this option.


# Very advanced (danger zone)

## Define local ranges

For the very advanced users: via Config -> Special you can define your own local ranges if you want to overrule what SABnzbd defines as local.



    


