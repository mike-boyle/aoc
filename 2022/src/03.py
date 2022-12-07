from utils.api import get_input

input_str = get_input(3)

a_ord = ord("A")
lines = input_str.split("\n")
sum = 0
for line in lines:
    midpoint = int(len(line) / 2)
    first_half = set(line[:midpoint:])
    found = False
    for chr in line[midpoint::]:
        if chr in first_half:
            if ord(chr) >= ord("a"):
                sum += ord(chr) - ord("a") + 1
            else:
                sum += ord(chr) - ord("A") + 27
            found = True
            break

    if not found:
        print("something went wrong")
        exit()

sum2 = 0
for i in range(int(len(lines) / 3)):
    i = i * 3
    group = lines[i : i + 3]
    s = set(group[0])
    s = s.intersection(set(group[1]))
    s = s.intersection(set(group[2]))

    if len(s) != 1:
        print("something went wrong")
        exit()

    val = s.pop()
    if ord(val) >= ord("a"):
        sum2 += ord(val) - ord("a") + 1
    else:
        sum2 += ord(val) - ord("A") + 27


print(sum)
print(sum2)
