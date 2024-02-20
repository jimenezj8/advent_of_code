use crate::common::Solution;
use std::time::SystemTime;

fn parse(contents: &str) -> Vec<&str> {
    contents.lines().collect()
}

fn priority_from_char(input: char) -> u32 {
    let value = input as u32;
    let lower_ref = 'a' as u32;
    let upper_ref = 'A' as u32;

    if value >= lower_ref {
        value - lower_ref + 1
    } else {
        value - upper_ref + 27
    }
}

fn part1(sacks: &Vec<&str>) -> u32 {
    sacks
        .iter()
        .map(|sack| sack.split_at(sack.len() / 2))
        .map(|sack| sack.0.chars().find(|item| sack.1.contains(*item)).unwrap())
        .map(|shared_item| priority_from_char(shared_item))
        .sum()
}

fn part2(sacks: &Vec<&str>) -> u32 {
    sacks
        .chunks(3)
        .map(|group| {
            group[0]
                .chars()
                .find(|item| group[1].contains(*item) && group[2].contains(*item))
                .unwrap()
        })
        .map(|shared_item| priority_from_char(shared_item))
        .sum()
}

pub fn solve() -> Solution<u32, u32> {
    let start = SystemTime::now();

    let contents = include_str!("./input.txt");
    let sacks = parse(contents);

    Solution {
        day: 3,
        part1: part1(&sacks),
        part2: part2(&sacks),
        runtime: SystemTime::now().duration_since(start).unwrap(),
    }
}
