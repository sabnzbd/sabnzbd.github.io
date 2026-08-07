---
title: Configure
---
SABnzbd comes with sensible defaults that work out of the box. Beyond those, there are plenty of options and tweaks to tailor SABnzbd to your needs. View the relevant page below for details on what each option does.

## Configuration sections

- [General](/wiki/configuration/{{ site.wiki_version }}/general): web interface access, login, language, article cache, HTTPS and update checks.
- [Folders](/wiki/configuration/{{ site.wiki_version }}/folders): where SABnzbd stores temporary downloads, completed downloads, scripts, the watched folder and more.
- [Servers](/wiki/configuration/{{ site.wiki_version }}/servers): your Usenet server(s) and their connection settings.
- [Categories](/wiki/configuration/{{ site.wiki_version }}/categories): sort jobs into categories, each with their own folder, script and priority.
- [Switches](/wiki/configuration/{{ site.wiki_version }}/switches): queue, post-processing, naming and quota behavior.
- [Sorting](/wiki/configuration/{{ site.wiki_version }}/sorting): automatically rename and organize completed downloads.
- [Notifications](/wiki/configuration/{{ site.wiki_version }}/notifications): email, desktop and mobile notification services.
- [Scheduling](/wiki/configuration/{{ site.wiki_version }}/scheduling): pause, resume, speed limits and other timed actions.
- [RSS](/wiki/configuration/{{ site.wiki_version }}/rss): read RSS feeds and filter which jobs to grab automatically.
- [Special](/wiki/configuration/{{ site.wiki_version }}/special): advanced settings that are not shown in the normal interface.
- [API Reference](/wiki/configuration/{{ site.wiki_version }}/api): control SABnzbd from other programs.

Scripts are covered separately under [Pre-queue](/wiki/configuration/{{ site.wiki_version }}/scripts/pre-queue-scripts), [Post-processing](/wiki/configuration/{{ site.wiki_version }}/scripts/post-processing-scripts) and [Notification](/wiki/configuration/{{ site.wiki_version }}/scripts/notification-scripts) scripts.

## The sabnzbd.ini file

All configuration data is stored in the `sabnzbd.ini` file. You can see which `sabnzbd.ini` file is being used on the Configuration main page.
Default locations for each operating system can be found in [Folder Setup](/wiki/advanced/directory-setup).
