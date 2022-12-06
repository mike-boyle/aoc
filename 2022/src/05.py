from utils.api import get_input

input_str = get_input(5)
stack_str, moves = [lines.split("\n") for lines in input_str.split("\n\n")]

stacks = [""] * 10
for line in stack_str[:-1]:
    for i, box in enumerate(line[1::4]):
        if box != " ":
            stacks[i + 1] += box

ans_1, ans_2 = stacks[:], stacks[:]
for line in moves:
    _, n, _, src, _, dest = line.split()
    n = int(n)
    src = int(src)
    dest = int(dest)

    ans_1[src], ans_1[dest] = ans_1[src][n:], ans_1[src][:n][::-1] + ans_1[dest]
    ans_2[src], ans_2[dest] = ans_2[src][n:], ans_2[src][:n] + ans_2[dest]

print("".join(box[0] for box in ans_1 if box))
print("".join(box[0] for box in ans_2 if box))
