#!/usr/bin/env python3
# https://adventofcode.com/2024/day/4

from collections import defaultdict
from pathlib import Path

lines = Path("input.txt").read_text("utf8").splitlines()

# lines = """MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX""".splitlines()

# FIXME: this whole thing is still pretty ugly

rx, ry = range(len(lines[0])), range(len(lines))
grid = defaultdict(str, {(x, y): lines[y][x] for y in ry for x in rx})


def check(grid, sx, sy):
    d = (-1, 0, 1)
    return ["".join(["".join(grid[sx + i * dx, sy + i * dy]) for i in range(4)]) for dx in d for dy in d]


def allc(grid, c):
    return [(x, y) for y in ry for x in rx if grid[x, y] == c]


allx = allc(grid, "X")
print(f"Part 1: {sum(c.count('XMAS') for c in [check(grid, x, y) for x, y in allx])}")

# look for x-mas lol
alla = allc(grid, "A")
parts = [[[grid[x + dx, y + dy] for dy in (-1, 1)] for dx in (-1, 1)] for x, y in alla]

acc = sum(
    all(s in alist for s in [["M", "M"], ["S", "S"]]) or any(alist.count(s) == 2 for s in [["S", "M"], ["M", "S"]])
    for alist in parts
)
print(f"Part 2: {acc}")
