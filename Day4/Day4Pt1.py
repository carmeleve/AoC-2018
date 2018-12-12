from dateutil.parser import parse
import collections
import datetime

file_path= "input.txt"
file = open(file_path, 'r') 

lines = file.readlines()
events = {}

for line in lines:
    date = line.split(']')[0].strip()
    event = line.split(']')[1].strip()
    date = parse(date.replace('[',''))
    event = event.replace('\n', '')
    events[date] = event

events = collections.OrderedDict(sorted(events.items(), ))
guard_id = 0
falls_asleep = "0"

times_asleep = {}
for event in events:
    if "Guard" in events[event]:
        parts = events[event].split(' ')
        guard_id = int(parts[1].replace('#', ''))
    if "falls asleep" == events[event]:
        falls_asleep = event
    if "wakes up" == events[event]:
        minutes = (event - falls_asleep).total_seconds()/60
        for minute in range(0, int(minutes)):
            time = falls_asleep + timedelta(minutes=minute)
            if guard_id in times_asleep:
                times_asleep[guard_id].append(time)
            else:
                times_asleep[guard_id] = list()
                times_asleep[guard_id].append(time)

max_time = 0
winning_guard = 0 
for guard in times_asleep:
    time_asleep = len(times_asleep[guard])
    if time_asleep > max_time:
        max_time = time_asleep
        winning_guard = guard
        
minutes_asleep ={}

for time in times_asleep[winning_guard]:
    minute = int(time.minute)
    if minute in minutes_asleep:
        minutes_asleep[minute] += 1
    else:
        minutes_asleep[minute] = 1
        
max_count = 0
max_minute = 0
for minute in minutes_asleep:
    if minutes_asleep[minute] > max_count:
        max_count = minutes_asleep[minute] 
        max_minute = minute
    
print(winning_guard*max_minute)

        
        
        
