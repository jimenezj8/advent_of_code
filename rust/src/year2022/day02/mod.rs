use crate::common::Solution;
use std::time::SystemTime;

#[derive(PartialEq, Eq)]
enum Hand {
    Rock,
    Paper,
    Scissors,
}

impl Hand {
    fn beats(&self) -> Self {
        match *self {
            Hand::Rock => Hand::Scissors,
            Hand::Paper => Hand::Rock,
            Hand::Scissors => Hand::Paper,
        }
    }

    fn loses(&self) -> Self {
        match *self {
            Hand::Scissors => Hand::Rock,
            Hand::Paper => Hand::Scissors,
            Hand::Rock => Hand::Paper,
        }
    }

    fn from(val: u8) -> Self {
        match val {
            0 => Hand::Rock,
            1 => Hand::Paper,
            2 => Hand::Scissors,
            _ => unreachable!(),
        }
    }
}

fn parse(contents: &str) -> Vec<(u8, u8)> {
    contents
        .lines()
        .map(|round| round.as_bytes())
        .map(|round| (round.first().unwrap() - 65, round.last().unwrap() - 88))
        .collect()
}

fn part1(rounds: &Vec<(u8, u8)>) -> u32 {
    rounds
        .iter()
        .map(|round| (Hand::from(round.0), Hand::from(round.1)))
        .map(|round| {
            let mut total = if &round.1.beats() == &round.0 {
                6
            } else if round.0 == round.1 {
                3
            } else {
                0
            };

            total += round.1 as u32 + 1;

            total
        })
        .collect::<Vec<u32>>()
        .iter()
        .sum::<u32>()
}

fn part2(rounds: &Vec<(u8, u8)>) -> u32 {
    rounds
        .iter()
        .map(|round| (Hand::from(round.0), round.1))
        .map(|round| {
            let mut points = match round.1 {
                0 => round.0.beats() as u32,
                1 => round.0 as u32,
                2 => round.0.loses() as u32,
                _ => unreachable!(),
            };
            points += 1;
            points += round.1 as u32 * 3;

            points
        })
        .collect::<Vec<u32>>()
        .iter()
        .sum::<u32>()
}

pub fn solve() -> Solution<u32, u32> {
    let start = SystemTime::now();

    let contents = include_str!("./input.txt");
    let rounds = parse(contents);

    Solution {
        day: 2,
        part1: part1(&rounds),
        part2: part2(&rounds),
        runtime: SystemTime::now().duration_since(start).unwrap(),
    }
}
