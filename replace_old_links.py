import os

replace_list = []
# CSS STYLES
replace_list.append(['<table class="wiki-content-table">', '<table class="table table-bordered table-hover">'])
replace_list.append(['<div id="toc-list">', '<ul class="toc-list">'])
replace_list.append(['<div style="margin-left: 2em;">', '<li>'])
replace_list.append(['<a class="vglnk" href="http://localhost:8080/sabnzbd/api" rel="nofollow"><span>http</span><span>://</span><span>localhost</span><span>:</span><span>8080</span><span>/</span><span>sabnzbd</span><span>/</span><span>api</span></a>', 'http://localhost:8080/sabnzbd/api'])
replace_list.append(['<a class="vglnk" href="http://localhost:8080/api" rel="nofollow"><span>http</span><span>://</span><span>localhost</span><span>:</span><span>8080</span><span>/</span><span>api</span></a>', 'http://localhost:8080/sabnzbd/api'])


# Footnotes
for i in range(1,6):
    i = str(i)
    replace_list.append(['<a id="footnoteref-'+i+'" href="javascript:;" class="footnoteref" onclick="WIKIDOT.page.utils.scrollToReference(\'footnote-'+i+'\')">'+i+'</a>', '<a id="footnoteref-'+i+'" href="#footnote-'+i+'">'+i+'</a>'])
    replace_list.append(['<a href="javascript:;" onclick="WIKIDOT.page.utils.scrollToReference(\'footnoteref-'+i+'\')">'+i+'</a>', i])

# Outdated links
replace_list.append(['<a href="/known-issues-pickle">More info.</a>', ''])
replace_list.append(['For more info see: <a href="/introducing-0-7-0#intro-precheck">Pre-check</a>', ''])
replace_list.append(['<a href="/introducing-0-8-0#OptimalRepair">', '<a href="/wiki/introducing-1-0#OptimalRepair">'])

# LINKS
replace_list_links = []
replace_list_links.append(['/introducing-1-0', '/wiki/introducing-1-0'])
replace_list_links.append(['/introducing-0-7', '/wiki/introducing-1-0'])
replace_list_links.append(['/faq', '/wiki/faq'])
replace_list_links.append(['/contact', '/wiki/contact'])

replace_list_links.append(['/configure-directories-v2', '/wiki/configuration/1.0/folders'])
replace_list_links.append(['/configure-directories', '/wiki/configuration/1.0/folders'])
replace_list_links.append(['/configure-folders-v2', '/wiki/configuration/1.0/folders'])
replace_list_links.append(['/configure-folders-1-0', '/wiki/configuration/1.0/folders'])
replace_list_links.append(['/configure-folders-0-7', '/wiki/configuration/0.7/folders'])

replace_list_links.append(['/configure-email', '/wiki/configuration/1.0/notifications'])
replace_list_links.append(['/configure-servers', '/wiki/configuration/1.0/servers'])
replace_list_links.append(['/configure-servers-1-0', '/wiki/configuration/1.0/servers'])
replace_list_links.append(['/configure-servers-0-7', '/wiki/configuration/0.7/servers'])
replace_list_links.append(['/configure-categories', '/wiki/configuration/1.0/categories'])
replace_list_links.append(['/configure-categories-0-8', '/wiki/configuration/1.0/categories'])
replace_list_links.append(['/configure-categories-1-0', '/wiki/configuration/1.0/categories'])
replace_list_links.append(['/configure-categories-0-7', '/wiki/configuration/0.7/categories'])
replace_list_links.append(['/configure-general-v2', '/wiki/configuration/1.0/general'])
replace_list_links.append(['/configure-general-1-0', '/wiki/configuration/1.0/general'])
replace_list_links.append(['/configure-general-0-7', '/wiki/configuration/0.7/general'])
replace_list_links.append(['/configure-scheduling-v2', '/wiki/configuration/1.0/scheduling'])
replace_list_links.append(['/configure-scheduling-1-0', '/wiki/configuration/1.0/scheduling'])
replace_list_links.append(['/configure-scheduling-0-7', '/wiki/configuration/0.7/scheduling'])
replace_list_links.append(['/configure-switches-v2', '/wiki/configuration/1.0/switches'])
replace_list_links.append(['/configure-switches-1-0', '/wiki/configuration/1.0/switches'])
replace_list_links.append(['/configure-switches-0-8', '/wiki/configuration/1.0/switches'])
replace_list_links.append(['/configure-switches-0-7', '/wiki/configuration/0.7/switches'])
replace_list_links.append(['/configure-switches', '/wiki/configuration/1.0/switches'])
replace_list_links.append(['/configure-rss-1-0', '/wiki/configuration/1.0/rss'])
replace_list_links.append(['/configure-rss-0-7', '/wiki/configuration/0.7/rss'])
replace_list_links.append(['/configure-rss', '/wiki/configuration/1.0/rss'])
replace_list_links.append(['/configure-sorting-1-0', '/wiki/configuration/1.0/sorting'])
replace_list_links.append(['/configure-sorting-0-7', '/wiki/configuration/0.7/sorting'])
replace_list_links.append(['/configure-sorting', '/wiki/configuration/1.0/sorting'])
replace_list_links.append(['/configure-special-1-0', '/wiki/configuration/1.0/special'])
replace_list_links.append(['/configure-special-0-7', '/wiki/configuration/0.7/special'])
replace_list_links.append(['/configure-special', '/wiki/configuration/1.0/special'])
replace_list_links.append(['/configure-notifications-1-0', '/wiki/configuration/1.0/notifications'])
replace_list_links.append(['/configure-notifications-0-7', '/wiki/configuration/0.7/notifications'])
replace_list_links.append(['/configure-notifications', '/wiki/configuration/1.0/notifications'])

