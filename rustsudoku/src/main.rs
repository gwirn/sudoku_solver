fn solve(grid: &mut [[usize; 9]; 9]) {
    for y in 0..9 {
        for x in 0..9 {
            if grid[y][x] == 0 {
                for n in 1..10 {
                    if possible(grid, &y, &x, &n) {
                        grid[y][x] = n;
                        solve(grid);
                        grid[y][x] = 0;
                    }
                }
                return;
            }
        }
    }
    println!("{:?}", &grid);
}

fn possible(grid: &[[usize; 9]; 9], y: &usize, x: &usize, n: &usize) -> bool {
    for i in 0..9 {
        if &grid[*y][i] == n {
            return false;
        }
    }
    for i in grid.iter().take(9) {
        if i[*x] == *n {
            return false;
        }
    }
    let xcoord: f32 = (x / 3) as f32;
    let xcoord = (&xcoord.floor() * 3.0) as usize;
    let ycoord: f32 = (y / 3) as f32;
    let ycoord = (&ycoord.floor() * 3.0) as usize;
    for i in 0..3 {
        for j in 0..3 {
            if &grid[ycoord + i][xcoord + j] == n {
                return false;
            }
        }
    }
    true
}

fn main() {
    let mut arr: [[usize; 9]; 9] = [
        [9, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 3, 0, 0, 7, 0, 6, 9, 0],
        [0, 0, 2, 8, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 4, 0, 0, 0, 3],
        [8, 0, 0, 7, 0, 0, 4, 5, 0],
        [3, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 6, 0, 5, 7, 0],
    ];
    solve(&mut arr);
}
