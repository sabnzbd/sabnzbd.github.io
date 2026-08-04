---
title: Webserver using HTTPS
---

To make the communication between SABnzbd and your web browser private, you can enable HTTPS (secured HTTP). The purpose of a certificate is two-fold: one is to give you encrypted communication, the other is to authenticate the server. The certificate authority guarantees that you are actually talking to the website of your bank or similar service. Web browsers are very fussy about the authentication part, and by default will complain unless you use a certificate issued by a trusted authority.

By default SABnzbd will create self-signed certificates for you to use. These will give browser warnings when you try to connect, but it is usually easy to make an exception for these certificates.

The default key and certificate are located inside the `admin` folder of the folder where your `sabnzbd.ini` is. For example:

```
Windows:
%localappdata%\sabnzbd\admin\server.cert
%localappdata%\sabnzbd\admin\server.key
Linux:
~/.sabnzbd/admin/server.cert
~/.sabnzbd/admin/server.key
```

You can change the location of these files by entering the full path to both in [Config->General](/wiki/configuration/{{ site.wiki_version }}/general).

If you want trouble-free communication you need a certificate from a Certificate Authority. [Let's Encrypt](https://letsencrypt.org/) issues these for free (see below); commercial authorities also sell them, but for just accessing SABnzbd there is no need to pay for one.

To turn on access using HTTPS, you need to enable HTTPS in [Config->General](/wiki/configuration/{{ site.wiki_version }}/general#toc1). This will enable HTTPS on the main listening port. If you want it to listen on a different port specific for HTTPS, you can specify this by clicking on Advanced.

<span class="label label-warning">NOTE</span> If you upgraded from an older version of SABnzbd, the HTTPS port (under Advanced) might be set to `9090`. Set it to empty to enable HTTPS on the main port.

If you expose SABnzbd to the Internet you can use `443` as port number, as this is the official number for HTTPS and allows you to not specify the port when accessing. Please note that using a port number below 1024 requires running as root under Linux.

## Creating a valid certificate using Let's Encrypt

If you run SABnzbd behind an Apache proxy, you can create free valid certificates using Let's Encrypt.
[A guide is available on the forums.](https://forums.sabnzbd.org/viewtopic.php?f=1&t=19684)

## Create a self-signed certificate with OpenSSL

From a command prompt type:

```
openssl genrsa 4096 > host.key
openssl req -new -x509 -nodes -sha256 -days 365 -key host.key > host.cert
```
