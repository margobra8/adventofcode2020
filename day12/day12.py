cardinales = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
direcciones = ((1, 0), (0, -1), (-1, 0), (0, 1))
ubicacion = 0, 0
direccion = 0

for line in open('input.txt'):
	accion, valor = line[0], int(line[1:])

	if accion == 'F' or accion in cardinales:
		cambio = direcciones[direccion] if accion == 'F' else cardinales[accion]
		ubicacion = ubicacion[0] + valor * cambio[0], ubicacion[1] + valor * cambio[1]
	else:
		direccion = (direccion + (valor if accion == 'R' else -valor) // 90) % len(direcciones)

print(sum(map(abs, ubicacion)))

# parte 2

waypoint = 10, 1
barco = 0, 0

for line in open('input.txt'):
	accion, valor = line[0], int(line[1:])

	if accion in cardinales:
		waypoint = waypoint[0] + valor * cardinales[accion][0], waypoint[1] + valor * cardinales[accion][1]
	elif accion == 'F':
		barco = barco[0] + valor * waypoint[0], barco[1] + valor * waypoint[1]
	else:
		x, y = waypoint
		gra_horario = {'L': 360 - valor, 'R': valor}[accion]
		waypoint = {90: (y, -x), 180: (-x, -y), 270: (-y, x)}[gra_horario]

print(sum(map(abs, barco)))