---
title: Firewalls and Virus scanners
---

# Firewalls

Firewalls can interfere with a program's Internet communication, often without telling you about it. If SABnzbd cannot connect, check your firewall's logging and settings.

SABnzbd uses the following types of communication:

**Outgoing:**

* DNS traffic: during startup it may communicate with an external DNS server to find out network information.
* Usenet servers: port 563 (SSL, recommended) or 119, although some providers use other ports.
* Fetching NZBs from indexers and websites: ports 443 and 80.
* Sending email notifications: port 25, 587, 465 or others.
* Checking `sabnzbd.org` for the latest release: port 443.

**Incoming:**

* Web interface: the user interface is a website, so SABnzbd has to "listen" on a port of your choice (default `8080`). Some firewalls will even complain about the use of localhost.

# Virus scanners

SABnzbd's Windows releases are code-signed (signing provided by [SignPath](https://signpath.io/)), so virus scanners and Windows Defender should not flag SABnzbd itself as a problem.

However, virus scanners can still slow down downloading: not all of them handle large, growing files well. When you are downloading a large file, the scanner may want to re-scan it every time a piece is added. It is better to exclude SABnzbd's Temporary Download Folder and Completed Download Folder from so-called on-access scanning; your scanner's scheduled system scan will still check the downloaded files later.

SABnzbd itself does not execute any downloaded file, so no viruses will be activated by SABnzbd.
