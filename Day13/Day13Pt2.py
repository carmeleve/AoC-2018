import operator
import numpy as np
import collections

np.set_printoptions(threshold=np.nan)

def get_cart_direction(symbol):
    if symbol == "^":
        return (0,-1)
    elif symbol == ">":
        return (1,0)
    elif symbol == "<":
        return (-1,0)
    else:
        return (0,1)
    
def get_cart_symbol(direction):
    if direction == (0,-1):
        return "^"
    elif direction == (1,0):
        return ">"
    elif direction == (-1,0):
        return "<"
    else:
        return "v"
    
def plus_condition(x, y , tracks):
    if x==0 or y==0 or x== tracks.shape[0] - 1 or y == tracks.shape[1] -1:
        return False
    elif tracks[(x+1,y)] == "-" and (tracks[(x,y+1)] == "|" or tracks[(x,y+1)] == "/" or tracks[(x,y+1)] == "\\" or tracks[(x,y+1)] == "+"):
        return True
    elif tracks[(x-1,y)] == "-" and (tracks[(x,y+1)] == "|" or tracks[(x,y+1)] == "/" or tracks[(x,y+1)] == "\\" or tracks[(x,y+1)] == "+"):
        return True
    elif tracks[(x,y+1)] == "|" and (tracks[(x+1,y)] == "-" or tracks[(x+1,y)] == "/" or tracks[(x+1,y)] == "\\" or tracks[(x+1,y)] == "+"):
        return True
    elif tracks[(x-1,y)] == "|" and (tracks[(x+1,y)] == "-" or tracks[(x+1,y)] == "/" or tracks[(x+1,y)] == "\\" or tracks[(x+1,y)] == "+"):
        return True
    else:
        return False
    

def vertical_condition(x,y,tracks):
    if x==0 or x == tracks.shape[0] - 1:
        return True
    elif y==0  or y == tracks.shape[1] -1:
        return False
    elif tracks[(x,y+1)] == tracks[(x,y-1)] == "|":
        return True
    elif tracks[(x,y-1)] == "|" and (tracks[(x,y+1)] == "/" or tracks[(x,y+1)] == "\\" ):
        return True
    elif tracks[(x,y+1)] == "|" and (tracks[(x,y-1)] == "/"or tracks[(x,y-1)] == "\\" ):
        return True
    elif tracks[(x,y-1)] == "+" and (tracks[(x,y+1)] == "/" or tracks[(x,y+1)] == "\\" or tracks[(x,y+1)] == "|" or tracks[(x,y+1)] == "+"):
        return True
    elif tracks[(x,y+1)] == "+" and (tracks[(x,y-1)] == "/" or tracks[(x,y-1)] == "\\" or tracks[(x,y-1)] == "|" or tracks[(x,y-1)] == "+"):
        return True
    else:
        return False
    
def horizontal_condition(x,y,tracks):
    if y==0  or y == tracks.shape[1] -1:
        return True
    elif x==0 or x == tracks.shape[0] - 1:
        return False
    elif tracks[(x+1,y)] == tracks[(x-1,y)] == "-":
        return True
    elif tracks[(x-1,y)] == "-" and (tracks[(x+1,y)] == "/" or tracks[(x+1,y)] == "\\" ):
        return True
    elif tracks[(x+1,y)] == "-" and (tracks[(x-1,y)] == "/" or tracks[(x-1,y)] == "\\"):
        return True
    elif tracks[(x-1,y)] == "+" and (tracks[(x+1,y)] == "/" or tracks[(x+1,y)] == "\\" or tracks[(x+1,y)] == "-" or tracks[(x+1,y)] == "+"):
        return True
    elif tracks[(x+1,y)] == "+" and (tracks[(x-1,y)] == "/" or tracks[(x-1,y)] == "\\" or tracks[(x-1,y)] == "-" or tracks[(x-1,y)] == "+"):
        return True
    else:
        return False
    
def forward_slash_condition(x,y,tracks):
    if tracks[(x+1,y)] == "-" and (tracks[(x,y+1)] == "|" or tracks[(x,y+1)] == "+"or tracks[(x,y+1)] == "\\"):
        return True
    elif tracks[(x-1,y)] == "-"and (tracks[(x,y-1)] == "|" or tracks[(x,y-1)] == "+"or tracks[(x,y-1)] == "\\"):
        return True
    elif tracks[(x,y+1)] == "|" and (tracks[(x+1,y)] == "-" or tracks[(x+1,y)] == "+"or tracks[(x+1,y)] == "\\"):
        return True
    elif tracks[(x,y-1)] == "|" and (tracks[(x-1,y)] == "-" or tracks[(x-1,y)] == "+"or tracks[(x-1,y)] == "\\"):
        return True
    else:
        return False

