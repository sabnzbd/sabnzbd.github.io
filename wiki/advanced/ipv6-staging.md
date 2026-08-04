---
title: IPv6 Staging
---

With `ipv6_staging`, you can activate special IPv6 features in SABnzbd that are not yet mainstream.

You can find `ipv6_staging` on the [Special](/wiki/configuration/{{ site.wiki_version }}/special) page of the Config.

## Features

### Enrich news servers with IPv6 connectivity

Some usenet providers have an IPv4-only news server, and a separate IPv6-only news server.
To be more exact: it's probably the same news server, but there is an IPv4-only name (FQDN), and an IPv6-only one.
For example: `news.eweka.nl` and `news6.eweka.nl`.

These providers want the user to specify this separate news server by hand.
However, this is more work for the user (a separate entry in the Server list), and it's annoying if the user has a laptop which sometimes has and sometimes hasn't got IPv6 connectivity.

SABnzbd solves this with the `ipv6_staging` feature: if you turn it on, SABnzbd will enrich
the IPv4-only name with the IPv6-only name (for well-known news servers).
Combined with Happy Eyeballs, SABnzbd will find the connection that works quickest.
This is fail-safe: if there is no IPv6, or it's slow, SABnzbd will use IPv4.

What is the advantage of using IPv6? With IPv6, you have no NAT (and no CGNAT), so the IPv6 connection might be faster.

You can turn on this feature even if you haven't (yet) IPv6.

Example logging in sabnzbd.log (with +Debug turned on):

```
2024-10-29 11:37:07,682::DEBUG::[downloader:218] Retrieving server address information for <Server: id=-1, host=news.eweka.nl:563>
2024-10-29 11:37:07,682::INFO::[happyeyeballs:136] Added alternative IPv6 address: news6.eweka.nl
2024-10-29 11:37:07,710::DEBUG::[happyeyeballs:168] Available addresses for news.eweka.nl (port=563, IPv4 or IPv6): 4 IPv4 and 3 IPv6
2024-10-29 11:37:07,719::DEBUG::[happyeyeballs:100] Happy Eyeballs connected to 2001:4de0:1::233 (news6.eweka.nl) in 8ms
2024-10-29 11:37:07,719::INFO::[happyeyeballs:201] Quickest IP address for news.eweka.nl (port=563, IPv4 or IPv6): 2001:4de0:1::233 (news6.eweka.nl)
2024-10-29 11:37:07,776::INFO::[newswrapper:336] -1@news.eweka.nl: Connected using TLSv1.3 (TLS_AES_256_GCM_SHA384)
```


