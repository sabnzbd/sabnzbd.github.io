---
title: Android
---

<span class="label label-warning">NOTE</span> Experimental and advanced.

It is possible to run SABnzbd on a plain, standard Android device.

## Basic installation

1. On your Android device, install the app [UserLAnd](https://play.google.com/store/apps/details?id=tech.ula).
2. While setting up UserLAnd, choose Ubuntu and ssh.
3. Start UserLAnd. On the command line, run `sudo apt-get install sabnzbdplus`.
4. Start SABnzbd with `sabnzbdplus`.
5. On your Android device, access SABnzbd via [http://127.0.0.1:8080](http://127.0.0.1:8080).
6. You can now fill out the wizard.

This gives you the SABnzbd version included with the Ubuntu release, which is usually outdated.

## Update to the latest SABnzbd

With some extra work, you can update to the current version of SABnzbd. On the command line of Ubuntu-on-Android, run:

```
sudo apt update -y
sudo apt-get install software-properties-common -y
sudo add-apt-repository ppa:jcfp/ppa -y
sudo apt-get install sabnzbdplus -y
```

You can start SABnzbd with:

```
sabnzbdplus
```

You can access SABnzbd via [http://127.0.0.1:8080](http://127.0.0.1:8080).

## Share downloads to Android

There are shared directories between UserLAnd and Android.

For internal storage:

* UserLAnd: `/storage/internal/`
* Android app "Files", "Internal storage": `/Android/data/tech.ula/files/storage`

For SD card (if any):

* UserLAnd: `/storage/sdcard/`
* Android app "Files", "SD Card": `/Android/data/tech.ula/files/storage`

So, in SABnzbd set the Completed Download Folder to `/storage/internal/`.

## Remote access to Ubuntu-on-Android

You can access Ubuntu-on-Android via SSH like this:

```
ssh <ip address of Android device> -p 2022
```
