# "Access Denied" when trying to access SABnzbd

If you try to access SABnzbd and you get "access denied", the cause is that you're trying to access SABnzbd from an device on Internet. 
By default, because of security reasons, SABnzbd refuses such connections from Internet

## Solve "access denied" via SABnzbd's WebGUI

If you want to give SABnzbd WebGUI access to devices on Internet, go into SABnzbd -> Config -> General, 
and at "External internet access", select "Full Web interface"  or "Full Web interface - Only external access requires login"


## Advanced: only API access from Internet

If you only want to give access to the API interface (so no Web access), select one of the first "API" options.

## Advanced: Commandline parameter

From the commandline, you can specify the internet exposure with:

```
--inet_exposure <0..5>  Set external internet access
```

## Advanced: in sabnzbd.ini

The relevant setting in sabnzbd.ini is `inet_exposure = 4`

## Very Advanced: define local ranges

For the very advanced users: via Config -> Special you can define your own local ranges. 

## Values for inet_exposure

```
    0=no access
    1=nzb
    2=api
    3=full_api
    4=webui
    5=webui with login for external
```
    


