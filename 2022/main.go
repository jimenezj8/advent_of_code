package main

import (
	"log"
	"os"

	dotenv "github.com/joho/godotenv"

	day1 "jimenezj8/aoc/2022/1"
	day2 "jimenezj8/aoc/2022/2"
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
	day1.Run(root)
	day2.Run(root)
}
