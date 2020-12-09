
from typing import Union

program = tuple((command, int(number))
                for command, number in map(str.split, open('input.txt', 'r')))
acc, index = 0, 0
states = set()

while index not in states:
    states.add(index)
    command, number = program[index]
    index += number if command == 'jmp' else 1
    acc += number if command == 'acc' else 0

print(acc)


program = [(command, int(number))
           for command, number in map(str.split, open('input.txt'))]

def resolve_program() -> Union[None, int]:
    acc, index = 0, 0
    states = set()

    while index not in states and index < len(program):
        states.add(index)
        command, number = program[index]
        index += number if command == 'jmp' else 1
        acc += number if command == 'acc' else 0

    return acc if index == len(program) else None


def get_final_acc() -> int:
    swap = {'jmp': 'nop', 'acc': 'acc', 'nop': 'jmp'}

    for i, (command, number) in enumerate(program):
        program[i] = swap[command], number

        if resolve_program():
            return resolve_program()

        program[i] = command, number


print(get_final_acc())