def back_slash_condition(x,y,tracks):
    if tracks[(x+1,y)] == "-" and (tracks[(x,y-1)] == "|" or tracks[(x,y-1)] == "+"or tracks[(x,y-1)] == "\\"):
        return True
    elif tracks[(x-1,y)] == "-"and (tracks[(x,y+1)] == "|" or tracks[(x,y+1)] == "+"or tracks[(x,y+1)] == "\\"):
        return True
    elif tracks[(x,y-1)] == "|" and (tracks[(x+1,y)] == "-" or tracks[(x+1,y)] == "+"or tracks[(x+1,y)] == "\\"):
        return True
    elif tracks[(x,y+1)] == "|" and (tracks[(x-1,y)] == "-" or tracks[(x-1,y)] == "+"or tracks[(x-1,y)] == "\\"):
        return True
    else:
        return False
    
    
def get_new_direction(direction, track):
    if track == "/":
        return (-direction[1], -direction[0])
    elif track == "\\":
        return(direction[1], direction[0])
        
def get_track_type(position, tracks):
    x= position[0]
    y= position[1]
    if plus_condition(x,y,tracks):
        return "+"
    elif vertical_condition(x,y,tracks):
        return "|"
    elif horizontal_condition(x,y,tracks):
        return "-"
    elif back_slash_condition(x,y,tracks):
        return "\\"
    elif forward_slash_condition(x,y,tracks):
        return "/"
        
def turn_left(direction):
    if direction == (1,0):
        return (0,-1)
    elif direction == (0,1):
        return (1,0)
    elif direction == (-1,0):
        return (0,1)
    else:
        return (-1, 0)

def turn_right(direction):
    if direction == (1,0):
        return (0,1)
    elif direction == (0,1):
        return (-1,0)
    elif direction == (-1,0):
        return (0,-1)
    else:
        return (1, 0)
         

file_path = "input.txt"

py_tracks = []

with open(file_path) as file:
    for line in file:
        track_line = list(line.replace("\n",""))
        py_tracks.append(track_line)

tracks = np.array(py_tracks)
tracks = np.swapaxes(tracks, 0 ,1)

tracks_without_carts = np.array(py_tracks)
tracks_without_carts = np.swapaxes(tracks_without_carts, 0 ,1)

cart_symbols = ["<",">","^","v"]
direction_changes = ["\\","/"]


cart_directions = {}
cart_counters = {}

for y_iter in range(tracks.shape[1]):
    for x_iter in range(tracks.shape[0]):
        symbol_at_position = tracks[x_iter, y_iter]
        if symbol_at_position in cart_symbols:
            direction = get_cart_direction(symbol_at_position)
            cart_directions[(x_iter,y_iter)] = direction
            cart_counters[(x_iter,y_iter)]  = 0
   
for cart in cart_directions:
    tracks_without_carts[cart[0],cart[1]] = get_track_type(cart, tracks)
    
crash_coord = (-1,-1)

print(np.swapaxes(tracks, 0 ,1))
ticks = 0
while True:
    if ticks % 100 == 0:
        print(len(cart_directions))
    new_carts = {}
    destroyed_carts = {}
    for cart in cart_directions:
        direction = cart_directions[cart]
        new_position = tuple(map(operator.add, cart, cart_directions[cart]))

        track = tracks[new_position[0], new_position[1]]
        if track in cart_symbols:
            tracks[new_position] = tracks_without_carts[new_position]
            tracks[cart] = tracks_without_carts[cart]
            if new_position in cart_directions:
                destroyed_carts[new_position] = cart_directions[new_position]
            if new_position in new_carts:
                del new_carts[new_position]
        elif not cart in destroyed_carts:
            if track in direction_changes:
                direction = get_new_direction(cart_directions[cart], track)
            elif track == "+":
                if cart_counters[cart] == 0:
                    direction = turn_left(cart_directions[cart])
                    cart_counters[cart] += 1
                elif cart_counters[cart] == 1:
                     cart_counters[cart] += 1
                else:
                    direction = turn_right(cart_directions[cart])
                    cart_counters[cart] = 0
                    
            tracks[cart] = tracks_without_carts[cart]
            tracks[new_position] = get_cart_symbol(direction)
            new_carts[new_position] = direction
            
            cart_counters[new_position] = cart_counters[cart]
        del cart_counters[cart]
    if len(cart_directions) <= 1:
        last_cart = cart
        break    
    new_carts = collections.OrderedDict(sorted(new_carts.items() , key=lambda k: k[0][0]))
    new_carts = collections.OrderedDict(sorted(new_carts.items() , key=lambda k: k[0][1]))
    cart_directions = new_carts
    ticks += 1

print(last_cart)

tracks = np.swapaxes(tracks, 0 ,1)           
with  open("output.txt","w") as file:
    lines = list()
    for i in range (0,tracks.shape[0]):
        line = ''.join(tracks[i])
        file.write(line + "\n")
          
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            