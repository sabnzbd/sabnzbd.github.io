---
title: SABYenc
redirect_from: "/sabyenc"
---

In SABnzbd 2.0.0 we introduce a new `sabyenc` module to increase the download speed on CPU-limited devices.

Currently this module can only be installed via Python's packaging manager (pip) by running:

```
pip install sabyenc
```

<span class="label label-warning">NOTE</span> The regular `_yenc` module will stay supported and download speed (should) stay the same.

During testing for SABnzbd 2.0.0 not having the `sabyenc` module installed will result in an error on start-up to make test-users aware of the change.

If you experience any issues, please let us know on our [Forums](https://forums.sabnzbd.org/) or [Github](https://github.com/sabnzbd/sabnzbd/issues)!