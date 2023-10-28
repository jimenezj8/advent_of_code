use std::fmt::Display;

mod year2022;

mod common {
    use std::time::Duration;

    use super::Display;

    #[derive(Debug)]
    pub struct Solution<P1: Display, P2: Display> {
        pub part1: P1,
        pub part2: P2,
        pub runtime: Duration,
    }
}

pub fn display_year_2022() {
    year2022::display_all();
}
