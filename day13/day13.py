import math

with open("input.txt") as f:
    linea = f.readline()
    temprano = int(linea)
    buses = [int(bus) for bus in f.readline().split(',') if bus != 'x']

print(math.prod(min((bus - temprano % bus, bus) for bus in buses)))

# parte dos

with open('input.txt') as f:
    temprano = int(f.readline())
    buses = [(index, int(bus))
             for index, bus in enumerate(f.readline().split(',')) if bus != 'x']

hora, step = 0, 1

for offset, bus in buses:
    while (hora + offset) % bus:
        hora += step

    step *= bus  # mul con bus para aumentar hora en un factor

print(hora)
