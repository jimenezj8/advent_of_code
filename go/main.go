package main

import (
	"log"
	"os"

	aoc2022 "github.com/jimenezj8/advent_of_code/year2022"
)

var root string

func init() {
	var err error
	if root, err = os.Getwd(); err != nil {
		log.Fatal("Failed to get working directory")
	}
}

func main() {
	aoc2022.Run(root)
}
