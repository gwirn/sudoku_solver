package main

import (
	"fmt"
	"math"
)

var grid = [][]int{
	{9, 0, 0, 0, 0, 0, 0, 0, 4},
	{0, 3, 0, 0, 7, 0, 6, 9, 0},
	{0, 0, 2, 8, 0, 0, 0, 0, 0},
	{0, 5, 0, 0, 0, 0, 0, 0, 1},
	{0, 0, 0, 0, 4, 0, 0, 0, 3},
	{8, 0, 0, 7, 0, 0, 4, 5, 0},
	{3, 0, 0, 0, 0, 9, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 1, 0},
	{0, 9, 0, 0, 6, 0, 5, 7, 0},
}

func solve() {
	for y := 0; y < 9; y++ {
		for x := 0; x < 9; x++ {
			if grid[y][x] == 0 {
				for n := 1; n < 10; n++ {
					if possible(&y, &x, &n) {
						grid[y][x] = n
						solve()
						grid[y][x] = 0
					}
				}
				return
			}
		}
	}
	for _, i := range grid {
		fmt.Println(i)
	}
}

func possible(y *int, x *int, n *int) bool {
	for i := 0; i < 9; i++ {
		if grid[*y][i] == *n {
			return false
		}
	}
	for i := 0; i < 9; i++ {
		if grid[i][*x] == *n {
			return false
		}
	}
	x0 := int((math.Floor(float64(*x) / float64(3))) * 3)
	y0 := int((math.Floor(float64(*y) / float64(3))) * 3)
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if grid[y0+i][x0+j] == *n {
				return false
			}
		}
	}
	return true
}

func main() {
	solve()
}
