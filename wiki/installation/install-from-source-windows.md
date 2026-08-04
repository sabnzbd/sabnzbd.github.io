---
title: Install SABnzbd for Windows from source
---

Running the source Python (.py) files on a Windows system is not recommended unless you want to try the latest GitHub copy, or make changes yourself.

1. Install Python 3.10 or higher from [Python.org](http://www.python.org/).
2. Install [Git for Windows](https://git-for-windows.github.io/) on your system. The default options are OK.
3. Get a local copy (clone) of the SABnzbd source by opening Git Bash from the start menu and running:

    ```
    git clone -b master https://github.com/sabnzbd/sabnzbd.git
    ```

    Press "Insert" instead of "Ctrl+V" to paste into Git Bash.
    You can specify the target directory as a second argument if you don't want it in the default location (`C:\Users\USERNAME\sabnzbd\`).

4. Install the required modules by opening a Command Prompt or Git Bash, navigating to the location of the Git clone, and running:

    ```
    cd sabnzbd
    pip install -r requirements.txt
    ```

5. To enable multi-language support, run in the same window:

    ```
    python tools/make_mo.py
    ```

6. You can start SABnzbd by running in the Command Prompt or Git Bash:

    ```
    python C:\Users\USERNAME\sabnzbd\SABnzbd.py
    ```

To update the source files to the latest version, open Git Bash and type:

```
cd sabnzbd
git pull
```

Optional (hide the console window when SABnzbd is launched):

* Create a `.cmd` file to easily launch SABnzbd such as: `python "path\to\folder\SABnzbd.py"`.
* Put a shortcut to the `.cmd` file in your startup folder, and set it to start as minimized.
