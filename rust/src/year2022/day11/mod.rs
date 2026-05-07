use std::time::SystemTime;

use crate::common::Solution;

struct Monkey {
    items: Vec<u64>,
    operation: Box<dyn Fn(u64, Option<u64>) -> u64>,
    operand: Option<u64>,
    divisor: u64,
    target_true: usize,
    target_false: usize,
    pub inspections: u64,
}

impl Monkey {
    fn new(
        items: Vec<u64>,
        op_closure: impl Fn(u64, Option<u64>) -> u64 + 'static,
        operand: Option<u64>,
        divisor: u64,
        target_true: usize,
        target_false: usize,
    ) -> Self {
        Monkey {
            items,
            operation: Box::new(op_closure),
            operand,
            divisor,
            target_true,
            target_false,
            inspections: 0,
        }
    }

    fn inspect(&mut self) {
        self.items[0] = (self.operation)(self.items[0], self.operand);
        self.inspections += 1;
    }

    fn toss(&mut self) -> usize {
        if self.items[0] % self.divisor == 0 {
            self.target_true
        } else {
            self.target_false
        }
    }
}

fn parse(contents: &str) -> Vec<Monkey> {
    let mut monkeys = vec![];
    for monkey in contents.split("\n\n") {
        let mut params = monkey.lines();
        params.next(); // skip monkey number - we'll know based on the index in the vector

        let items_str = params.next().unwrap();
        let items: Vec<u64> = items_str
            .split_once(": ")
            .unwrap()
            .1 // ignore 'Starting items: ' text
            .split(", ")
            .map(|v| v.parse().unwrap())
            .collect();

        let op_str = params.next().unwrap();
        let components: Vec<_> = op_str.split_once("= ").unwrap().1.split(" ").collect(); // ignore 'Operation: new = ' text
        let operand: Option<u64> = match components[2] {
            "old" => None,
            _ => Some(components[2].parse::<u64>().unwrap()),
        };
        let operation: Box<dyn Fn(u64, Option<u64>) -> u64> = match components[1] {
            "*" => Box::new(|old, arg2| old * arg2.unwrap_or(old)),
            "/" => Box::new(|old, arg2| old / arg2.unwrap_or(old)),
            "+" => Box::new(|old, arg2| old + arg2.unwrap_or(old)),
            "-" => Box::new(|old, arg2| old - arg2.unwrap_or(old)),
            _ => panic!("Unexpected operator: {}", components[1]),
        };

        let divisor = params
            .next()
            .unwrap()
            .split_once("divisible by ")
            .unwrap()
            .1
            .parse()
            .unwrap();

        let target_true = params
            .next()
            .unwrap()
            .split_once("monkey ")
            .unwrap()
            .1
            .parse::<usize>()
            .unwrap();

        let target_false = params
            .next()
            .unwrap()
            .split_once("monkey ")
            .unwrap()
            .1
            .parse::<usize>()
            .unwrap();

        monkeys.push(Monkey::new(
            items,
            operation,
            operand,
            divisor,
            target_true,
            target_false,
        ))
    }

    monkeys
}

fn part1(monkeys: &mut Vec<Monkey>) -> u64 {
    for _ in 0..20 {
        for m in 0..monkeys.len() {
            for _ in 0..monkeys[m].items.len() {
                monkeys[m].inspect();
                monkeys[m].items[0] /= 3;
                let new_owner = monkeys[m].toss();
                let item = monkeys[m].items[0];
                monkeys[m].items = monkeys[m].items[1..].to_vec();
                monkeys[new_owner].items.push(item);
            }
        }
    }

    monkeys.sort_by(|m1, m2| m1.inspections.cmp(&m2.inspections));
    monkeys.reverse();
    monkeys[..2].iter().fold(1, |acc, m| acc * m.inspections) as u64
}

fn part2(monkeys: &mut Vec<Monkey>) -> u64 {
    let lcm = monkeys
        .iter()
        .map(|monkey| monkey.divisor)
        .fold(1, |acc, d| acc * d);
    for _ in 0..10000 {
        for m in 0..monkeys.len() {
            for _ in 0..monkeys[m].items.len() {
                monkeys[m].inspect();
                monkeys[m].items[0] %= lcm;
                let new_owner = monkeys[m].toss();
                let item = monkeys[m].items[0];
                monkeys[m].items = monkeys[m].items[1..].to_vec();
                monkeys[new_owner].items.push(item);
            }
        }
    }

    monkeys.sort_by(|m1, m2| m1.inspections.cmp(&m2.inspections));
    monkeys.reverse();
    monkeys[..2].iter().fold(1, |acc, m| acc * m.inspections) as u64
}

pub fn solve() -> Solution<u64, u64> {
    let start = SystemTime::now();

    let contents = include_str!("./input.txt");
    let mut monkeys1 = parse(contents);
    let mut monkeys2 = parse(contents);

    Solution {
        day: 11,
        part1: part1(&mut monkeys1),
        part2: part2(&mut monkeys2),
        runtime: SystemTime::now().duration_since(start).unwrap(),
    }
}
