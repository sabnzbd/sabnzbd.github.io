---
title: NNTP Pipelining
---

NNTP pipelining is a performance optimization that allows SABnzbd to send multiple article requests to your Usenet server without waiting for each response. 
This significantly improves download speeds, especially on connections with higher latency.

# When to Use Pipelining

Pipelining provides the most benefit in these situations:

* **Higher latency connections** (80+ ms) - The performance improvement is most dramatic when your connection to the news server has noticeable delay
* **Fast internet connections** - If you have bandwidth to spare, pipelining helps utilize it more effectively

<span class="label label-primary">NOTE</span> Pipelining is **enabled by default** with a conservative value of 2 requests per connection.

# Configuration

## Adjusting Pipelining

Pipelining is enabled by default with a value of 2. To adjust it:

1. Go to **[Config → Special](/wiki/configuration/{{site.wiki_version}}/special)**
2. Find the `pipelining_requests` setting
3. Adjust the value to control how many article requests are sent to each connection without waiting for responses

## Recommended Settings

The default value of **2** is conservative and works well for most users. If you want to experiment:

* **Default (2)**: Good starting point for most connections
* **Higher latency connections (100+ ms)**: Try values of 5-10
* **Very high latency (200+ ms)**: Try values up to 15-20
* **Low latency connections (< 50 ms)**: The default of 2 is often sufficient
* **Server Connections**: Use 8-12 connections per server
* **SSL/TLS**: Pipelining works with both SSL and non-SSL connections

<span class="label label-warning">NOTE</span> The pipeline depth should be tuned carefully. Values that are too high can reduce performance due to increased overhead and the amount of responses buffered. Increase gradually while monitoring your speeds.

## Troubleshooting

**Speeds didn't improve:**
* The default value of 2 is conservative - try increasing to 5-10 for high-latency connections
* Verify your server supports pipelining (check with your provider)
* Check if your connection is already saturated
* Low latency connections (< 20ms) may show minimal improvement even with higher values

**Getting connection errors:**
* Reduce `pipelining_requests` to 1 (effectively disabling pipelining)
* Some servers may have limits on concurrent requests
* Set to 0 to completely disable pipelining if issues persist

**Unstable downloads:**
* Reduce the `pipelining_requests` value incrementally
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


