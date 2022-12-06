from utils.api import get_input

input_str = get_input(1)

inventories = [
    sum(map(int, elf_inventory.split("\n")))
    for elf_inventory in input_str.split("\n\n")
]
inventories.sort()

ans_one = inventories[-1]
ans_two = sum(inventories[-3:])

print(ans_one)
print(ans_two)
