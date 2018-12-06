import math

def get_total_distance(input_coord, coords):
    total_dist =0
    for coord in coords:
        x_dist = abs(input_coord[0] - coord[0])
        y_dist = abs(input_coord[1] - coord[1])
        dist = x_dist + y_dist
        total_dist += dist
    return total_dist

def within_region(input_coord, coords):
    if get_total_distance(input_coord, coords) < 10000:
        return True
    return False
    

file_path = "input.txt"
with open(file_path) as f:
    input = f.readlines()
    
coords = []
for line in input:
    x = int(line.split(',')[0].strip())
    y= int(line.split(',')[1].strip())
    coord = (x,y)
    coords.append(coord)
    
largest_x = -math.inf
largest_y = -math.inf
smallest_x = math.inf
smallest_y = math.inf

for coord in coords:
    x= coord[0]
    y = coord[1]
    if x > largest_x:
        largest_x = x
    if x < smallest_x:
        smallest_x = x
    if y > largest_y:
        largest_y = y
    if y < smallest_y:
        smallest_y = y

total_area = 0
for x_iter in range(smallest_x, largest_x):
    for y_iter in range(smallest_y, largest_y):
        coord = (x_iter, y_iter)
        if within_region(coord, coords):
            total_area += 1
        
print(total_area)
    


    



    
    