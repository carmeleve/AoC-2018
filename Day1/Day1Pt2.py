file_path= "input.txt"
file = open(file_path, 'r') 
lines = file.readlines()

freqs = {}
i = 0
freq = 0

while True :
    freq += int(lines[i])
    if freq in freqs:
        freq = freq + int(lines[i])
        break
    freqs[freq] = 0
    
    if i == len(lines)-1:
        i=0
    else:
        i += 1

print(freq)