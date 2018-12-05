file_path = "input.txt"
file_object  = open(file_path, 'r')

freq = 0

for line in file_object:
    freq += int(line)
    
print(freq)