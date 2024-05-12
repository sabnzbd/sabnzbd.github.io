---
title: Queue and History searching
---

# Search options

The queue search box appears only when there are more items than the Queue/History item limit (set in Status and Interface settings), or when editing multiple jobs.

All options accept multiple values, seperated by a comma.

### Category: `cat` or `category`

Examples: 
 * `show name cat:tv`

### Priority (Queue only): `priority`
Examples:  
* `title priority:High,Low`

### Status: `status`

Examples:  
* `status:Fetching`
* `status:Queued,Running`

<table class="table table-bordered table-hover">
  <thead>
    <tr>
      <th>Status</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>Propagating</code></td>
      <td>Queue</td>
      <td>Delayed download</td>
    </tr>
    <tr>
      <td><code>Paused</code></td>
      <td>Queue</td>
      <td>Job is paused</td>
    </tr>
    <tr>
      <td><code>Downloading</code></td>
      <td>Queue</td>
      <td>Normal downloading</td>
    </tr>
    <tr>
      <td><code>Checking</code></td>
      <td>Queue</td>
      <td>Pre-check is running</td>
    </tr>
    <tr>
      <td><code>Fetching</code></td>
      <td>Queue</td>
      <td>Job is downloading extra par2 files</td>
    </tr>
    <tr>
      <td><code>Grabbing</code></td>
      <td>Queue</td>
      <td>Getting an NZB from an external site</td>
    </tr>
    <tr>
      <td><code>Queued</code></td>
      <td>Queue/History</td>
      <td>Job is waiting for its turn to download or post-process</td>
    </tr>
    <tr>
      <td><code>Moving</code></td>
      <td>History</td>
      <td>Files are being moved</td>
    </tr>
    <tr>
      <td><code>QuickCheck</code></td>
      <td>History</td>
      <td>QuickCheck verification is running</td>
    </tr>
    <tr>
      <td><code>Repairing</code></td>
      <td>History</td>
      <td>Job is being repaired (by par2)</td>
    </tr>
    <tr>
      <td><code>Running</code></td>
      <td>History</td>
      <td>User's post-processing script is running</td>
    </tr>
    <tr>
      <td><code>Verifying</code></td>
      <td>History</td>
      <td>Job is being verified (by par2)</td>
    </tr>
    <tr>
      <td><code>Completed</code></td>
      <td>History</td>
      <td>Job is finished</td>
    </tr>
    <tr>
      <td><code>Failed</code></td>
      <td>History</td>
      <td>Job has failed, now in History</td>
    </tr>
  </tbody>
</table>

