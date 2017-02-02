**SABnzbd and SSL/TLS security**

Usenet (aka Newsservers) offers SSL/TLS security. It’s called NNTPS, or NNTP with SSL. 

Just like HTTPS, it has two functions:

* Are you really talking to the server you want to talk to.

* Others can’t see what is being sent between client and server. So others can’t see 1) your login credentials and 2) what you’re downloading.

As of SABnzbd version 1.2.0, SABnzbd by default actively checks SSL/TLS security. 

Currently there are still a lot of non-secure newsservers, most of them resellers of Highwinds / sslusenet. Apparently usenet administrators (and users) are not yet aware of the insecure setup.

The default setting of SABnzbd checking is therefore not yet very strict. You can set it to Strict yourself in the Advanced settings on the Servers page.

You can completely turn off SABnzbd’s security checking, but then your connection does not offer you the security of the two functions above.

This page tells what to do in case of problems.

**Newsserver problems **

Q: I get this error message "untrusted certificate". What is going on? What can I do?

[Errno 111] Failed to connect: Server news.someserver.com uses an untrusted certificate [[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)] [-1@news.someserver.com](mailto:-1@news.someserver.com):563

A: You can do different things:

1. Easy but not secure: Make the problem go away by not using SSL (Server-settings, untick SSL)

2. Easy but not secure: Ignore the problem, and instruct SABnzbd to ignore the problem: in SABnzbd’s Server-settings, under Advanced, set "Certificate verification" to Disabled. You have now an insecure SSL connection.

3. Hard, but secure: Try to find the cause of the problem: Check on [https://www.appelboor.com/newsservers/newsservers-with-SSL.html](https://www.appelboor.com/newsservers/newsservers-with-SSL.html) (and/or [https://www.appelboor.com/newsservers/check.html](https://www.appelboor.com/newsservers/check.html) ) the SSL/TLS-status of your newsserver. 

    1. If that site appelboor says gives an error message, and "OK NOK NOK" or “NOK NOK NOK”, the problem is on the side of the newsserver. You can ask the newsserver provider to solve that problem. That could be a hard path; the provider could deny they have a problem. 

    2. If that site says "OK OK OK" or “OK OK NOK” , the problem is on your own site (read: your computer/NAS): incorrect certificates, a virusscanner doing strange things, or something else. That is not something SABnzbd cannot solve for you. And it is OS-dependent how to solve that.

* * *


Q: I get this error message "hostname … doesn't match"

[Errno 111] Failed to connect: Server news.someserver.com uses an untrusted certificate [hostname 'news.someserver.com' doesn't match either of '*.othersite.com', 'othersite.com'] -1@news.someserver.com:563

A: your newsserver provider has some level of SSL, but the setup is not fully correct: they are using the certificates that do not belong to the hostname you’re using. That is not correct.

As of this writing about ⅓ of the newsserver provider have this problem. Most of them are resellers of Highwinds (which you can recognize by the error message "CertificateError: hostname 'news.someserver.com' doesn't match either of '*.sslusenet.com', 'sslusenet.com'")

You can do different things:

1. Easy and half/half-secure: in SABnzbd’s Server-settings, under Advanced, set "Certificate verification" to Default. Then try again.

2. Ask your newsserver provider to use the correct SSL keys on their newsserver

* * *


Q: Which Newsserver provider should I choose & use?

A: Choose one with triple OK on [https://www.appelboor.com/newsservers/newsservers-with-SSL.html](https://www.appelboor.com/newsservers/newsservers-with-SSL.html)

* * *


Q: I am a newsserver provider, what can I do?

That depends on how you do your newsserver:

* If you are a (Highwinds, Xennanews, etc) reseller, contact your wholesale provider (Highwinds, Xennanews, etc) to solve this. You will most likely need to provide a certificate to your provider

* If you are hosting your own newsserver, contact your newsserver administrator

**NZB / RSS Index site problems**

NZB / RSS Index sites are HTTPS sites. HTTPS/SSL/TLS problems on the server side are now (2017) uncommon because web browsers have been rejecting incorrect SSL/TLS setup for some time now.

Q: I get "hostname u'indexer.com' doesn't match “ trying to read a RSS or NZB

Failed to retrieve RSS from https://nzbindex.nl/rss/?q=bla&sort=agedesc&max=25: hostname u'nzbindex.nl' doesn't match either of 'www.nzbindex.com', 'nzbindex.com'

A: Open the same URL in your Chrome web browser on the same machine, and on another machine. If Chrome complains too, you know the problem is on the server side.

Thinks you can do:

1. Check if there is another URL that is secure. For example: nzbindex.COM is secure

2. Contact the site owner and tell him about the problem

3. Turn off "HTTPS certificate verification" in SABnzbd

If Chrome does not complain, the problem might be on your side. That is not something SABnzbd cannot solve for you. And it is OS-dependent how to solve that.

**Tools to test SSL/TLS news servers and websites**

* SSLshopper-website: [https://www.sslshopper.com/ssl-checker.html#hostname=newsreader.eweka.nl:563](https://www.sslshopper.com/ssl-checker.html#hostname=newsreader.eweka.nl:563)

* SSLlabs (only HTTPS checking): [https://www.ssllabs.com/ssltest/analyze.html?d=api.oznzb.com&latest](https://www.ssllabs.com/ssltest/analyze.html?d=api.oznzb.com&latest)

* Tool gnutls-cli

    * gnutls-cli -p 563 newsreader.eweka.nl

* Tool testssl.sh 

* Tool curl

* Tool wget

* Python (2.7.9 or higher)

    * python -c "import urllib2; response = urllib2.urlopen('https://api.oznzb.com/') "

