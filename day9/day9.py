import itertools


numbers = list(map(int, open('input.txt', 'r').readlines()))
print(next(
    numbers[i] for i in range(25, len(numbers))
    if all(
        a + b != numbers[i]
        for a, b in itertools.combinations(numbers[i - 25:i], 2)
    )
))

i, j = 0, 2

while sum(numbers[i:j]) != 2089807806:
    if sum(numbers[i:j]) < 2089807806:
        j += 1
    elif sum(numbers[i:j]) > 2089807806:
        i += 1

print(min(numbers[i:j]) + max(numbers[i:j]))
