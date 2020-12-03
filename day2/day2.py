
lines = []

with open("input.txt", "r") as f:
    lines = f.readlines()


halves = [l.split(":") for l in lines]
for half in halves:
    half[0] = half[0].split()
    half[1] = half[1].split()

valid1 = 0

for item in halves:
    constraints = item[0][0].split("-")
    min_n = int(constraints[0])
    max_n = int(constraints[1])

    char = item[0][1]
    pw = item[1][0]

    occs = pw.count(char)
    if (min_n <= occs) and (occs <= max_n):
        valid1 += 1

print(valid1)

valid2 = 0

for item in halves:
    constraints = item[0][0].split("-")
    min_n = int(constraints[0])
    max_n = int(constraints[1])

    char = item[0][1]
    pw = item[1][0]

    occs = pw.count(char)
    if bool(pw[min_n-1] == char) ^ bool(pw[max_n-1] == char):
        valid2 += 1

print(valid2)