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

print("Original grid is:")

for x in range(height):
    print(f"This is row: {x}:_ ", end="")
    for y in range(width):
        print(grid[x][y], end="")
    print()

print()
print(f"grid has width: {width} x height: {height}")
print()

def rotate_list(lst):
    # rotates lst 90 degrees

    width = len(lst[0])
    height = len(lst)
    for x in range(width):
        for y in range(height):
            print(grid[y][x], end="")
        print()

rotate_list(grid)
