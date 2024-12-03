#!/usr/bin/env python3
# https://adventofcode.com/2024/day/2

from itertools import pairwise
from pathlib import Path

# with open("input.txt", "r", encoding="utf8") as f:
#     lines = f.read().splitlines()
lines = Path("input.txt").read_text("utf8").splitlines()

# lines = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9""".splitlines()


def check(r):
    ds = [b - a for a, b in pairwise(r)]
    return all(abs(ds[i]) < 4 and ds[i] * ds[i - 1] > 0 for i in range(len(ds)))


rs = [list(map(int, l.split())) for l in lines]

print(f"Part 1: {sum(check(r) for r in rs)}")
print(f"Part 2: {sum(any(check(r[:i] + r[i + 1:]) for i in range(len(r))) for r in rs)}")
