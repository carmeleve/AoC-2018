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

i=0
while True:
    if i > len(input) - 2:
        break
    else:
        if input[i].lower() == input[i+1].lower():
            if (input[i].islower() and input[i+1].isupper()) or (input[i].isupper() and input[i+1].islower()):
                input = remove_char(input, i+1)
                input = remove_char(input, i)
                if not i==0:
                    i -= 1
            else:
                i += 1
        else:
            i += 1
        
print(len(input))
        
