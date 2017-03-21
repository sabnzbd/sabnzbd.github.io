---
title: SABnzbd and SSL/TLS security
redirect_from: "/certificate-errors"
---
Usenet (aka Newsservers) offers SSL/TLS security. It’s called NNTPS, or NNTP with SSL. Just like HTTPS, it has two functions:

* Are you really talking to the server you want to talk to.
* Others can’t see what is being sent between client and server. So others can’t see 1) your login credentials and 2) what you’re downloading.

As of SABnzbd version 1.2.0, SABnzbd by default actively checks SSL/TLS security.

Currently there are still a lot of non-secure newsservers. The default setting of SABnzbd checking is therefore not yet very strict. You can set it to `Strict` yourself in the Advanced settings on the [Servers](/wiki/configuration/{{ site.wiki_version }}/servers) page.

You can completely turn off SABnzbd’s security checking, but then your connection does not offer you the security of the two functions above.

This page tells what to do in case of problems.

-------------------

Online newsserver SSL/TLS check
-------------------

<form class="form-inline newsserver-test">
  <div class="form-group">
    <input type="text" class="form-control" id="newsserver-address" placeholder="Newsserver address">
    <button type="submit" class="btn btn-success">Test server <span class="glyphicon glyphicon-chevron-right"></span></button>
  </div>
</form>

<div class="progress newsserver-progress">
    <div class="progress-bar progress-bar-success progress-bar-striped active"></div>
</div>

<iframe id="newsserver-test-result" src=""></iframe>

<script type="text/javascript">
    $('.newsserver-test').on('submit', function() {
        // Clear first
        $('#newsserver-test-result').attr('src', '')
        // Show loading box
        $('.progress').show()
        // Fill the url
        $('#newsserver-test-result').attr('src', 'https://www.appelboor.com/cgi-bin/check_newsserver.py?server=' + $('#newsserver-address').val())
        // Track
        ga('send', 'event', 'servercheck', 'click', $('#newsserver-address').val(), {
                'transport': 'beacon'
            });
        return false
    })
    // Do the magic when done
    $('#newsserver-test-result').on('load', function() {
        $('.progress').hide()
        $(this).show();
    });

</script>


-------------------

Newsserver problems
-------------------
**Q: I get this error message "untrusted certificate". What is going on? What can I do?**

    Failed to connect: Server news.someserver.com uses an untrusted certificate [[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)]

**A: Your newsserver does not have valid certificates to verify it's identity. The certificates are self-signed and cannot be verified by a [trusted authority](https://en.wikipedia.org/wiki/Certificate_authority) or they are malicious.**

**You can do different things:**

1. Easy but not secure: Make the problem go away by not using SSL (untick SSL)
2. Easy but not secure: Ignore the problem, and instruct SABnzbd to ignore the problem: in SABnzbd’s Server-settings, under Advanced, set `Certificate verification` to `Disabled`. You have now an insecure SSL connection.
3. Hard, but secure: Try to find the cause of the problem: Check on [our Newsservers with SSL/TLS overview](https://www.appelboor.com/newsservers/newsservers-with-SSL.html) (and/or online newsserver SSL/TLS check above) the SSL/TLS-status of your newsserver.

    1. If the test or the overview shows an error message such as `OK NOK NOK` or `NOK NOK NOK`, the problem is on the side of the newsserver. You can ask the newsserver provider to solve that problem. That could be a hard path; the provider could deny they have a problem.

    2. If that site says `OK OK OK` or `OK OK NOK`, the problem is on your own site (read: your computer/NAS): incorrect certificates, a virusscanner doing strange things, or something else. That is not something SABnzbd cannot solve for you. And it is OS-dependent how to solve that.

* * *


**Q: I get this error message "hostname ... doesn't match"**

    Failed to connect: Server news.someserver.com uses an untrusted certificate [hostname 'news.someserver.com' doesn't match either of '*.othersite.com', 'othersite.com']

**A: your newsserver provider has some level of SSL, but the setup is not fully correct: they are using the certificates that do not belong to the hostname you're using. That is not correct.**

You can do different things:

1. Easy and half/half-secure: in SABnzbd’s Server-settings, under Advanced, set `Certificate verification` to `Default`. Then try again.<br> <span class="label label-warning">WARNING</span> Disabeling this check allows anyone to redirect and intercept your traffic using *any* valid certificate!
2. You can ask the newsserver provider to solve the problem. That could be a hard path; the provider could deny they have a problem.

* * *

**Q: Which Newsserver provider should I choose & use?**

**A: Choose one with triple OK on [our Newsservers with SSL/TLS overview](https://www.appelboor.com/newsservers/newsservers-with-SSL.html)**

* * *

**Q: I am a newsserver provider, what can I do?**

That depends on how your newsserver is set up:

* If you are a (Highwinds, Xennanews, etc) reseller, contact your wholesale provider (Highwinds, Xennanews, etc) to solve this. You will most likely need to provide a certificate to your provider
* If you are hosting your own newsserver, contact your newsserver administrator

-------------------

NZB / RSS Index site problems
-----------------------------

NZB / RSS Index sites are HTTPS sites. HTTPS/SSL/TLS problems on the server side are now (2017) uncommon because web browsers have been rejecting incorrect SSL/TLS setup for some time now.

**Q: I get a certificate error trying to read a RSS or NZB**

    Failed to retrieve RSS from https://nzbindex.nl/rss/?q=bla&sort=agedesc&max=25: hostname u'nzbindex.nl' doesn't match either of 'www.nzbindex.com', 'nzbindex.com'

**A: Open the same URL in your Chrome web browser on the same machine, and on another machine. If Chrome complains too, you know the problem is on the server side.**

Thinks you can do:

1. Check if there is another URL that is secure. For example: nzbindex.COM is secure
2. Contact the site owner and tell him about the problem
3. Turn off `HTTPS certificate verification` in SABnzbd

If Chrome does not complain, the problem might be on your side. That is not something SABnzbd cannot solve for you. And it is OS-dependent how to solve that.

-------------------

Tools to test SSL/TLS news servers and websites
-----------------------------------------------

* SSLshopper-website: [https://www.sslshopper.com/ssl-checker.html#hostname=newsreader.eweka.nl:563](https://www.sslshopper.com/ssl-checker.html#hostname=newsreader.eweka.nl:563)

* SSLlabs (only HTTPS checking): [https://www.ssllabs.com/ssltest/analyze.html?d=api.oznzb.com&latest](https://www.ssllabs.com/ssltest/analyze.html?d=api.oznzb.com&latest)

* Tool gnutls-cli
    * gnutls-cli -p 563 newsreader.eweka.nl
* Tool testssl.sh
* Tool curl
* Tool wget
* Python (2.7.9 or higher)
    * `python -c "import urllib2; response = urllib2.urlopen('https://api.oznzb.com/') "`

