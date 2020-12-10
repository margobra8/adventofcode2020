from collections import Counter
lines = []
answers = []

with open("input.txt", "r") as f:
    lines = f.readlines()

buffer = ""

for item in lines:
    if not item.startswith("\n"):
        buffer = buffer + " " + item.strip()
    else:
        answers.append(buffer.strip())
        buffer = ""

answers2 = [a for a in answers]
answers = [x.replace(" ", "") for x in answers]
answer_sets = []
for x in answers:
    s = set()
    for i in x:
        s.add(i)
    answer_sets.append(s)

print(answer_sets)

summ = 0

for i in answer_sets:
    summ += len(i)

# part2

print(answers2)
all_correct = []

for group in answers2:
    ind_ans = group.strip(" ")
    n_people = len(group.split(" "))
    ans_ctr = Counter(ind_ans)
    count = 0
    for key in ans_ctr:
        if ans_ctr[key] == n_people:
            count += 1
    all_correct.append(count)

print(all_correct)

print(sum(all_correct))
