def get_children(input, total_metadata):
    no_children = input[0]
    no_metadata = input[1]

    del input[0]
    del input[0]

    for i in range(no_children):
        get_children(input, total_metadata)
    for i in range(no_metadata):
        total_metadata["val"] += input[0]
        del input[0]
        

file_path = "input.txt"

with open(file_path) as file:
    input = file.read()
    
inputs = input.split(" ")
numbers = results = list(map(int, inputs))

total_metadata = {"val":0}

get_children(numbers, total_metadata)

print(total_metadata["val"])

    
    