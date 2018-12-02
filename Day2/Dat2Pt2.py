import csv

def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part

filePath = r"C:\Users\CarmelEve\Documents\GitHub\AoC-2018\Day2\input.csv"

with open(filePath) as file:
    csv_reader = csv.reader(file, delimiter=',')
    ids = {}
    for line in csv_reader:
        lineCount = 0
        for id in ids:
            differences = 0
            differenceAt = 0
            for index in range(0, len(line[0])):
                if id[index] != line[0][index]:
                    differences += 1
                    differenceAt = index
            if differences == 1:
                print(remove_char(line[0], differenceAt))
        ids[line[0]] = line[0]
        lineCount += 1
        

            