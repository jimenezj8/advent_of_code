package day1

import (
	"log"
	"sort"
	"strconv"
	"strings"
	"time"

	"github.com/jimenezj8/advent_of_code/common"
)

const input string = "2022/day1/input.txt"

func Run(root string) {
	start := time.Now()
	inputData := common.ReadInput(strings.Join([]string{root, input}, "/"))
	part1 := part1(inputData)
	part2 := part2(inputData)
	runtime := time.Now().Sub(start)

	solution := common.Solution{Day: 1, PartOne: part1, PartTwo: part2, RunTime: runtime}
	common.DisplaySolution(solution)
}

func part1(input string) (result int) {
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

func part2(input string) (result int) {
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
