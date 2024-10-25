package main

import (
	"flag"
	"fmt"
	"os"
)

func processFile(filename string) {
	fmt.Printf("Processing file %s\n", filename)

	data := readData(filename)
	getCharFreq(data)

	fmt.Printf("Completed processing of %s\n", filename)
}

func readData(filename string) string {
	bytes, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}

	return string(bytes)
}

func getCharFreq(data string) map[rune]int {
	charFreq := make(map[rune]int)
	for _, char := range data {
		charFreq[char]++
	}

	return charFreq
}

func main() {
	filename := flag.String("f", "", "Path to the input file")
	flag.Parse()

	if *filename == "" {
		panic("Provide output file using -f flag.")
	}

	processFile(*filename)
}
