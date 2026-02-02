---
title: NNTP Pipelining
---

NNTP pipelining is a performance optimization that allows SABnzbd to send multiple article requests to your Usenet server without waiting for each response. 
This significantly improves download speeds, especially on connections with higher latency.

# When to Use Pipelining

Pipelining provides the most benefit in these situations:

* **Higher latency connections** (80+ ms) - The performance improvement is most dramatic when your connection to the news server has noticeable delay
* **Fast internet connections** - If you have bandwidth to spare, pipelining helps utilize it more effectively

<span class="label label-primary">NOTE</span> Pipelining can be configured per server with a default value of 1 request per connection (disabled).

# Configuration

## Adjusting Pipelining

Pipelining is configured per server in **[Config → Servers](/wiki/configuration/{{site.wiki_version}}/servers)** under Advanced settings. The setting is called **Articles per request**.

## Recommended Settings

The default value of **1** disables pipelining. If you want to enable it and experiment:

* **Default (1)**: Pipelining disabled - safe for all servers
* **Low latency connections (< 50 ms)**: Try 2-4
* **Higher latency connections (100+ ms)**: Try values of 4-8
* **Very high latency (200+ ms)**: Try values up to 8-15
* **Fast internet connections (>1 GBit)**: Try values of 5-10
* **Server Connections**: Use 8-12 connections per server
* **SSL/TLS**: Pipelining works with both SSL and non-SSL connections

<span class="label label-warning">NOTE</span> The pipeline depth should be tuned carefully. Values that are too high can reduce performance due to increased overhead and the amount of responses buffered. Increase gradually while monitoring your speeds.

## Troubleshooting

**Speeds didn't improve:**
* The default value of 1 disables pipelining - try increasing to 2-10 for high-latency connections
* Verify your server supports pipelining (check with your provider)
* Check if your connection is already saturated
* Low latency connections (< 20ms) may show minimal improvement even with higher values

**Getting connection errors:**
* Set `Articles per request` to 1 (disabling pipelining) - this is the default
* Some servers may have limits on concurrent requests

**Unstable downloads:**
* Reduce the `Articles per request` value incrementally
* Ensure your network connection is stable
* Check server load with your provider

# How It Works

## Traditional NNTP Download

Without pipelining, SABnzbd must wait for each article response before requesting the next:

```text
Client: BODY <article1>
[wait for network round-trip]
Server: 222 Article retrieved
[receive article data]
Client: BODY <article2>
[wait for network round-trip]
Server: 222 Article retrieved
[receive article data]
```

## Pipelined NNTP Download

With pipelining, SABnzbd sends multiple requests immediately:

```text
Client: BODY <article1>
Client: BODY <article2>
Client: BODY <article3>
...
Server: 222 Article retrieved
[receive article1 data]
Server: 222 Article retrieved
[receive article2 data]
Server: 222 Article retrieved
[receive article3 data]
```

This eliminates idle waiting time and keeps the connection continuously busy.


