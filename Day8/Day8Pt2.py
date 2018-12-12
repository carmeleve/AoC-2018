def get_children(input):
    no_children = input[0]
    no_metadata = input[1]

    del input[0]
    del input[0]
    
    children = {}
    value = 0
    for i in range(no_children):
        val = get_children(input)
        children[i] = val
    if no_children == 0:
        for i in range(no_metadata):
            value += input[0]
            del input[0]
    else:
        for i in range(no_metadata):
            if (input[0]-1) in children:
                value += children[input[0]-1]
                del input[0]
            else:
                del input[0]    
            
    return value

file_path = "input.txt"

with open(file_path) as file:
    input = file.read()
    
inputs = input.split(" ")
numbers = results = list(map(int, inputs))

value = get_children(numbers)

print(value)

    
    