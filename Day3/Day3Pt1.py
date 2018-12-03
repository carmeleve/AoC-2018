
file_path = r"C:\Users\CarmelEve\Documents\GitHub\AoC-2018\Day3\input.txt"
file_object  = open(file_path, 'r')

coord_list = {}

for line in file_object:
    line = line.split('@')[1].strip()
    coord = line.split(':')[0].strip()
    length= line.split(':')[1].strip()
    x_start = int(coord.split(',')[0])
    y_start = int(coord.split(',')[1])
    x_length = int(length.split('x')[0])
    y_length = int(length.split('x')[1])
    
    
    for x_iter in range(x_start, x_start+x_length):
        for y_iter in range(y_start, y_start + y_length):
            coord = (x_iter, y_iter)
            if coord in coord_list:
                coord_list[coord] += 1
            else:
                coord_list[coord] = 1

no_repeat = 0

for coord in coord_list:
    if coord_list[coord] > 1:
        no_repeat += 1
        
print(no_repeat)