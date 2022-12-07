from utils.api import get_input

input_str = get_input(4)

sum_one = 0
sum_two = 0
for line in input_str.split("\n"):
    pair1, pair2 = [list(map(int, pair.split("-"))) for pair in line.split(",")]

    if pair1[0] <= pair2[0] and pair1[1] >= pair2[1]:
        sum_one += 1
    elif pair2[0] <= pair1[0] and pair2[1] >= pair1[1]:
        sum_one += 1

    if set(range(pair1[0], pair1[1] + 1)) & set(range(pair2[0], pair2[1] + 1)):
        sum_two += 1


print(sum_one)
print(sum_two)
