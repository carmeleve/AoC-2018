def run_states(state):
    new_state = "" 
    for pot in range(len(state)):
        if pot == 0:
            pot_state = ".." + state[pot:pot+3]
        elif pot == 1:
            pot_state = "." + state[pot-1: pot+3]
        elif pot == len(state) -2:
            pot_state = state[pot-2:pot + 2] + "."
        elif pot == len(state) -1:
            pot_state = state[pot-2:pot + 1] + ".."
        else:
            pot_state = state[pot-2:pot+3]
        if rules[pot_state]:
            new_state += "#"
        else:
            new_state += "."
               
    return new_state

file_path = "input.txt"
extra_pots = 100
generations = 20
repeat_year= 0
offset = {}
offset["val"] = 0

with open(file_path) as file:
    end= "." * extra_pots
    offset["val"] = 15
    state = offset["val"]*"." + file.readline().replace("initial state: ", "").replace("\n","") + end
    
    file.readline()
    rules_input = file.readlines()

    
rules = {}
for line in rules_input:
    rule = line.split("=>")[0].strip()
    outcome = line.split("=>")[1].strip()
    if outcome == "#":
        outcome = True
    else:
        outcome = False
    rules[rule] = outcome
    

for year in range(generations):
    state = run_states(state)

sum = 0
for pot in range(len(state)):
    if state[pot] == "#":
        sum += pot - offset["val"]
        
print(sum)
        
        
    