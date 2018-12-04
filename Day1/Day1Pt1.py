file_path = r"C:\Users\CarmelEve\Documents\GitHub\AoC-2018\Day1\input.txt"
file_object  = open(file_path, 'r')
freq = 0
for line in file_object:
    freq += int(line)
    
print(freq)