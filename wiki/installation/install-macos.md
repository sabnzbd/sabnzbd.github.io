---
title: Install SABnzbd for macOS
---

## The official App

If you just want to use SABnzbd, we provide a packaged application available [here](/downloads).
Pick the right folder for your macOS version and drag SABnzbd to the Applications folder.

----

## How to run from sources on macOS

Running the source Python (.py) files on a macOS system is not recommended unless you want to try the latest GitHub copy, or make changes yourself.

1. Make sure you have [Python 3.10 or higher](http://www.python.org) installed. Check with `python3 --version`.
2. Get a local copy (clone) of the SABnzbd source by running in the Terminal:

    ```
    git clone -b master https://github.com/sabnzbd/sabnzbd.git
    cd sabnzbd
    ```

3. Install the dependencies by running (might require Xcode):

    ```
    python3 -m pip install -r requirements.txt
    ```

4. Start SABnzbd by running:

    ```
    python3 SABnzbd.py
    ```

Your default web browser should now start and show the user interface of SABnzbd.

To update the source files to the latest version, open Terminal and run:

```
cd sabnzbd
git pull
```

----

## Running from Terminal

Should you ever need to run the compiled app from Terminal, this is the way:

```
/Applications/SABnzbd.app/Contents/MacOS/SABnzbd
```

If you need to see the logging output directly to the console:

```
/Applications/SABnzbd.app/Contents/MacOS/SABnzbd --console
```
