---
title: SSL Ciphers
---

## Summary

Setting SSL Ciphers to the following value will lower encryption strength, increase performance (download speed) and is supported by virtually all news servers:

```
AES128
```

Ciphers like `AES128` only apply to TLS 1.2 and older. Setting custom ciphers forces the maximum TLS version to 1.2, unless you also specify TLS 1.3 cipher suites (see below).

<span class="label label-warning">NOTE</span> Some older CPUs might lack AES hardware acceleration and `CHACHA20` might be faster than `AES128`.

## What are SSL ciphers?

When you connect to a news server using SSL/TLS, the first step in the connection process is for SABnzbd and the server to agree how the connection will be secured. The SSL/TLS specifications, such as TLSv1.2, define which protocols can and should be used. These protocols define how the security keys will be exchanged and how the actual data will be encrypted. As you can imagine, stronger encryption requires more CPU power to decode.

During the initial stage of the connection, the handshake, SABnzbd and the server will let each other know which protocols they support and then use the strongest available on both. By modifying the SSL Ciphers setting, you can specify what SABnzbd should report as available protocols.

When there are active connections, you can see which protocol is being used for each server in the Status and Interface settings (<span class="glyphicon glyphicon-wrench"></span>, Connections). For example: `TLSv1.2 (DHE-RSA-AES128-SHA)`.

## What are the options?

SABnzbd will use the OpenSSL library that's available on your system or that's part of Python.

You can see which ciphers are available on your system by executing `openssl ciphers -v` on the command line. All the strings on the left of the table can be used as an SSL Ciphers setting.

You can see which TLS 1.3 suites are available on your system by executing `openssl ciphers -v -tls1_3`.

It is also possible to specify multiple single cipher settings or a family of ciphers by specifying it in OpenSSL Cipher format. More information can be found here: [https://www.openssl.org/docs/manmaster/man1/openssl-ciphers.html](https://www.openssl.org/docs/manmaster/man1/openssl-ciphers.html).

## TLS 1.3 cipher suites

TLS 1.3 uses its own cipher suites, named like `TLS_AES_128_GCM_SHA256`. These can only be set when SABnzbd (5.2+) runs on Python 3.15 or newer.

If the SSL Ciphers setting contains a name starting with `TLS_`, SABnzbd will no longer limit the connection to TLS 1.2 and will set the TLS 1.3 cipher suites using the value you entered. Multiple suites can be separated with a colon:

```
TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256
```

When doing so, only the TLS 1.3 suites are taken from your setting. If the server does not support TLS 1.3, SABnzbd will fall back to TLS 1.2 using the default (`HIGH`) ciphers, so any TLS 1.2 ciphers in the same setting are ignored. Only use this if you know your news server supports TLS 1.3.

## What are the risks?

Setting your SSL Ciphers to `AES128` will not suddenly expose your traffic to the world. There is evidence that this and similar protocols can be decrypted, but it seems to require a large amount of resources.

It's up to you to decide how valuable your usenet data is. It should also be noted that your internet service provider will always be able to see to which IP-address you are connecting, with or without SSL. Enabling SSL only shields the contents of the connection, not the target.
