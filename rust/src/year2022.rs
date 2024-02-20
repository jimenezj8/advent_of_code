pub mod day01;
pub mod day02;
pub mod day03;
pub mod day04;

pub fn display_all() {
    println!("{:?}", day01::solve());
    println!("{:?}", day02::solve());
    println!("{:?}", day03::solve());
    println!("{:?}", day04::solve());
}
