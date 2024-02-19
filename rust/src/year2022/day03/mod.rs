use crate::common::Solution;
use std::time::SystemTime;

fn parse(contents: &str) -> Vec<&str> {
    contents.lines().collect()
}

fn part1(sacks: &Vec<&str>, priorities: &Vec<char>) -> u32 {
    sacks
        .iter()
        .map(|sack| sack.split_at(sack.len() / 2))
        .map(|(left, right)| {
            right
                .chars()
                .filter(|item| left.contains(*item))
                .map(|item| {
                    priorities
                        .iter()
                        .position(|&priority| priority == item)
                        .unwrap()
                })
                .collect::<Vec<_>>()
        })
        .map(|sack| (sack[0] + 1) as u32)
        .sum()
}

fn part2(sacks: &Vec<&str>, priorities: &Vec<char>) -> u32 {
    sacks
        .chunks(3)
        .map(|group| {
            group[0]
                .chars()
                .filter(|item| group[1].contains(*item) && group[2].contains(*item))
                .map(|item| {
                    priorities
                        .iter()
                        .position(|&priority| priority == item)
                        .unwrap()
                })
                .collect::<Vec<_>>()
        })
        .map(|group_priority| (group_priority[0] + 1) as u32)
        .sum()
}

pub fn solve() -> Solution<u32, u32> {
    let start = SystemTime::now();

    let contents = include_str!("./input.txt");
    let sacks = parse(contents);

    let priorities: Vec<char> = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        .chars()
        .collect();

    Solution {
        day: 3,
        part1: part1(&sacks, &priorities),
        part2: part2(&sacks, &priorities),
        runtime: SystemTime::now().duration_since(start).unwrap(),
    }
}
