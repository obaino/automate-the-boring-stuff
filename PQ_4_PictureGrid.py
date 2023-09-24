#!/usr/bin/env python3

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

width = len(grid[0])
height = len(grid)

print(f"grid has width: {width} x height: {height}")
new_grid = []
counter = 0

for x in range(width):
    for y in range(height):
        print(grid[y][x], end="")
        
    print()
