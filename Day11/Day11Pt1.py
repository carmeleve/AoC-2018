serial_no = 9110
powers = {}

for x_iter in range(300):
    for y_iter in range(300):
        rack_id = x_iter + 10
        power_level = rack_id * y_iter
        power_level += serial_no
        power_level *= rack_id
        power_level = str(power_level)
        power_level = int(power_level[len(power_level)-3])
        power_level -= 5
        powers[(x_iter, y_iter)] = power_level

max_power = 0
size = 3
for x_iter in range(300 - size +1):
    for y_iter in range(300 - size +1):
        total_power = 0
        size = 3
        for x in range(size):
            for y in range(size):
                total_power += powers[(x_iter+x, y_iter+y)]
        if total_power > max_power:
            max_power = total_power
            coord = (x_iter, y_iter)

print(coord)
        