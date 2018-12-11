no_players = 441
no_marbles = 71032

players = {}
for player in range(1,no_players+1):
    players[player] = 0

marbles = [0,2,1]

current_marble = 1
current_player = 3

for i in range(3, no_marbles):
    if i % 23 == 0:
        total_length = len(marbles)
        players[current_player] += i
        to_remove = current_marble - 7
        if current_marble in range(0, 6):
            to_remove = total_length - 7 + current_marble
            
        players[current_player] += marbles[to_remove]
        del marbles[to_remove]
        
        if to_remove == total_length -1:
            current_marble = 0
        else:
            current_marble = to_remove
    else:
        if current_marble == len(marbles) - 1:
            marbles.insert(1, i)
            current_marble = 1
        else:
            marbles.insert(current_marble + 2, i)
            current_marble += 2
    if current_player == no_players:
        current_player = 1
    else:
        current_player += 1
        
max_score = 0
for player in players:
    if players[player] > max_score:
        max_score = players[player]
        
print(max_score)
    