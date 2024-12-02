#!/usr/bin/env python3
# https://adventofcode.com/2024/day/1

from collections import Counter
from pathlib import Path

lines = Path("input.txt").read_text("utf8").splitlines()

# lines = """3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3""".splitlines()

sp = [l.split() for l in lines]
a, b = (sorted([int(l[n]) for l in sp]) for n in [0, 1])

diff = [abs(l[0] - l[1]) for l in zip(a, b)]
print(f"Part 1: {sum(diff)}")

c = Counter(b)
s = [n * c.get(n, 0) for n in a]
print(f"Part 2: {sum(s)}")
