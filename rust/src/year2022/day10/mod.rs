use std::collections::HashMap;
use std::num::ParseIntError;
use std::str::FromStr;
use std::time::SystemTime;

use crate::common::Solution;

#[derive(Debug, Clone, PartialEq, Eq)]
enum Instruction {
    NOOP,
    ADDX(i32),
}

#[derive(Debug)]
enum ParseInstructionError {
    ParseAddxValueError(ParseIntError),
    InvalidInput,
}

impl From<ParseIntError> for ParseInstructionError {
    fn from(value: ParseIntError) -> Self {
        Self::ParseAddxValueError(value)
    }
}

impl FromStr for Instruction {
    type Err = ParseInstructionError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        if let Some((_, value)) = s.split_once(" ") {
            Ok(Instruction::ADDX(value.parse()?))
        } else if s == "noop" {
            Ok(Instruction::NOOP)
        } else {
            Err(Self::Err::InvalidInput)
        }
    }
}

fn parse(contents: &str) -> Result<Vec<Instruction>, ParseInstructionError> {
    contents.lines().map(|line| line.parse()).collect()
}

fn part1(instructions: &Vec<Instruction>) -> i32 {
    let mut cycles = 0;
    let mut xreg = 1i32;

    let mut signals: HashMap<usize, i32> = HashMap::new();
    for inst in instructions {
        let (ticks, v) = match inst {
            Instruction::NOOP => (1, 0),
            Instruction::ADDX(v) => (2, *v),
        };

        let signal_no = (cycles + ticks + 20) / 40;
        if signal_no > signals.keys().count() {
            let signal = (signal_no * 40) - 20;
            let strength = xreg * signal as i32;
            println!("Signal {signal} has strength {strength} at xreg {xreg}");
            signals.insert(signal_no, strength);
        }

        if signal_no == 6 {
            break;
        }

        cycles += ticks;
        xreg += v;
    }

    println!("{signals:?}");
    signals.values().sum()
}

fn part2(instructions: &Vec<Instruction>) -> u32 {
    let mut cycles = 0;
    let mut xreg = 1i32;

    let mut buffer = String::with_capacity(240);

    for inst in instructions {
        let (ticks, v) = match inst {
            Instruction::NOOP => (1, 0),
            Instruction::ADDX(v) => (2, *v),
        };

        for tick in 0..ticks {
            let diff = xreg.abs_diff((cycles + tick) % 40 as i32);
            if diff <= 1 {
                buffer.push('#');
            } else {
                buffer.push('.');
            }
        }

        cycles += ticks;
        xreg += v;
    }

    for i in 1..=6 {
        let start = (i * 40) - 40;
        let eol = (i * 40) - 1;

        println!("{:?}", buffer.get(start..=eol).unwrap());
    }
    0
}

pub fn solve() -> Solution<u32, u32> {
    let start = SystemTime::now();

    let contents = include_str!("./input.txt");
    let instructions = parse(contents).unwrap();

    Solution {
        day: 10,
        part1: part1(&instructions) as u32,
        part2: part2(&instructions),
        runtime: SystemTime::now().duration_since(start).unwrap(),
    }
}
