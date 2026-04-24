 # Zigzag download speed pattern

## Sympton

SABnzbd can show a zigzag download pattern like in the screenshot:

<img width="662" height="77" alt="image" src="https://github.com/user-attachments/assets/39a0cff7-9506-47f1-8a4b-b414c4781d07" />

## Cause

This is caused by a disk that is slower than the Internet newsserver download speed.

Easy check: after downloading and seeing the pattern, in SABnzbd's upper right corner, click on the wrench symbol ("Status and interface options"),
then click on first tab Status. Check if you see "**Download speed limited by Disk speed** (...x)". If that line is there, it's proof your disk is the bottleneck.

Then: in the same window, and there click on the Refresh Circled Arrow. After 10 seconds, in the lower part you will see the hardware performance and Internet speed.

Example of a low spec machine (slow disk for Complete folder, low pystone value):

<img width="645" height="224" alt="image" src="https://github.com/user-attachments/assets/96517d39-d5f7-45ea-bec2-df668471d3a9" />


## Explanation:
1. The first downloaded parts are cached into RAM, which is fast.
2. In the background, SABnzbd & OS is writing from RAM to disk.
3. However, if the disk cannot keep up, RAM fills up, and SABnzbd can only throttle the download speed (which you see in the graph)
4. As soon as the cached data is written to disk, there is RAM available, and SABnzbd can speed up again.
5. ... until RAM gets filled up again due to the slower disk, and the process repeats itself, causing the zigzag pattern.


## Solution

Get a faster disk until you no more get "Download speed limited by Disk speed (...x)"

And on more difficult setups like Unraid: consult Unraid documentation.