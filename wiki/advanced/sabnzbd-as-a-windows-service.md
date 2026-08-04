---
title: SABnzbd as a Windows Service
---

## Introduction

Running SABnzbd as a Windows Service can be helpful to those needing the program to operate in an "always on" state. When installed this way, SABnzbd will start automatically as soon as Windows starts, even when no user account is logged in, and will remain running even when all users have logged out.

<span class="label label-warning">NOTE</span> While the functionality of SABnzbd is generally the same when running as a service, there are some restrictions and limitations. Most importantly, you will need to take additional steps after installing the service if you use network shares for your download folders. Details on these steps, and other considerations when running SABnzbd as a service, can be found after the basic installation instructions below.

## Basic Installation

The following procedure will install SABnzbd as a service using the same settings used by the graphical web-based interface. This should satisfy most users' needs, but if you need to run the service with different settings than those used in the web interface, please read through the "Specifying additional options" section that follows this section before proceeding.

1. Make sure SABnzbd is not running.
2. Open a Command Prompt with Administrative (elevated) privileges:
    * Click your Windows Start button.
    * Type `cmd`.
    * Right click "Command Prompt" in the search window and choose "Run As Administrator" in the drop-down menu that appears.
3. Access the directory in which you installed SABnzbd.
   If you installed SABnzbd in its default location (`C:\Program Files\SABnzbd`) just type (or paste) the below command exactly as it appears, then hit the RETURN key. If you installed it to a different drive or folder, however, make sure to edit the path to reflect that location.

    ```
    cd "C:\Program Files\SABnzbd"
    ```

4. Install the SABnzbd service, set it to automatically start, and launch it, by typing or pasting the below commands into the Command Prompt and hitting RETURN after each.

    ```
    SABnzbd-console.exe -f "%localappdata%\sabnzbd\sabnzbd.ini" install
    sc config SABnzbd start= auto
    net start SABnzbd
    ```

    <span class="label label-warning">NOTE</span> The first command uses the `%localappdata%` system variable to point to the LOCAL folder within your user's APPDATA folder, which should work on all versions of Windows. If for some reason that does not work on your system and you get a `sabnzbd.ini file not found` type error, you will need to replace the path portion of the above command to explicitly point to your `sabnzbd.ini` file within your `C:\Users\USERNAME\AppData\Local\sabnzbd` folder.

    <span class="label label-danger">NOTE</span> If you used PowerShell instead of Command Prompt you will need to use `$env:LOCALAPPDATA` instead of `%localappdata%`!

5. You can check SABnzbd is running as a service with:

    ```
    net start | find /i "sabnzbd"
    ```

That's it! SABnzbd is now installed and running as an "always on" service.
If all you need is to run SABnzbd as a service using the same settings used in the SABnzbd web interface, and you are not using network shares for your downloaded files, your work here is done.

However, if you want to customize the way that the service runs, or if you need to have SABnzbd access shared drives across the network, please read through the following sections for further information.

<span class="label label-warning">NOTE</span> SABnzbd will not present an icon in the Notification (lower right) area of the Windows screen when run as a service. This will not affect normal operation of the software.

<span class="label label-warning">NOTE</span> The Windows firewall will not warn you if it blocks SABnzbd as it does when blocking SABnzbd when running "normally", so you may need to add it to the firewall exception list using the normal procedures for your version of Windows if you run into an access problem. However, if you have already run SABnzbd successfully before installing it as a service, using the same port number, it is likely the exception will already be in effect.

<span class="label label-warning">NOTE</span> Before upgrading SABnzbd, it is recommended you stop the service to ensure there are no problems overwriting busy files. See the section below for details on stopping the service via the command line or through the Windows Service Manager.

## Specifying additional options

By default, installing SABnzbd as a service (as detailed in step 4 of the above installation instructions) will cause it to run using the same settings used by the SABnzbd web interface on your system.

You can, however, override many of these settings with [command line parameters](/wiki/advanced/command-line-parameters). Simply add the pertinent command to the line that installs the SABnzbd service. Be aware that not all of the available command line options are appropriate when SABnzbd is running as a service. For instance, parameters like `-b` (start browser) will be ignored even if specified.

<span class="label label-warning">NOTE</span> Any parameter you set in the command line will override the equivalent parameter in the web interface, and any changes to the interface settings will be ignored by the service for that parameter. For parameters not set through the command line, the service will use whatever was set in the GUI at the time the service is launched or updated.

For example, the following will install the SABnzbd service with the `-s host:port` command to reflect a different server address:

```
SABnzbd-console.exe -f "%localappdata%\sabnzbd\sabnzbd.ini" -s 127.0.0.1:8081 install
```

In this example, the SABnzbd service will continue to use the specified port (8081) even if you subsequently specify a different port within the web interface. You would need to reinstall the service by re-entering the above command without the `-s 127.0.0.1:8081` argument to have the SABnzbd service once again go back to using the value set in the web interface.

### Updating the service settings

Each time the SABnzbd service starts, it reads the SABnzbd ini file for configuration options. If you change settings within the SABnzbd web interface you can force the service to reread the ini file by typing the following command in an elevated Command Prompt after changing directories to the SABnzbd folder. Of course, you can also simply reboot the computer to cause the service to restart and reread the ini file again.

```
SABnzbd-console.exe -f "%localappdata%\sabnzbd\sabnzbd.ini" update
```

## Service actions

### Removing the service

To completely remove the SABnzbd service, follow steps 1 and 2 in the Installation instructions above to open an elevated Command Prompt and access the SABnzbd folder, then type or paste the following command into it and hit RETURN.

```
SABnzbd-console.exe remove
```

### Start the service

```
net start SABnzbd
```

### Stop the service

```
net stop SABnzbd
```

## Enabling Network Share Access

By default the SABnzbd service will be installed to run as the "Local System" account. This allows full access to local hard drives, but not to network shares.
If you are using network shares within SABnzbd to save or process your downloads, the SABnzbd service must run as a local user account with network privileges instead of "Local System". Here's how to make that change:

* Install SABnzbd as a service using the instructions in the above Installation section.
* Launch the Windows Service Manager utility. (Typically that's done by typing SERVICES into your Windows Start menu's search and choosing SERVICES from the results list.)
* In the Windows Services Manager, find the SABnzbd service (it will be displayed as "SABnzbd Binary Newsreader") in the list of services and double-click it to access its settings.
* Click the Log On tab.
* Specify a different "Log on" account. (Make sure it is one that has administrative privileges and access to network shares.)
* Apply the changes and close the Service Manager window.

<span class="label label-warning">NOTE</span> When using network shares with the SABnzbd service, you must use network (UNC) paths (`\\server\share`) instead of drive letters (`P:\`).

<span class="label label-warning">NOTE</span> Even after doing the above to enable network share access, you will still be restricted to local drives only for the admin, log and incomplete folders due to limitations in those functions. Make sure, in your SABnzbd web interface configuration, that those folders are not pointing to network shares.
