lines = []

with open("input.txt", "r") as f:
    lines = f.readlines()


halves = [li.split(":") for li in lines]
for half in halves:
    half[0] = half[0].split()
    half[1] = half[1].split()

valid_1 = 0

for item in halves:
    constraints = item[0][0].split("-")
    min_n = int(constraints[0])
    max_n = int(constraints[1])

    char = item[0][1]
    pw = item[1][0]

    occs = pw.count(char)
    if min_n <= occs <= max_n:
        valid_1 += 1

print(valid_1)

valid_2 = 0

for item in halves:
    constraints = item[0][0].split("-")
    min_n = int(constraints[0])
    max_n = int(constraints[1])

    char = item[0][1]
    pw = item[1][0]

    occs = pw.count(char)
    if bool(pw[min_n-1] == char) ^ bool(pw[max_n-1] == char):
        valid_2 += 1

print(valid_2)
