import collections

def get_condition_true(letter, conditions_list):
    if letter in conditions_list:
        return False
    else:
        return True

def get_next_condition(conditions):
    for condition in conditions:
        ready = True
        for letter in conditions[condition]:
            if not get_condition_true(letter, conditions):
                ready = False
        if ready:
            break
    del conditions[condition]
    return condition
    

file_path = "input.txt"

conditions = {}

with open(file_path) as file:
    for line in file:
        line = line.replace(" can begin.", "")
        line = line.replace("\n", "")
        line = line.replace("Step ", "")
        parts = line.split(" must be finished before step ")
        if not parts[0] in conditions:
            conditions[parts[0]] = list()
        if parts[1] in conditions:
            conditions[parts[1]].append(parts[0])
        else:
            conditions[parts[1]] = list()
            conditions[parts[1]].append(parts[0])

conditions = collections.OrderedDict(sorted(conditions.items()))

instructions_list = ""
while True:
    if (len(conditions) == 0):
        break
    instructions_list += get_next_condition(conditions)

    
print(instructions_list)

        
