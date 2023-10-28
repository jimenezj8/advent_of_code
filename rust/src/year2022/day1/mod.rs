use crate::common::Solution;
use std::time::SystemTime;

pub fn part1() -> u32 {
    let contents = include_str!("./input.txt");
    let packs = contents.split("\n\n");
    let packs = packs
        .map(|pack| {
            pack.lines()
                .map(|item| item.parse::<u32>().expect("Failed to parse calories."))
        })
        .map(|pack| pack.sum::<u32>());

    packs.max().unwrap()
}

pub fn part2() -> u32 {
    let contents = include_str!("./input.txt");
    let mut packs: Vec<u32> = contents
        .split("\n\n")
        .map(|pack| {
            pack.lines()
                .map(|item| item.parse::<u32>().expect("Failed to parse calories."))
        })
        .map(|pack| pack.sum::<u32>())
        .collect::<Vec<u32>>();
    packs.sort();
    packs.reverse();

    packs[0..3].iter().sum()
}

pub fn solve() -> Solution<u32, u32> {
    let start = SystemTime::now();

    Solution {
        part1: part1(),
        part2: part2(),
        runtime: (SystemTime::now().duration_since(start)).expect("Failed to measure runtime"),
    }
}
