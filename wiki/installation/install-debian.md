---
title: SABnzbd installation on Debian
---

## Notice About Application Versions

Debian has a _very_ long development cycle as part of their intentional focus on stability. This means if you pull SABnzbd directly from APT you will _almost certainly_ recieve a version that is considered unsupported by the SABnzbd team. For example, at time of writing the version present in Debian Stable is two years out of date, and it will likely reach 2.5 years of being outdated by the time the next Stable version of Debian ships.

If your base distribution is Debian we _strongly_ recommend using some kind of containerized solution to install SABnzbd, be it Docker, Flatpak, Snapcraft, or something else. Those options are documented on the main [Unix Installation page](/wiki/installation/install-unix).

## Installing from Debian Backports

If you _must_ install from APT we recommend you use [Debian Backports](https://backports.debian.org/) to ensure you receive an actually up-to-date version of SABnzbd. These specific instructions are based on the current stable version of Debian 'Bookworm', but the instructions should hold true for future releases as well, just swap out all references to `bookworm` to `trixie` or whatever future Debian release you are running.

- Edit `/etc/apt/sources.list` with sudo / as root
- Confirm that your existing sources include Debian's `main`, `contrib`, and `non-free` repos. Your configuration should look something like this:

    ```
    deb http://deb.debian.org/debian/ bookworm main contrib non-free
    deb-src http://deb.debian.org/debian/ bookworm main contrib non-free

    deb http://security.debian.org/debian-security bookworm-security main contrib non-free
    deb-src http://security.debian.org/debian-security bookworm-security main contrib non-free

    deb http://deb.debian.org/debian/ bookworm-updates main contrib non-free
    deb-src http://deb.debian.org/debian/ bookworm-updates main contrib non-free
    ```

- NOTE: You may have _other_ repos like `non-free-firmware`, that's OK please keep any extra lines, just make sure you at least have `main`, `contrib`, and `non-free` and add whichever of them you don't already have to each line.
- Add the `bookworm-backports` repo at the bottom:

    ```
    deb http://deb.debian.org/debian bookworm-backports main contrib non-free
    ```

- Save the file
- Update apt: `sudo apt update`
	- It should show you downloading any contrib / non-free repo metadata you didn't previously have
- Install SABnzbd from backports: `sudo apt install -t bookworm-backports sabnzbdplus`
	- NOTE: This will JUST install the packages from backports if it provides specific versions we request (like `python3-sabctools`), but will prefer your stable packages if possible (like `unrar`)
- That's it, you've installed SABnzbd from Debian Backports.

With installation completed you can start SABnzbd manually by running:

```
sabnzbdplus
```

Or alternatively, you can proceed to the [How to Run as a Service](/wiki/installation/install-ubuntu-repo#toc3) section of the Ubuntu instructions to have SABnzbd run automatically on boot.