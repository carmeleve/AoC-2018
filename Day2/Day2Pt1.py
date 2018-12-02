import csv

num2s = 0
num3s = 0

filePath = r"C:\Users\CarmelEve\Documents\GitHub\AoC-2018\Day2\input.csv"

with open(filePath) as file:
    csv_reader = csv.reader(file, delimiter=',')
    for line in csv_reader:
        letters = {}
        two = False
        three = False
        for letter in line[0]:
            if letter in letters:
                letters[letter] += 1
            else: 
                letters[letter] = 1
        
        for letter in letters:
            if letters[letter] == 2:
                two = True
            if letters[letter] == 3:
                three = True
        if two:
            num2s += 1
        if three: 
            num3s += 1
            
            
        
    
print(num2s*num3s)
