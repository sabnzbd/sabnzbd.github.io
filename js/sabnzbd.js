/**
 * jQuery.browser.mobile (http://detectmobilebrowser.com/)
 *
 * jQuery.browser.mobile will be true if the browser is a mobile device
 *
 **/
(function(a){(jQuery.browser=jQuery.browser||{}).mobile=/(android|bb\d+|meego|ipad|playbook|silk).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0,4))})(navigator.userAgent||navigator.vendor||window.opera);

// Determine platform
var platform = '';
var downloadTitle = 'Browse packages';
if (navigator.appVersion.indexOf('Win')!=-1)    { platform = 'win-setup'; downloadTitle = 'For Windows'}
if (navigator.appVersion.indexOf('Mac')!=-1)    { platform = 'osx'; downloadTitle = 'For macOS'}
if (navigator.appVersion.indexOf('X11')!=-1)    { platform = 'src'; downloadTitle = 'For Linux'}
if (navigator.appVersion.indexOf('Linux')!=-1)  { platform = 'src'; downloadTitle = 'For Linux'}

// Ignore for mobile
if(jQuery.browser.mobile) {
    platform = '';
    downloadTitle = 'Browse packages';
}

// Get the boxes
var stableBox = $('.download-stable .download-button');
var betaBox = $('.download-beta .download-button');

// See if maybe we saved the data from the previous page
// In try/catch in case it's not defined or blocked by security settings
try {
    parseGitHubResults(JSON.parse(sessionStorage.releases_data))
} catch(e) {
    // If not available, get the data from Github
    $.ajax('https://api.github.com/repos/sabnzbd/sabnzbd/releases', {
        timeout: 3000
    }).done(function(releases) {
        // Store the data
        sessionStorage.releases_data = JSON.stringify(releases)

        // In case GitHub returns something weird
        try {
            parseGitHubResults(releases)
        } catch(e) {
            // Place backup links
            backupLinks()
        }
    })
    .fail(function() {
        // Place backup links
        backupLinks()
    })
}

// Now parse it, going over each asset to see if it's the last stable
function parseGitHubResults(releases) {
    // Do we have a beta before a stable?
    var have_beta = false
    var have_stable = false

    // Markdown converter
    var converter = new showdown.Converter()
    converter.setOption('headerLevelStart', 2);

    // Loop over releases from GitHub
    $.each(releases, function(index, release) {
        // Is it a stable? We stop after the first stable
        if(!release.prerelease && !have_stable) {
            // Set the label and download-link for big button
            parseAssets(release.assets, platform, true)
            stableBox.children('h4').text('Download ' + release.name.replace('SABnzbd', '').trim())

            // Set link to source-code on Downloads page
            $('#download-links-stable .download-link-source').attr('href', release.html_url)

            // Set the changelog info
            $('#stable-changelog .changelog-content').html(converter.makeHtml(release.body))

            // General URL if no platform (mobile)
            if(!platform) {
                stableBox.attr('href', release.html_url)
            }

            // If there's no newer beta than the last stable, remove the beta-column
            if(!have_beta) {
                $('.download-beta').remove()
            }

            // Stop iterating over releases
            have_stable = true
        }
        // Is this the first beta?
        else if(!have_beta) {
            // Set the label and download-link for big button
            parseAssets(release.assets, platform, false)
            betaBox.children('h4').text('Download ' + release.name.replace('SABnzbd', '').trim())

            // Set link to source-code on Downloads page
            $('#download-links-beta .download-link-source').attr('href', release.html_url)

            // Set the changelog info
            $('#beta-changelog .changelog-content').html(converter.makeHtml(release.body))

            // General URL if no platform (mobile)
            if(!platform) {
                betaBox.attr('href', release.html_url)
            }

            // Don't process beta's after this
            have_beta = true
        }
        // Stop if we found both
        if(have_beta && have_stable) return
    })

    // Linux?
    if(platform == 'src') {
        $('.linux-row').show()
    }

    // Check if all assets filled
    $(".download-links li>a").each(function(index, element) {
        // Remove empty ones
        if(!$(element).attr('href')) {
            $(element).parent().hide()
        }
    })

    // Show
    $('.download-os').text(downloadTitle)
    $('.show-before-load').hide()
    $('.show-after-load').css('visibility', 'visible')
}

// Parse download-assets
function parseAssets(assets, platform, stable_release) {
    // Go over all the assets untill we find the right one
    $.each(assets, function(index, asset) {
        // The right one, put it in the box
        if(platform && asset.name.indexOf(platform) !== -1) {
            // Stable/beta
            if(stable_release) {
                stableBox.attr('href', asset.browser_download_url)
            } else {
                betaBox.attr('href', asset.browser_download_url)
            }
        }

        // Update links on download-page
        if($('.download-links').length) {
            // Stable/beta box
            var linksBox = stable_release ? $('#download-links-stable') : $('#download-links-beta')

            // Have to search which one it is
            $.each(['win32-setup', 'win-setup', 'win32-bin', 'win64-bin', 'osx', 'src'], function(index, platform_search) {
                if(asset.name.indexOf(platform_search) !== -1) {
                    linksBox.find('.download-link-' + platform_search).attr('href', asset.browser_download_url)

                    // Show message to beta-users that we want feedback
                    if(!stable_release) {
                        linksBox.find('.download-link-' + platform_search).click(function() {
                            $.featherlight('#beta-please-report');
                        })
                    }
                }
            })
        }
    })
}

// Backup for failures
function backupLinks() {
    stableBox.attr('href', 'https://github.com/sabnzbd/sabnzbd/releases/latest')
    stableBox.children('h4').text('Download SABnzbd')
    $('.download-os').text(downloadTitle)
    $('.show-before-load').hide()
    $('.show-after-load').css('visibility', 'visible')
    $('.download-beta, #download-links-stable, #download-links-beta').remove()
}

// Slideshow only for frontpage
$(document).ready(function() {
    if($("#frontpage-slideshow").length) {
        $('#frontpage-slideshow').lightSlider({
            auto:true,
            item:2,
            galleryMargin: 15,
            loop:true,
            pause: 4000,
            nextHtml: '<span class="glyphicon glyphicon-menu-right"></span>',
            prevHtml: '<span class="glyphicon glyphicon-menu-left"></span>'
        });
    }

})
