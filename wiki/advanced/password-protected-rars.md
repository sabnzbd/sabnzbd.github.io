---
title: Password-protected RARs
---

Sometimes you encounter encrypted (or password-protected) RARs. It's only useful to download a password protected post when you know the password upfront. Trying to get a password afterwards is probably a waste of your time and/or money.

SABnzbd will try all available passwords when it detects an encrypted job during the downloading. If none of the passwords work you can set to automatically [Pause or Abort](/wiki/configuration/{{ site.wiki_version }}/switches) the download.

----

## Password per NZB

Supposing you know the required password, you can give it to SABnzbd before the download starts post-processing.
You can do this like this:

* In the NZB file name you can embed the password like this: {% raw %}`My Job {{PW}}.nzb`{% endraw %} or `My Job password=PW.nzb`.
  This will set the job name to `My Job` and the password to `PW`.
* When the job is in the queue, hover over the job and click the <span class="glyphicon glyphicon-folder-open"></span> icon.
  At the top of the files list you can set the password.
* You can also rename the job in the queue.
  `My Job / PASSWORD` will set the password. The `/` is used as a separator because it cannot be part of a folder name.
  The folder name will be `My Job` and `PASSWORD` will be used as the decryption password when unpacking.

The password can be changed until the job enters the post-processing queue.

## Inside the NZB

Indexers and NZB suppliers can include the password inside the NZB `head` section (see [NZB specification](/wiki/extra/nzb-spec)):

{% highlight html %}
<meta type="password">secret</meta>
{% endhighlight %}

Or as the `x-dnzb-password` header when SABnzbd fetches the URL.

----

## Password file

If you don't set a password per job, you can create a text file containing all passwords to be tried.
It's a simple text file (created with Notepad, VI or TextEdit) and should contain one password per line.
Specify where the file is in [Config->Folders](/wiki/configuration/{{ site.wiki_version }}/folders).

<span class="label label-warning">NOTE</span> Checking passwords is not very fast, the more passwords you list in the file the longer it will take and the more CPU power is lost. Do not list more than ~20 passwords in this file.
