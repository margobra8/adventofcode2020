from itertools import combinations
from functools import reduce
import operator
  
def findSum(lst, o, K): 
    return [pair for pair in combinations(lst, o) if sum(pair) == K]


def prod(iterable):
    return reduce(operator.mul, iterable, 1)

stdin = []

with open("input.txt", "r") as f:
    stdin = f.readlines()

stdin = [int(x.split()[0]) for x in stdin]

pair = findSum(stdin, 2, 2020)
trio = findSum(stdin, 3, 2020)

res1 = prod(pair[0])
res2 = prod(trio[0])

print(pair, trio, res1, res2)