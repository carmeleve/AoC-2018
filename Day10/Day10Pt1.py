import matplotlib.pyplot as plt

file_path = "input.txt"

velocities = []
x_positions = []
y_positions = []

for line in open(file_path):
    pos = line.split(" velocity=<")[0].replace("position=<","").replace(">", "")
    pos_x = int(pos.split(",")[0].strip())
    pos_y = int(pos.split(",")[1].strip())
    position = (pos_x,pos_y)
    
    vel = line.split(" velocity=<")[1].replace(">", "")
    vel_x = int(vel.split(",")[0].strip())
    vel_y = int(vel.split(",")[1].strip())
    print(pos_x)
    print(pos_y)
    velocity = (vel_x, vel_y)
    
    velocities.append(velocity)
    print(velocity)
    x_positions.append(pos_x)
    y_positions.append(pos_y)

 
plt.ion()
fig, ax = plt.subplots()
sc = ax.scatter(x_positions,y_positions)

plt.draw()
# Here narrowed down through watching input and increasing pause
for j in range(100000):
    for i in range(len(x_positions)):
        x_positions[i] += velocities[i][0]
        y_positions[i] += velocities[i][1]
    if  j==10879:
        plt.cla()
        fig.canvas.draw_idle()
        reflected_x = []
        reflected_y = []
        for y in y_positions:
            reflected_y.append(-y)
        ax.scatter(x_positions, reflected_y)
        plt.pause(1)
        plt.draw()
        print(j)
    
   
    
    