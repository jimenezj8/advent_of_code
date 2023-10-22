package main

import (
	"log"
	"os"

	dotenv "github.com/joho/godotenv"

	aoc2022 "github.com/jimenezj8/advent_of_code/2022"
)

var root string

func init() {
	err := dotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file; check that it exists in the module root.")
	}
	root = os.Getenv("AOC_ROOT")
}

func main() {
	aoc2022.Day1(root)
	aoc2022.Day2(root)
}
