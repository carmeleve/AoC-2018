
file_path = r"C:\Users\CarmelEve\Documents\GitHub\AoC-2018\Day3\input.txt"
file_object  = open(file_path, 'r')

coord_list = {}
plans = {}

for line in file_object:
    id = line.split('@')[0].strip().replace('#','')         
    line = line.split('@')[1].strip()
    coord = line.split(':')[0].strip()
    length= line.split(':')[1].strip()
    x_start = int(coord.split(',')[0])
    y_start = int(coord.split(',')[1])
    x_length = int(length.split('x')[0])
    y_length = int(length.split('x')[1])
    plan = []
    for x_iter in range(x_start, x_start+x_length):
        for y_iter in range(y_start, y_start + y_length):
            coord = (x_iter, y_iter)
            if coord in coord_list:
                coord_list[coord] += 1
            else:
                coord_list[coord] = 1
            if not id in plans:
                plans[id] = list()
                plans[id].append(coord)
            else:
                plans[id].append(coord)
                
                
for id in plans:
    unique = True
    for coord in plans[id]:
        if not coord_list[coord] == 1:
            unique = False
    if unique:
        print(id)