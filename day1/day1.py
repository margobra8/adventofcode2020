from itertools import combinations
from functools import reduce
import operator


def find_sum(lst, pairs, k):
    return [pair for pair in combinations(lst, pairs) if sum(pair) == k]


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


stdin = []

with open("input.txt", "r") as f:
    stdin = f.readlines()

stdin = [int(x.split()[0]) for x in stdin]

pair = find_sum(stdin, 2, 2020)
trio = find_sum(stdin, 3, 2020)

res1 = prod(pair[0])
res2 = prod(trio[0])

print(pair, trio, res1, res2)
