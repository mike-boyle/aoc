from utils.api import get_input
from collections import deque

input_str = get_input(6)

buffer_one = deque(input_str[:4])
buffer_two = deque(input_str[:14])

answer_one = answer_two = None

for i, s in enumerate(input_str[4:]):
    i = i + 4
    if answer_one is None and len(set(buffer_one)) == 4:
        answer_one = i
    
    if len(set(buffer_two)) == 14:
        answer_two = i
        print(answer_one)
        print(answer_two)
        exit()
    
    buffer_one.popleft()
    buffer_one.append(s)

    if len(buffer_two) == 14:
        buffer_two.popleft()
        buffer_two.append(s)

print("no answer!")