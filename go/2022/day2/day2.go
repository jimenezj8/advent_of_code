package day2

import (
	"strings"
	"time"

	"github.com/jimenezj8/advent_of_code/common"
)

const input string = "2022/day2/input.txt"

func Run(root string) {
	start := time.Now()
	inputData := common.ReadInput(strings.Join([]string{root, input}, "/"))
	part1 := part1(inputData)
	part2 := part2(inputData)
	solution := common.Solution{
		Day:     2,
		PartOne: part1,
		PartTwo: part2,
		RunTime: time.Now().Sub(start),
	}
	common.DisplaySolution(solution)
}

func part1(input string) (score int) {
	pointsMap := map[string]int{
		"rock":     1,
		"paper":    2,
		"scissors": 3,
	}
	stratMap := map[string]string{
		"a": "rock",
		"x": "rock",
		"b": "paper",
		"y": "paper",
		"c": "scissors",
		"z": "scissors",
	}
	winMap := map[string]string{
		"scissors": "paper",
		"paper":    "rock",
		"rock":     "scissors",
	}

	score = 0
	for _, match := range strings.Split(input, "\n") {
		choices := strings.Split(match, " ")
		if len(choices) != 2 {
			continue
		}
		opp := stratMap[strings.ToLower(choices[0])]
		me := stratMap[strings.ToLower(choices[1])]

		score = score + pointsMap[me]

		if opp == me {
			score = score + 3
		} else if winMap[me] == opp {
			score = score + 6
		}
	}

	return
}

func part2(input string) (score int) {
	pointsMap := map[string]int{
		"rock":     1,
		"paper":    2,
		"scissors": 3,
	}
	stratMap := map[string]string{
		"a": "rock",
		"x": "lose",
		"b": "paper",
		"y": "tie",
		"c": "scissors",
		"z": "win",
	}
	winMap := map[string]string{
		"scissors": "paper",
		"paper":    "rock",
		"rock":     "scissors",
	}
	loseMap := make(map[string]string, len(winMap))
	for key, val := range winMap {
		loseMap[val] = key
	}

	score = 0
	for _, match := range strings.Split(input, "\n") {
		choices := strings.Split(match, " ")
		if len(choices) != 2 {
			continue
		}
		opp := stratMap[strings.ToLower(choices[0])]
		me := stratMap[strings.ToLower(choices[1])]

		switch me {
		case "tie":
			score = score + 3
			score = score + pointsMap[opp]
		case "win":
			score = score + 6
			score = score + pointsMap[loseMap[opp]]
		case "lose":
			score = score + pointsMap[winMap[opp]]
		}
	}

	return
}
