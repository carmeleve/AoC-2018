scores = list()

no_recipes =702831

no_elves = 2

current_recipes = {}
current_recipes[0] = 0
current_recipes[1] = 1

input = "37"
starting_length = len(input)

for i in range(no_recipes + 6):
    new_recipe = int(input[current_recipes[0]]) + int(input[current_recipes[1]])
    new_recipe = str(new_recipe)
    input += new_recipe
    for elf in range(no_elves):
        current_recipes[elf] += int(input[current_recipes[elf]]) +1
        while current_recipes[elf] > len(input) - 1:
            current_recipes[elf] -= len(input)
print(input[no_recipes:no_recipes+10])