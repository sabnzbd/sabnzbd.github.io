---
title: SSL Ciphers
---

## Summary

Setting SSL Ciphers to the following value will lower encryption strength, increase performance (download speed) and is supported by virtually all news servers:

```
AES128
```

<span class="label label-warning">NOTE</span> Setting the SSL Cipher with news servers that support TLS 1.3 connections is not (yet) supported by Python and thus SABnzbd. Setting custom ciphers forces the maximum TLS version to 1.2.

Increases in download speed are most notable on systems where CPU power is the limiting factor.
Note that some older CPUs might lack AES hardware acceleration and `CHACHA20` might be faster than `AES128`.

## What are SSL ciphers?

When you connect to a news server using SSL/TLS, the first step in the connection process is for SABnzbd and the server to agree how the connection will be secured. The SSL/TLS specifications, such as TLSv1.2, define which protocols can and should be used. These protocols define how the security keys will be exchanged and how the actual data will be encrypted. As you can imagine, stronger encryption requires more CPU power to decode.

During the initial stage of the connection, the handshake, SABnzbd and the server will let each other know which protocols they support and then use the strongest available on both. By modifying the SSL Ciphers setting, you can specify what SABnzbd should report as available protocols.

When there are active connections, you can see which protocol is being used for each server in the Status and Interface settings (<span class="glyphicon glyphicon-wrench"></span>, Connections). For example: `TLSv1.2 (DHE-RSA-AES128-SHA)`.

## What are the options?

SABnzbd will use the OpenSSL library that's available on your system or that's part of Python.

You can see which ciphers are available on your system by executing `openssl ciphers -v` on the command line. All the strings on the left of the table can be used as an SSL Ciphers setting.

It is also possible to specify multiple single cipher settings or a family of ciphers by specifying it in OpenSSL Cipher format. More information can be found here: [https://www.openssl.org/docs/manmaster/man1/openssl-ciphers.html](https://www.openssl.org/docs/manmaster/man1/openssl-ciphers.html).

## What are the risks?

Setting your SSL Ciphers to `AES128` will not suddenly expose your traffic to the world. There is evidence that this and similar protocols can be decrypted, but it seems to require a large amount of resources.

It's up to you to decide how valuable your usenet data is. It should also be noted that your internet service provider will always be able to see to which IP-address you are connecting, with or without SSL. Enabling SSL only shields the contents of the connection, not the target.
