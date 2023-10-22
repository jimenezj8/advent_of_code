package common

import (
	"fmt"
	"io"
	"log"
	"os"
	"time"
)

type Solution struct {
	Day     int
	PartOne int
	PartTwo int
	RunTime time.Duration
}

/*
ReadInput takes an absolute filepath and returns the file contents as a string.
*/
func ReadInput(filepath string) (text string) {
	file, err := os.Open(filepath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	contentBytes, err := io.ReadAll(file)
	if err != nil {
		log.Fatal(err)
	}
	return string(contentBytes)
}

// DisplaySolution takes a Solution and prints to the command line in a pretty format.
func DisplaySolution(solution Solution) {
	fmt.Printf("%+v", solution)
	println()
}
