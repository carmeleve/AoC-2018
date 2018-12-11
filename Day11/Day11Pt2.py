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
max_size= 0
coord = (0,0)
prev_totals = {}
for coord in powers:
    prev_totals[coord] = powers[coord]
    
for size in range(2, 300):
    print(size)       
    for x_iter in range(300 - size + 1):
        for y_iter in range(300 - size + 1):
            extra_power = 0
            for x in range(size):
               extra_power += powers[(x_iter+x, y_iter+size-1)]
            for y in range(size -1):
                extra_power += powers[(x_iter+size-1,y_iter + y)]
            total_power = prev_totals[(x_iter,y_iter)] + extra_power
            prev_totals[(x_iter,y_iter)] = total_power
            if total_power > max_power:
                max_power = total_power
                coord = (x_iter, y_iter)
                max_size = size

print(coord)
print(max_size)
print(max_power)
        