replace_list_links.append(['/nzb-sources', '/wiki/introduction/nzb-sources'])
replace_list_links.append(['/howto', '/wiki/introduction/howto'])
replace_list_links.append(['/known-issues', '/wiki/introduction/known-issues'])
replace_list_links.append(['/usage', '/wiki/introduction/usage'])
replace_list_links.append(['/quick-setup', '/wiki/introduction/quick-setup'])

replace_list_links.append(['/install-as-a-unix-daemon', '/wiki/installation/install-as-a-unix-daemon'])
replace_list_links.append(['/install-nas', '/wiki/installation/install-nas'])
replace_list_links.append(['/install-off-modules', '/wiki/installation/install-off-modules'])
replace_list_links.append(['/install-osx-src', '/wiki/installation/install-osx-src'])
replace_list_links.append(['/install-unix', '/wiki/installation/install-unix'])
replace_list_links.append(['/install-windows', '/wiki/installation/install-windows'])
replace_list_links.append(['/install-ubuntu-repo', '/wiki/installation/install-ubuntu-repo'])
replace_list_links.append(['/install-fedora-repo', '/wiki/installation/install-fedora-repo'])
replace_list_links.append(['/install-from-source-windows', '/wiki/installation/install-from-source-windows'])
replace_list_links.append(['/windows-source', '/wiki/installation/install-from-source-windows'])



replace_list_links.append(['/api', '/wiki/advanced/api'])
replace_list_links.append(['/advanced/api', '/wiki/advanced/api']) # Oops, bad replace
replace_list_links.append(['/ipv6', '/wiki/advanced/ipv6'])
replace_list_links.append(['/advanced/ipv6', '/wiki/advanced/ipv6']) # Oops, bad replace
replace_list_links.append(['/unix-packaging', '/wiki/advanced/unix-packaging'])
replace_list_links.append(['/advanced/unix-packaging', '/wiki/advanced/unix-packaging']) # Oops, bad replace
replace_list_links.append(['/sabnzbd-as-a-windows-service', '/wiki/advanced/sabnzbd-as-a-windows-service'])
replace_list_links.append(['/advanced/sabnzbd-as-a-windows-service', '/wiki/advanced/sabnzbd-as-a-windows-service']) # Oops, bad replace
replace_list_links.append(['/directory-setup', '/wiki/advanced/directory-setup'])
replace_list_links.append(['/unix-permissions', '/wiki/advanced/unix-permissions'])
replace_list_links.append(['/user-scripts', '/wiki/advanced/user-scripts'])
replace_list_links.append(['/user-pre-queue-script', '/wiki/advanced/user-pre-queue-script'])
replace_list_links.append(['/command-line-parameters', '/wiki/advanced/command-line-parameters'])
replace_list_links.append(['/automation-support', '/wiki/advanced/automation-support'])
replace_list_links.append(['/https', '/wiki/advanced/https'])
replace_list_links.append(['/advanced/https', '/wiki/advanced/https']) # Oops, bad replace
replace_list_links.append(['/highspeed-downloading', '/wiki/advanced/highspeed-downloading'])
replace_list_links.append(['/password-protected-rars', '/wiki/advanced/password-protected-rars'])

replace_list_links.append(['/email-templates', '/wiki/extra/email-templates'])
replace_list_links.append(['/job-options', '/wiki/extra/job-options'])
#replace_list_links.append(['/cross-site-vulnerability', '/wiki/extra/cross-site-vulnerability'])
#replace_list_links.append(['/skins', '/wiki/extra/skins'])
replace_list_links.append(['/bonjour-support', '/wiki/extra/bonjour-support'])
replace_list_links.append(['/directnzb', '/wiki/extra/directnzb'])
replace_list_links.append(['/firewalls-and-virus-scanners', '/wiki/extra/firewalls-and-virus-scanners'])
replace_list_links.append(['/howto-apache', '/wiki/extra/howto-apache'])
replace_list_links.append(['/howto-portable', '/wiki/extra/howto-portable'])

replace_list_links.append(['/roadmap', '/wiki/extra/roadmap'])
replace_list_links.append(['/nzb-spec', '/wiki/extra/nzb-spec'])
replace_list_links.append(['/release-numbering', '/wiki/extra/release-numbering'])



for dirname, dirnames, filenames in os.walk('.') :
    for filename in filenames:
        # Only  .htm(l) files
        if '.html' in filename or '.htm' in filename:
            file_pointer_in = open(os.path.join(dirname, filename), "r")
            file_data = file_pointer_in.read()
            file_pointer_in.close()

            # Do replace
            for replace_item in replace_list:
                file_data = file_data.replace(replace_item[0], replace_item[1])

            # Links seperate so we really only replace links
            for replace_item in replace_list_links:
                file_data = file_data.replace('="'+replace_item[0]+'"', '="'+replace_item[1]+'"')

            # Write back
            file_pointer_out = open(os.path.join(dirname, filename), "w")
            file_pointer_out.write(file_data)
            file_pointer_out.close()

