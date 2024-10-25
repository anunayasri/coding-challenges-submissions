package main

import (
	"testing"
)

func BenchmarkCharFreq(b *testing.B) {
	filename := "../250mb-file.txt"
	processFile(filename)
}
