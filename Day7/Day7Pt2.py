import collections

def get_condition_true(letter, done_jobs):
    if letter in done_jobs:
        return True
    else:
        return False

def get_next_condition(conditions, done_jobs):
    for condition in conditions:
        ready = True
        for letter in conditions[condition]:
            if not get_condition_true(letter, done_jobs):
                ready = False
        if ready:
            del conditions[condition]
            return condition
    return ""
    

file_path = "input.txt"
no_elves = 5

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
time_left = [0] * no_elves
current_job = [""] * no_elves
total_time = 0

total_jobs = len(conditions)
done_jobs = {}

while True:
    for elf in range(0,5): 
        if time_left[elf] != 0:
            time_left[elf] -= 1
        if time_left[elf] == 0:
            if current_job[elf] != "":
                done_jobs[current_job[elf]] = 1
            next_job = get_next_condition(conditions, done_jobs)
            current_job[elf] = next_job
            if next_job != "":
                time_left[elf] = ord(next_job.lower()) - 96 + 60
    if (len(done_jobs) == total_jobs):
        break
    total_time += 1
    
print(total_time)

        
