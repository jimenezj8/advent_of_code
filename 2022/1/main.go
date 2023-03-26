package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
	"time"
)

type Output struct {
	name  string
	value int
}

func main() {
	start := time.Now()
	part1 := Output{name: "Part1", value: part1()}
	part2 := Output{name: "Part2", value: part2()}
	fmt.Printf("%+v", part1)
	fmt.Printf("%+v", part2)
	fmt.Println(start.Sub(time.Now()))
}

func readInput() (text string) {
	file, err := os.Open("input.txt")
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

func part1() (result int) {
	input := readInput()
	splitData := strings.Split(input, "\n\n")
	var elfPacks = *new([]int)

	for _, elfPack := range splitData {
		items := strings.Split(elfPack, "\n")
		total := 0
		for _, item := range items {
			if item == "" {
				continue
			}
			val, err := strconv.Atoi(item)
			if err != nil {
				log.Fatal(err)
			}
			total += val
		}
		elfPacks = append(elfPacks, total)
	}
	sort.Slice(elfPacks, func(i, j int) bool {
		return elfPacks[i] > elfPacks[j]
	})

	result = elfPacks[0]

	return result
}

func part2() (result int) {
	input := readInput()
	splitData := strings.Split(input, "\n\n")
	var elfPacks = *new([]int)

	for _, elfPack := range splitData {
		items := strings.Split(elfPack, "\n")
		total := 0
		for _, item := range items {
			if item == "" {
				continue
			}
			val, err := strconv.Atoi(item)
			if err != nil {
				log.Fatal(err)
			}
			total += val
		}
		elfPacks = append(elfPacks, total)
	}
	sort.Slice(elfPacks, func(i, j int) bool {
		return elfPacks[i] > elfPacks[j]
	})

	result = 0
	for _, calories := range elfPacks[0:3] {
		result += calories
	}
	return result
}
