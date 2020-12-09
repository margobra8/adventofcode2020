import re
from collections import defaultdict
from typing import Set, List, DefaultDict, Tuple

parents: DefaultDict[str, List[str]] = defaultdict(lambda: [])

for line in open('input.txt', "r"):
	parent = line.split(' bags contain ')[0]
	children: List[str] = re.findall(r'\d ([\w ]+) bag', line)

	for child in children:
		parents[child].append(parent)


def find_parents(bag: str) -> Set[str]:
	return set().union(parents[bag], *(find_parents(parent) for parent in parents[bag]))


print(len(find_parents('shiny gold')))

child_map: DefaultDict[str, Tuple[Tuple[int, str]]] = defaultdict(lambda: tuple())

for line in open('input.txt'):
	parent = line.split(' bags contain ')[0]
	children: List[Tuple[str, str]] = re.findall(r'(\d+) ([\w ]+) bag', line)
	child_map[parent] = tuple((int(a), b) for a, b in children)


def count_children(bag: str) -> int:
	return sum(child_count * (1 + count_children(child)) for child_count, child in child_map[bag])


print(count_children('shiny gold'))