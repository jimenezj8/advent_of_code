use crate::common::Solution;
use std::collections::HashMap;
use std::time::SystemTime;

fn parse(contents: &str) -> Vec<Vec<u32>> {
    contents
        .lines()
        .map(|line| {
            line.chars()
                .map(|char| char.to_digit(10).unwrap())
                .collect()
        })
        .collect()
}

#[derive(PartialEq, Eq, Hash)]
struct Pos {
    x: u32,
    y: u32,
}

fn part1(assignments: &Vec<Vec<u32>>) -> u32 {
    let h = assignments.len();
    let w = assignments[0].len();

    let mut visibility: HashMap<Pos, u32> = HashMap::new();

    for i in 0..h {
        for j in 0..w {
            let current_pos = Pos {
                x: j as u32,
                y: i as u32,
            };
            let current_height = assignments[i][j];

            // all trees on the edges are visible
            if i == 0 || i == h - 1 || j == 0 || j == w - 1 {
                visibility.insert(current_pos, 1);
                continue;
            };
            // check visibility from the left and right edges
            let max_left = *assignments[i][..j].iter().max().unwrap();
            let max_rgt = *assignments[i][j + 1..].iter().max().unwrap();
            if current_height > max_left || current_height > max_rgt {
                visibility.insert(current_pos, 1);
                continue;
            }

            // now from the top and bottom edges
            let col: Vec<u32> = assignments.iter().map(|row| row[j]).collect();
            let max_top = *col[..i].iter().max().unwrap();
            let max_btm = *col[i + 1..].iter().max().unwrap();
            if current_height > max_top || current_height > max_btm {
                visibility.insert(current_pos, 1);
                continue;
            }
        }
    }

    visibility.values().sum()
}

fn part2(assignments: &Vec<Vec<u32>>) -> u32 {
    let h = assignments.len();
    let w = assignments[0].len();

    let mut visibility: HashMap<Pos, u32> = HashMap::new();

    for i in 0..h {
        for j in 0..w {
            let current_pos = Pos {
                x: j as u32,
                y: i as u32,
            };
            let current_height = assignments[i][j];

            // check visibility from the left and right edges
            let mut taller_left: Vec<bool> = (*assignments)[i][..j]
                .iter()
                .map(|tree| *tree >= current_height)
                .collect();
            taller_left.reverse();
            let taller_rgt: Vec<bool> = (*assignments)[i][j + 1..]
                .iter()
                .map(|tree| *tree >= current_height)
                .collect();

            // now from the top and bottom edges
            let col: Vec<u32> = assignments.iter().map(|row| row[j]).collect();
            let mut taller_top: Vec<bool> = (*col)[..i]
                .iter()
                .map(|tree| *tree >= current_height)
                .collect();
            taller_top.reverse();
            let taller_btm: Vec<bool> = (*col)[i + 1..]
                .iter()
                .map(|tree| *tree >= current_height)
                .collect();

            let vis_l = match taller_left.iter().position(|v| *v == true) {
                Some(p) => p + 1,
                None => taller_left.len(),
            };
            let vis_r = match taller_rgt.iter().position(|v| *v == true) {
                Some(p) => p + 1,
                None => taller_rgt.len(),
            };
            let vis_t = match taller_top.iter().position(|v| *v == true) {
                Some(p) => p + 1,
                None => taller_top.len(),
            };
            let vis_b = match taller_btm.iter().position(|v| *v == true) {
                Some(p) => p + 1,
                None => taller_btm.len(),
            };

            visibility.insert(current_pos, (vis_l * vis_r * vis_t * vis_b) as u32);
        }
    }

    *visibility.values().max().unwrap()
}

pub fn solve() -> Solution<u32, u32> {
    let start = SystemTime::now();

    let contents = include_str!("./input.txt");
    let tree_heights = parse(contents);

    Solution {
        day: 8,
        part1: part1(&tree_heights),
        part2: part2(&tree_heights),
        runtime: SystemTime::now().duration_since(start).unwrap(),
    }
}
