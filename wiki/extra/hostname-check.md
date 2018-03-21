---
title: Hostname verification
redirect_from:
    - /hostname-check
---

# Why do I get an `Access denied` error?

Due to something called [DNS hijacking](https://en.wikipedia.org/wiki/DNS_hijacking), attackers could access your SABnzbd installation even if you have not exposed it to the internet.

In short, when you visit a website `evil.com` your browser will not allow it to access your SABnzbd running on `localhost`. However, attackers can use DNS hijacking with a sub-domain `attack.evil.com` that points to `127.0.0.1` (same as `localhost`).

Your browser will allow Javascript running on `evil.com` to access `attack.evil.com`, since that domain now actually points to your SABnzbd they can access it from within the browser. This can also happen if `evil.com` is somehow injected as a hidden frame into a hacked non-evil website.

This attack path was recently identified in other software ([CVE-2018-5702](http://www.cvedetails.com/cve/CVE-2018-5702/)) that uses a web-interface setup similar to SABnzbd.

To prevent this, in SABnzbd 2.3.3 measures were taken and a new [Special](/wiki/configuration/{{ site.wiki_version }}/special) setting was introduced called `host_whitelist` where you can specify what URL's that are allowed to represent your SABnzbd.

# How can I access my setup again from a custom URL?

1. Add your host to `host_whitelist` in the [Specials](/wiki/configuration/{{ site.wiki_version }}/special) page of the Config. You can also edit the `sabnzbd.ini` [directly](/wiki/advanced/directory-setup). <br>Only include the hostname, separate multiple values by `,`.
2. Enable a Username and Password in the [General](/wiki/configuration/{{ site.wiki_version }}/general) page of the Config.
3. Access SABnzbd directly through it's IP address (if exposed).