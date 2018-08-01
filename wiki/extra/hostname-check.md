---
title: Hostname verification
redirect_from:
    - /hostname-check
---

This article is about the message 'Refused connection with hostname "sabnzbd.special.com"', and how to solve it.

# Introduction

Due to something called [DNS hijacking](https://en.wikipedia.org/wiki/DNS_hijacking), attackers could access your SABnzbd installation even if you have not exposed it to the internet.

To prevent this, in SABnzbd 2.3.3 measures were taken and a new [Special](/wiki/configuration/{{ site.wiki_version }}/special) setting was introduced called `host_whitelist` where you can specify what URL's that are allowed to represent your SABnzbd.

For normal usage (ie access from your LAN), SABnzbd will fill out this setting automatically with your hostname and you don't have to do anything at all.

# How can I access my setup again from a custom URL, or: How can I get can rid of the error message?

You can choose **one** of the following methods to allow access:

- Just add the host name or the full name ('FQDN') shown in the error message to `host_whitelist` in the [Specials](/wiki/configuration/{{ site.wiki_version }}/special) page of the Config. You can also edit the `sabnzbd.ini` [directly](/wiki/advanced/directory-setup). So, if you use for example `http://sabnzbd.special.com:8080/` to access SABnzbd, then add `sabnzbd.special.com` to `host_whitelist`, **or**
- Access SABnzbd directly through it's IP address, **or**
- Enable a Username and Password in the [General](/wiki/configuration/{{ site.wiki_version }}/general) page of the Config.


# Technical background

In short, when you visit a website `evil.com` your browser will not allow it to access your SABnzbd running on `localhost`. However, attackers can use DNS hijacking with a sub-domain `attack.evil.com` that points to `127.0.0.1` (same as `localhost`).

Your browser will allow Javascript running on `evil.com` to access `attack.evil.com`, since that domain now actually points to your SABnzbd they can access it from within the browser. This can also happen if `evil.com` is somehow injected as a hidden frame into a hacked non-evil website.

This attack path was identified in January 2018 in other software ([CVE-2018-5702](http://www.cvedetails.com/cve/CVE-2018-5702/)) that uses a web-interface setup similar to SABnzbd.

# Why do I get an `Access denied` error?

If SABnzbd is accessed via an unexpected name, this will happen:

In the webbrowser trying to access SABnzbd, you'll see
```
Access denied - Hostname verification failed: https://sabnzbd.org/hostname-check
```

In the SABnzbd GUI (with access) and in sabnzbd.log you will see
```
Refused connection with hostname "superbox" from: ::1>Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
```
or
```
Refused connection with hostname "mysabhost.duckdns.org" from: ::ffff:2.14.253.70>Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36
```




