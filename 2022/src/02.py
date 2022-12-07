from utils.api import get_input

input_str = get_input(2)

sum_one = 0
sum_two = 0
x_offset = ord("X")
a_offset = ord("A")
for line in input_str.split("\n"):
    opp = line[0]
    me = line[2]

    sum_one += ord(me) - x_offset + 1

    opp_val = ord(opp) - a_offset
    me_val = ord(me) - x_offset

    diff = opp_val - me_val
    if diff == 0:
        sum_one += 3
    elif ((opp_val + 1) % 3) == me_val:
        sum_one += 6

    if me_val == 0:
        sum_two += ((opp_val + 2) % 3) + 1
    elif me_val == 1:
        sum_two += opp_val + 1
        sum_two += 3
    else:
        sum_two += 6
        sum_two += ((opp_val + 1) % 3) + 1


print(sum_one)
print(sum_two)
