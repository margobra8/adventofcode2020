from functools import reduce
import operator

lines = []

with open("input.txt", "r") as f:
    lines = [x.split() for x in f.readlines()]


def findTrees(chart, down, across, max_down) -> int:
    trees = 0
    i_down = 0
    i_across = 0
    max_across = len(chart[0][0])

    for i in range(0, max_down, down):
        row = chart[i][0]
        i_select = i_across % max_across
        if row[i_select] == "#":
            trees += 1
        i_across += across
        i_down += down

    return trees

#print(findTrees(lines, 1, 3, len(lines)))

inputs = [
    (1, 1),
    (1, 3),
    (1, 5),
    (1, 7),
    (2, 1)
]

outputs = []

for (d, a) in inputs:
    res = findTrees(lines, d, a, len(lines))
    print("down:", d, "across:", a, "-->", res)
    outputs.append(res)

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

print("Final result", prod(outputs))