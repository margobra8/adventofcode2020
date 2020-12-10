from math import comb, prod
import re

ratings = sorted(map(int, open('input.txt', 'r').readlines()))
ratings = [0] + ratings + [ratings[-1] + 3]

print(prod(map(sum, zip(
    *((b - a == 1, b - a == 3) for a, b in zip(ratings, ratings[1:]))
))))

# parte 2

ratings = sorted(map(int, open('input.txt').readlines()))
ratings = [0] + ratings + [ratings[-1] + 3]
differences = (b - a for a, b in zip(ratings, ratings[1:]))
group_lengths = map(len, re.findall(
    r'(1{2,})', ''.join(map(str, differences))))
print(prod([1 + comb(length - 1, 1) + comb(length - 1, 2)
            for length in group_lengths]))
