use crate::common::Solution;
use std::time::SystemTime;

fn parse(contents: &str) -> Vec<&str> {
    contents.lines().collect()
}

fn part1(assignments: &Vec<&str>) -> u32 {
    assignments
        .iter()
        .map(|pair| {
            let (a, b) = pair.split_once(",").unwrap();
            let ((x1, y1), (x2, y2)) = (a.split_once("-").unwrap(), b.split_once("-").unwrap());
            (
                (x1.parse::<u32>().unwrap(), y1.parse::<u32>().unwrap()),
                (x2.parse::<u32>().unwrap(), y2.parse::<u32>().unwrap()),
            )
        })
        .filter(|((start1, end1), (start2, end2))| {
            (start1 <= start2 && end1 >= end2) || (start1 >= start2 && end1 <= end2)
        })
        .count() as u32
}

fn part2(assignments: &Vec<&str>) -> u32 {
    assignments
        .iter()
        .map(|pair| {
            let (a, b) = pair.split_once(",").unwrap();
            let ((start1, end1), (start2, end2)) =
                (a.split_once("-").unwrap(), b.split_once("-").unwrap());
            (
                (start1.parse::<u32>().unwrap(), end1.parse::<u32>().unwrap()),
                (start2.parse::<u32>().unwrap(), end2.parse::<u32>().unwrap()),
            )
        })
        .filter(|((start1, end1), (start2, end2))| !(start1 > end2 || end1 < start2))
        .count() as u32
}

pub fn solve() -> Solution<u32, u32> {
    let start = SystemTime::now();

    let contents = include_str!("./input.txt");
    let assignments = parse(contents);

    Solution {
        day: 4,
        part1: part1(&assignments),
        part2: part2(&assignments),
        runtime: SystemTime::now().duration_since(start).unwrap(),
    }
}
