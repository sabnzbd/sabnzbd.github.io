---
title: Bonjour support
---

SABnzbd can announce itself on your local network using Apple's Bonjour protocol (also known as Zeroconf, or Avahi on Linux) and the Simple Service Discovery Protocol (SSDP). Other systems and apps on your network can then find your SABnzbd server automatically, without you having to mess around with IP addresses and port numbers.

The announcements are controlled by the `enable_broadcast` setting on the [Special](/wiki/configuration/{{ site.wiki_version }}/special) page of the Config.

# Limitation

Announcements only work when SABnzbd is set up to communicate with other computers on your local network. A completely local installation (listening on `127.0.0.1` or `localhost`) will not be advertised; the protocols do not support this. Start SABnzbd with host name `0.0.0.0` (or empty) so it is reachable from, and advertised to, your local network.

# macOS

There is nothing to install; Bonjour support is built into macOS.

# Windows

SSDP announcements work out of the box. For Bonjour announcements, Apple's [Bonjour Print Services for Windows](https://support.apple.com/kb/DL999) needs to be installed.

# Debian/Ubuntu

Install these two packages to get Bonjour working:

```
sudo apt-get install avahi-daemon libavahi-compat-libdnssd1
```

The separate tool `avahi-discover` (package name `avahi-discover`) can be handy, as it shows all Bonjour services on your LAN.
