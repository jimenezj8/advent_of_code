package aoc

import (
	"fmt"
	"io/ioutil"
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

func ReadInput(filepath string) (text string) {
	file, err := os.Open(filepath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	contentBytes, err := ioutil.ReadAll(file)
	if err != nil {
		log.Fatal(err)
	}
	return string(contentBytes)
}

func DisplaySolution(solution Solution) {
	fmt.Printf("%+v", solution)
	println()
}
