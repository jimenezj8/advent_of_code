use crate::common::Solution;
use itertools::Itertools;
use std::cmp::Reverse;
use std::time::SystemTime;

fn parse(contents: &str) -> Vec<u32> {
    contents
        .split("\n\n")
        .map(|pack| pack.lines().map(|item| item.parse::<u32>().unwrap()))
        .map(|pack| pack.sum::<u32>())
        .collect()
}

pub fn part1(packs: &Vec<u32>) -> u32 {
    packs.iter().max().unwrap().clone()
}

pub fn part2(packs: &Vec<u32>) -> u32 {
    packs.iter().sorted_by_key(|&i| Reverse(i)).take(3).sum()
}

pub fn solve() -> Solution<u32, u32> {
    let start = SystemTime::now();

    let contents = include_str!("./input.txt");
    let packs = parse(contents);

    Solution {
        day: 1,
        part1: part1(&packs),
        part2: part2(&packs),
        runtime: (SystemTime::now().duration_since(start)).expect("Failed to measure runtime"),
    }
}
