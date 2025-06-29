# Installation of SABnzbd docker

If there is no ready-made SABnzbd package for your operating system or NAS, this page is for you.

If you're able to use Docker on your operating system or NAS, SABnzbd based on docker can be a very nice solution 
as the docker image contains all needed software. 
And a docker image can directly land on your system, without the need for intermediate developers and release processes.

Worth knowing:
* docker itself has a learning curve
* docker is an isolated container, so you need to take care of mapping to the host:
  * port for the Web interface (normally 8080)
  * Config Folder
  * Completed Download Folder 
* performance of SABnzbd within docker can be a bit lower than straight on OS & hardware


## SABnzbd docker images

You can find SABnzbd docker images via https://hub.docker.com/search?q=sabnzbd

The most used SABnzbd docker image is linuxserver.io's image: https://hub.docker.com/r/linuxserver/sabnzbd

Note: SABnzbd docker images are not provided by the SABnzbd team, but by third parties.


## GUI / Graphical User Interface

If your OS or NAS provides a GUI to install & configure docker, 
it's probably the easiest way to find, install, configure & manage SABnzbd docker that way.

Examples of NAS solution that offer a GUI for docker: (modern) Synology devices and Unraid.

Check your NAS how to install & configure docker.

## Non-GUI: docker-compose and commandline

This is the harder way.

See the page of your SABnzbd image how to start via docker-compose or from the commandline. 
In case of linuxserver.io's image: https://docs.linuxserver.io/images/docker-sabnzbd/#usage

Pay extra attention to the mapping of port and folders: this is often the more difficult part for users.


