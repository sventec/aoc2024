#!/usr/bin/env python3
# https://adventofcode.com/2024/day/3

import operator
import re
from itertools import starmap
from pathlib import Path

inp = Path("input.txt").read_text("utf8").replace("\n", "")

# inp = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def ex(s):
    p = [tuple(map(int, n)) for n in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", s)]
    return sum(starmap(operator.mul, p))


print(f"Part 1: {ex(inp)}")

fs = "".join(re.findall(r"do\(\)(.*?)don't\(\)", "do()" + inp + "don't()"))
print(f"Part 2: {ex(fs)}")
