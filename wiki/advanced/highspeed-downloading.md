---
title: High speed Downloading
---
If you have a fast Internet connection (60MB/s aka 500 Mbps, and over) and are not getting the full speeds you require, 
there are a few steps that you can take to diagnose what is causing the limitation.

# Diagnosing speed limitations

Open the Status window ( <span class="glyphicon glyphicon-wrench"></span> ), run the tests ( <span class="glyphicon glyphicon-repeat"></span> ) and check the following:

<img src="/images/wiki/highspeed-downloading.png" alt="Diagnostics" style="float: right; width: 450px; border: 1px solid #ddd; margin: 3px">

1. Is the speed listed as **Internet Bandwidth** near your expected bandwidth?<br>
   If not, make sure the network connection to your device is working correctly.<br>
   Test your device's speed via [fast.com](https://fast.com/).
2. Is the **Pystone** score at least 100.000 or above?<br>
   If the score is lower than this, the CPU in your device is either too slow or something else is preventing SABnzbd from using its power.
3. Is the **Folder Speed** at least 150MB/s?<br>
   Both Incomplete and Complete should be on a SSD/M.2/NVMe disk.
4. Download the **10GB test download**, is the speed higher than on regular downloads?
5. After this, do you see **Download speed limited by** Disk Speed in the Status Window?<br>
   If so, either your disk are too slow or something is preventing SABnzbd from writing fast to your disks.

<span class="label label-warning">NOTE</span> When you seek support on our forums/Discord/Reddit, please make sure that you have used the diagnostics above and report the results.

# Optimizations

* Make sure `Maximum line speed` in [Config-&gt;General](/wiki/configuration/{{site.wiki_version}}/general) is set to the correct value for your connection.
* Try different connection numbers for your servers. Start with 8 and increase from there. A higher number will increase the overhead so more connections might actually reduce your speed.
* Turn Off `Direct Unpack` in [Config-&gt;Switches](/wiki/configuration/{{site.wiki_version}}/switches) to reduce disk load.
* Turn On `Pause Downloading During Post-Processing` in [Config-&gt;Switches](/wiki/configuration/{{site.wiki_version}}/switches). This will reduce disk load, as downloading and post-processing are not performed simultaneously.
* Change [SSL Ciphers](/wiki/advanced/ssl-ciphers) to `AES128` or `CHACHA20` in [Config-&gt;Servers](/wiki/configuration/{{site.wiki_version}}/servers). This can slightly reduce CPU load.
* Turn off `Unwanted Extensions` and `Action when encrypted RAR is downloaded`, as these use a substantial amount of disk and CPU power.
