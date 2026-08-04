---
title: IPv6
---

SABnzbd is fully IPv6 enabled: it can download from IPv6 enabled news servers, and you can access SABnzbd's web-interface over IPv6.

### Download from IPv6 enabled news servers

SABnzbd will automatically use IPv6 if available when connecting to news servers.
Based on Happy Eyeballs, SABnzbd will choose the quickest connection to a news server: via IPv4 or via IPv6.

See [IPv6 Staging](/wiki/advanced/ipv6-staging) for additional IPv6 features that are not yet enabled by default.

### Access SABnzbd's web-interface over IPv6

To access SABnzbd's web-interface over IPv6, you need to fill out `::` in [General](/wiki/configuration/{{ site.wiki_version }}/general) at the field "SABnzbd Host". Press Save Changes, and then restart SABnzbd.

As a first test, you should be able to access SABnzbd via `http://[::1]:8080/`.
If that works you can fill out the public IPv6 address of your system running SABnzbd, so something like `http://[2001:dead:beef:cafe:123:4567:b055]:8080/`

### Access SABnzbd over IPv6 from your LAN without login

To access SABnzbd over IPv6 from your LAN without login, you can fill out your IPv6 network prefix in the `local_ranges` setting on the [Special](/wiki/configuration/{{ site.wiki_version }}/special) page of the Config, so something like `2001:dead:beef:cafe::/64` (replace with your actual prefix).

### Access SABnzbd over IPv6 from the outside world

To access SABnzbd over IPv6 from the outside world, you need to configure your router to allow incoming connections on the SABnzbd port (default is 8080) for the local IPv6 addresses.
