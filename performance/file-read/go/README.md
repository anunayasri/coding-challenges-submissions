# Build a Frequency Table of Chars in a Text File in Go

Run the benchmark only once and store the cpu profile in an output file.

```sh
go test -bench . -cpuprofile 250mb-unicode.prof -benchtime 1x
```

Analyse profiled cpu data 

```sh
go tool pprof -http 127.0.0.1:8080 250mb-unicode.prof
```

Total execution time for 250 MB file : `3.86 s`

`5%` time is spend in reading the data from the file.
`92%` time is spend in iterating through the contents and building the frequency table.
`72%` time is spend in `runtime.mapassign_fast32()` which I think is updating 
the map ie freq table.
