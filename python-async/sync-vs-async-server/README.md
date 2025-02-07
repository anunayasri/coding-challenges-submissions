# Comparing Sync vs Async Servers in Python

## Experiment

Run a sync server using the builtin `http.server` module. Sleep for `10ms` to simulate workload.

Run an async server using `aiohttp` module. Sleep for `10ms` to simulate workload.

Compare the performance of both servers using `wrk` tool.

Load: 100 connections, 4 threads, 10 seconds.

```sh
wrk -t4 -c100 -d10s <server_url>
```

## Results

Sync server

```
Running 10s test @ http://localhost:9000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    65.17ms   12.88ms  82.06ms   80.00%
    Req/Sec    21.20     13.84    70.00     72.92%
  450 requests in 10.09s, 62.84KB read
  Socket errors: connect 0, read 771, write 9, timeout 0
Requests/sec:     44.61
Transfer/sec:      6.23KB
```

Async server with downstream async calls

```
Running 10s test @ http://localhost:9001
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    12.98ms    1.11ms  17.73ms   64.04%
    Req/Sec     1.93k   167.57     2.26k    58.50%
  77184 requests in 10.04s, 13.10MB read
Requests/sec:   7685.20
Transfer/sec:      1.30MB
```

Async server with downstream sync calls

```
Running 10s test @ http://localhost:9002
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.16s   233.41ms   1.27s    90.92%
    Req/Sec    20.62      7.15    59.00     61.83%
  815 requests in 10.09s, 141.67KB read
Requests/sec:     80.80
Transfer/sec:     14.05KB
```

## Observations

1. Clients can make significantly more requests to the async server.
2. Async server with async downstream calls has significantly lower
   latency,even though the workload is same. Why ❓
3. Async server with sync downstream calls has higher latency than the sync
   server. ❗


| Metric | Sync | Async + Async | Async + Sync |
|--------|:----:|:-----:|:-----:|
| Req/sec | 44 | 7.7k | 80 |
| Avg Latency | 65ms | 13ms | 1.16s |
| Max Latency | 82ms | 17ms | 1.27s |
