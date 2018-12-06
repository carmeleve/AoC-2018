import math

def get_closest_coord(input_coord, coords):
    min_dist = math.inf
    dists = {}
    for coord in coords:
        x_dist = abs(input_coord[0] - coord[0])
        y_dist = abs(input_coord[1] - coord[1])
        dist = x_dist + y_dist
        if dist in dists:
            dists[dist].append(coord)
        else:
            dists[dist] = list()
            dists[dist].append(coord)
        if dist < min_dist:
            min_dist = dist
    if len(dists[min_dist]) > 1:
        return None
    
    return dists[min_dist][0]

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

closest_coords = {}
coords_to_remove = {}
for x_iter in range(smallest_x, largest_x):
    for y_iter in range(smallest_y, largest_y):
        current_coord = (x_iter, y_iter)
        closest_coord = get_closest_coord(current_coord, coords)
        if closest_coord != None:
            if x==smallest_x or y== smallest_y or x==largest_x or y == largest_y:
                coords_to_remove[closest_coord] = 1
            elif closest_coord in closest_coords:
                closest_coords[closest_coord].append(current_coord)
            else:
                closest_coords[closest_coord] = list()
                closest_coords[closest_coord].append(current_coord)
            
for edge_coord in coords_to_remove:
    del closest_coords[edge_coord]
    
max_area = 0
for coord in closest_coords:
    area = len(closest_coords[coord])
    
    if area > max_area:
        max_area = area
        
print(max_area)
    


    



    
    