import string
alphabet = string.ascii_lowercase

def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part

file_path = "input.txt"
with open(file_path) as f:
    input = f.read()

input = input.strip()
    
minLength = 100000

for letter in alphabet:
    input_copy = input
    i=0
    input_copy = input_copy.replace(letter, "")
    input_copy = input_copy.replace(letter.upper(), "")
    while True:
        if i > len(input_copy) - 2:
            break
        else:
            if input_copy[i].lower() == input_copy[i+1].lower():
                if (input_copy[i].islower() and input_copy[i+1].isupper()) or (input_copy[i].isupper() and input_copy[i+1].islower()):
                    input_copy = remove_char(input_copy, i+1)
                    input_copy = remove_char(input_copy, i)
                    if not i==0:
                        i -= 1
                else:
                    i += 1
            else:
                i += 1
    if len(input_copy) < minLength:
        minLength = len(input_copy)

print(minLength)
        