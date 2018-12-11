class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Circular_linked_list:
   current = None
   def __init__(self, init_list):
       temp_list_nodes = list()
       for i in range(0, len(init_list)):
           if i == 0:
               node = Node(init_list[i])
               temp_list_nodes.append(node)
           elif i == len(init_list) - 1:
               node = Node(init_list[i])
               node.prev = temp_list_nodes[i-1]
               node.prev.next = node
               node.next = temp_list_nodes[0]
               node.next.prev = node
               temp_list_nodes.append(node)
           else:
               node = Node(init_list[i])
               node.prev = temp_list_nodes[i-1]
               node.prev.next = node    
               temp_list_nodes.append(node)
               
       self.current = temp_list_nodes[0]
       
   def insert(self, val):
       newNode = Node(val)
       newNode.next = self.current.next
       newNode.prev = self.current
       self.current.next.prev = newNode
       self.current.next = newNode
       self.current = newNode
       
   def remove(self):
       node_to_delete = self.current
       self.current =  node_to_delete.next
       self.current.prev = node_to_delete.prev
       node_to_delete.prev.next = self.current
       del node_to_delete
        
   def next(self):
        self.current = self.current.next
        return self.current
   def prev(self):
       self.current = self.current.prev
       return self.current



no_players = 441
no_marbles = 71032*100

players = {}
for player in range(1,no_players+1):
    players[player] = 0

start_array = list()
start_array.append(0)
start_array.append(1)
start_array.append(2)

marbles = Circular_linked_list(start_array)


marbles.next()
current_player = 3

for i in range(3, no_marbles):
    if i % 23 == 0:
        players[current_player] += i
        for counter in range(0,7):
            marbles.prev()           
        players[current_player] += marbles.current.val
        marbles.remove()

    else:
        marbles.next()
        marbles.insert(i)
    if current_player == no_players:
        current_player = 1
    else:
        current_player += 1
        
max_score = 0
for player in players:
    if players[player] > max_score:
        max_score = players[player]
        
print(max_score)
    