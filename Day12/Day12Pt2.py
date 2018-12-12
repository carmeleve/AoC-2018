def run_states(state, starting_pots, ignored_pots):
    plant_formation = "" 
    empty_counter = 0
    
    first_found = False
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
            plant_formation += "#"
            if not first_found:
                first_found = True
                ignored_pots["val"] += pot - starting_pots
            empty_counter = 0
        else:
            if first_found:
                plant_formation += "."
                empty_counter += 1
            if empty_counter > 100:
                    break
                
    return plant_formation[0:len(plant_formation)-101]

def get_rules_from_file(file_path):
    rules = {}
    with open(file_path) as file:
        end= "." * ending_pots
        start = "." * starting_pots
        rules["initial_state"] = start + file.readline().replace("initial state: ", "").replace("\n","") + end
        
        file.readline()
        rules_input = file.readlines()

    for line in rules_input:
        rule = line.split("=>")[0].strip()
        outcome = line.split("=>")[1].strip()
        if outcome == "#":
            outcome = True
        else:
            outcome = False
        rules[rule] = outcome
        
    return rules
    

file_path = "input.txt"

starting_pots = 1000
ending_pots = 100000

generations = 50000000000
repeat_year= 0

rules = get_rules_from_file(file_path)

state = rules["initial_state"]

ignored_pots = {}
ignored_pots["val"] = 0   

previous_states = set()
constant_counter = 0
offset_change = 0
plant_formation = ""

for year in range(generations):
    old_ignored_pots = ignored_pots["val"]
    plant_formation = run_states(state, starting_pots, ignored_pots)
    if plant_formation in previous_states:
        constant_counter += 1
        if constant_counter > 100:
            offset_change = ignored_pots["val"] - old_ignored_pots
            break 
    previous_states.add(plant_formation)
    state = starting_pots*"." + plant_formation + ending_pots*"."

ignored_pots["val"] += (generations - year - 1)*offset_change

sum = 0
for pot in range(len(plant_formation)):
    if plant_formation[pot] == "#":
        sum += pot + ignored_pots["val"]        
print(sum)
        
        
    