---
title: SABnzbd and SSL/TLS security
redirect_from: "/certificate-errors"
---
Usenet (aka News servers) offers SSL/TLS security. It's called NNTPS, or NNTP with SSL. Just like HTTPS, it has two functions:

1. Confirm you really are talking to the server you want to talk to.
2. Encrypts communications between client and server so others can't see information like your login credentials and what you are downloading.

When you add a new server and enable SSL its `Certificate verification` setting will be set to `Strict` by default which enforces both functions described above.

There are still a lot of [non-secure news servers](https://www.appelboor.com/newsservers/newsservers-with-SSL.html) around. Therefore, the default setting for existing servers is only `Minimal`. You can set it to `Strict` yourself in the Advanced settings on the [Servers](/wiki/configuration/{{ site.wiki_version }}/servers) page.

You can completely turn-off SABnzbd's security checks and encryption, but you won't have the security described above.

-------------------

Online news server SSL/TLS check
-------------------

<form class="form-inline newsserver-test">
  <div class="form-group">
    <input type="text" class="form-control" id="newsserver-address" placeholder="News server address">
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

News server problems
-------------------
**Q: I get this error message "untrusted certificate". What can I do?**

    Failed to connect: Server news.someserver.com uses an untrusted certificate [[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)]

**A: Your news server does not have valid certificates to verify its identity. The certificates are self-signed and cannot be verified by a [trusted authority](https://en.wikipedia.org/wiki/Certificate_authority) or they are malicious.**

Solutions:

1. Easy but **not** secure: Don't use SSL (untick SSL).
2. Easy but **less** secure: Tell SABnzbd to ignore the problem: in SABnzbd's Server-settings, under Advanced, set `Certificate verification` to `Disabled`.<br> <span class="label label-danger">WARNING</span> Disabling this check allows anyone to redirect and intercept your traffic using *any* certificate! It is comparable to not using SSL at all.
3. Hard but secure: Test the status of your news server online (above) or check out the [News servers with SSL/TLS overview](https://www.appelboor.com/newsservers/newsservers-with-SSL.html).

    1. If the test (or overview) shows an error message such as '`OK NOK NOK`' or '`NOK NOK NOK`', the problem is on the side of the news server. You can ask the news server provider to fix this. But, they could deny there is a problem.

    2. If the test says '`OK OK OK`' or '`OK OK NOK`', then the problem is local (i.e. your computer/NAS): incorrect certificates, a virusscanner doing strange things, or something else. This is not something SABnzbd can solve for you. And the solutions are OS-dependent.

* * *

**Q: I get this error message "hostname ... doesn't match"**

    Failed to connect: Server news.someserver.com uses an untrusted certificate [hostname 'news.someserver.com' doesn't match either of '*.othersite.com', 'othersite.com']

**A: Your news server provider has some level of SSL, but their setup is not correct: they are using certificates that do not belong to the hostname you're using.**

Solutions:

1. Easy and half/half-secure: in SABnzbd's Server-settings, under Advanced, set `Certificate verification` to `Default`/`Minimal`. Then try again.<br> <span class="label label-danger">WARNING</span> Disabling this check allows anyone to redirect and intercept your traffic using *any* valid certificate!  It is comparable to not using SSL at all.
2. You can ask the news server provider to fix this. But, they could deny there is a problem.

* * *

**Q: Which News server provider should I choose?**

**A: Choose one with '`OK OK OK`' on our [News servers with SSL/TLS overview](https://www.appelboor.com/newsservers/newsservers-with-SSL.html)**

* * *

**Q: I am a news server provider, what can I do?**

**A: That depends on your circumstances:**

* If you are a (Highwinds, Xennanews, etc) reseller, contact your wholesale provider (Highwinds, Xennanews, etc) to solve this. You will most likely need to provide a certificate to your provider.
* If you are hosting your own news server, contact your administrator.

-------------------

NZB / RSS Index site problems
-----------------------------

NZB / RSS Index sites are HTTPS sites. HTTPS/SSL/TLS problems on the server side are (in 2017) uncommon because web browsers have been rejecting incorrect SSL/TLS setups for some time.

**Q: I get a certificate error trying to read a RSS or NZB**

    Failed to retrieve RSS from https://nzbindex.nl/rss/?q=bla&sort=agedesc&max=25: hostname u'nzbindex.nl' doesn't match either of 'www.nzbindex.com', 'nzbindex.com'

**A: Open the same URL in your Chrome web browser on the same machine, and on another machine. If Chrome complains too, you know the problem is on the server side.**

Solutions:

1. Check if there is another URL that is secure. For example: nzbindex.COM is secure.
2. Contact the site owner and inform them of the problem.
3. Turn off `HTTPS certificate verification` in SABnzbd.

If Chrome does not complain, the problem might be on your side. This is not something SABnzbd can solve for you. And the solutions are OS-dependent.

-------------------

Tools to test SSL/TLS news servers and websites
-----------------------------------------------

* SSLshopper-website: [https://www.sslshopper.com/ssl-checker.html#hostname=newsreader.eweka.nl:563](https://www.sslshopper.com/ssl-checker.html#hostname=newsreader.eweka.nl:563)

* SSLlabs (only HTTPS checking): [https://www.ssllabs.com/ssltest/analyze.html?d=api.oznzb.com&latest](https://www.ssllabs.com/ssltest/analyze.html?d=api.oznzb.com&latest)

* Tool `gnutls-cli`
    * `gnutls-cli -p 563 newsreader.eweka.nl`
* Tool `testssl.sh`
* Tool `curl`
* Tool `wget`
* Python (2.7.9 or higher)
    * `python -c "import urllib2; response = urllib2.urlopen('https://api.oznzb.com/') "`

