use crate::common::Solution;
use std::collections::HashSet;
use std::fmt::{Display, Formatter, Result as FmtResult};
use std::num::ParseIntError;
use std::ops::{Add, AddAssign, Sub};
use std::str::FromStr;
use std::time::SystemTime;

#[derive(Debug)]
enum Direction {
    Up,
    Left,
    Down,
    Right,
}

#[derive(Debug)]
enum ParseDirectionError {
    InvalidDirection(String),
}

impl Display for ParseDirectionError {
    fn fmt(&self, f: &mut Formatter) -> FmtResult {
        let msg = match self {
            ParseDirectionError::InvalidDirection(v) => {
                format!("Invalid direction: {}", v)
            }
        };
        write!(f, "{msg}")
    }
}

impl FromStr for Direction {
    type Err = ParseDirectionError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "U" => Ok(Direction::Up),
            "L" => Ok(Direction::Left),
            "D" => Ok(Direction::Down),
            "R" => Ok(Direction::Right),
            _ => Err(ParseDirectionError::InvalidDirection(s.to_string())),
        }
    }
}

struct Instruction {
    pub direction: Direction,
    pub steps: usize,
}

#[derive(Debug)]
enum ParseInstructionError {
    BadInput,
    BadDirection(ParseDirectionError),
    BadStep(ParseIntError),
}

impl From<ParseDirectionError> for ParseInstructionError {
    fn from(value: ParseDirectionError) -> Self {
        ParseInstructionError::BadDirection(value)
    }
}

impl From<ParseIntError> for ParseInstructionError {
    fn from(value: ParseIntError) -> Self {
        ParseInstructionError::BadStep(value)
    }
}

impl Display for ParseInstructionError {
    fn fmt(&self, f: &mut Formatter<'_>) -> FmtResult {
        let msg = match self {
            ParseInstructionError::BadDirection(v) => &format!("Invalid instruction: {}", v),
            ParseInstructionError::BadStep(v) => &format!("Invalid value for steps: {}", v),
            _ => "Could not parse Instruction",
        };
        write!(f, "{msg}")
    }
}

impl FromStr for Instruction {
    type Err = ParseInstructionError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        if let Some((d_str, s_str)) = s.split_once(" ") {
            Ok(Instruction {
                direction: d_str.parse()?,
                steps: s_str.parse()?,
            })
        } else {
            Err(ParseInstructionError::BadInput)
        }
    }
}

fn parse(contents: &str) -> Result<Vec<Instruction>, ParseInstructionError> {
    contents.lines().map(|line| line.parse()).collect()
}

#[derive(PartialEq, Eq, Hash, Clone, Copy, Debug)]
struct Pos {
    pub x: isize,
    pub y: isize,
}

impl Add for Pos {
    type Output = Pos;
    fn add(self, rhs: Self) -> Self::Output {
        Pos {
            x: self.x + rhs.x,
            y: self.y + rhs.y,
        }
    }
}

impl Sub for Pos {
    type Output = Pos;
    fn sub(self, rhs: Self) -> Self::Output {
        Pos {
            x: self.x - rhs.x,
            y: self.y - rhs.y,
        }
    }
}

impl AddAssign for Pos {
    fn add_assign(&mut self, rhs: Self) {
        self.x += rhs.x;
        self.y += rhs.y;
    }
}

fn update_knots(head_pos: &mut Pos, tail_pos: &mut Pos) {
    let diff = *head_pos - *tail_pos;
    let y_diff = diff.y;
    let x_diff = diff.x;

    let add_x = x_diff.abs().checked_div(x_diff).unwrap_or(0);
    let add_y = y_diff.abs().checked_div(y_diff).unwrap_or(0);

    if x_diff.abs() == 2 || y_diff.abs() == 2 {
        tail_pos.x += add_x;
        tail_pos.y += add_y;
    }
}

fn part1(instructions: &Vec<Instruction>) -> usize {
    let mut positions: HashSet<Pos> = HashSet::new();

    let start_pos = Pos { x: 0, y: 0 };
    positions.insert(start_pos);

    let mut head_pos = start_pos.clone();
    let mut tail_pos = start_pos.clone();

    for inst in instructions {
        for _ in 0..inst.steps {
            let mut add_x = 0;
            let mut add_y = 0;
            match inst.direction {
                Direction::Up => add_y += 1,
                Direction::Left => add_x -= 1,
                Direction::Down => add_y -= 1,
                Direction::Right => add_x += 1,
            }

            let mv = Pos { x: add_x, y: add_y };
            head_pos += mv;

            update_knots(&mut head_pos, &mut tail_pos);

            positions.insert(tail_pos);
        }
    }

    positions.iter().count()
}

fn part2(instructions: &Vec<Instruction>) -> usize {
    let mut positions: HashSet<Pos> = HashSet::new();

    let start_pos = Pos { x: 0, y: 0 };
    positions.insert(start_pos);

    let mut knots: Vec<Pos> = vec![start_pos.clone(); 10];

    for inst in instructions {
        for _ in 0..inst.steps {
            let mut add_x = 0;
            let mut add_y = 0;
            match inst.direction {
                Direction::Up => add_y += 1,
                Direction::Left => add_x -= 1,
                Direction::Down => add_y -= 1,
                Direction::Right => add_x += 1,
            }

            let mv = Pos { x: add_x, y: add_y };
            knots[0] += mv;

            for i in 1..=9 {
                let (heads, tails) = knots.split_at_mut(i);

                update_knots(&mut heads[heads.len() - 1], &mut tails[0]);
            }

            positions.insert(knots[9]);
        }
    }

    positions.iter().count()
}

pub fn solve() -> Solution<u32, u32> {
    let start = SystemTime::now();

    let contents = include_str!("./input.txt");
    let instructions = parse(contents).unwrap();

    Solution {
        day: 9,
        part1: part1(&instructions) as u32,
        part2: part2(&instructions) as u32,
        runtime: SystemTime::now().duration_since(start).unwrap(),
    }
}
