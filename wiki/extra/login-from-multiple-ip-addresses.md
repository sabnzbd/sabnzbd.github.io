---
title: Login from multiple IP addresses
redirect_from:
    - /multiple-adresses
---

If you get the warning `Login from multiple different IP addresses`, it means your news server provider sees your account logging in from different IP addresses.
News server providers often don't allow this, because it looks like you're sharing your account with someone else. However, the cause is often different: you're not sharing your account, but your logins do come from different IP addresses.

# Possible causes

1. You're switching between VPN and no-VPN, or between a fixed and a mobile internet connection.
2. Your account is used from a different location at the same time, by you or maybe someone else (= account sharing).
3. You have more than one (combined) internet connection, for example two mobile connections, or fixed plus mobile.
4. SABnzbd is switching between IPv4 and IPv6.
5. Your ISP uses a technology called "CGNAT" (Carrier Grade NAT), in which you share one IP address with other ISP customers, and that IP address can change between sessions.

# Things worth trying

* Avoid the situations listed above where possible.
* If you're behind CGNAT, hopefully your ISP also provides IPv6. You can check the IPv6 address in SABnzbd in the Status and Interface settings (<span class="glyphicon glyphicon-wrench"></span>) window. If so, use the IPv6 address of your news server.
