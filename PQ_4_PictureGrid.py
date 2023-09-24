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
while counter <= width:
        for x in range(height, 0, -1):
                print(f"x is: {x - 1} , counter is: {counter}")
                print(grid[x-1][counter])
                new_grid.append(grid[x][counter])
        counter += 1

print(new_grid)
