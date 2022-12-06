import sys
from collections import Counter

sys.path.append("..")
from input import Input

PACKET_CHAR_COUNT = 4
MESSAGE_CHAR_COUNT = 14

def get_marker_start(line, char_count):
    for i in range(len(line) - char_count + 1):
        count = Counter(line[i : i + char_count])
        if all(x == 1 for x in count.values()):
            return i + char_count
    return None

input = Input()

# PART ONE
# print([get_marker_start(line, PACKET_CHAR_COUNT) for line in input.example])
print(get_marker_start(input.puzzle[0], PACKET_CHAR_COUNT))

# PART TWO
# print([get_marker_start(line, MESSAGE_CHAR_COUNT) for line in input.example])
print(get_marker_start(input.puzzle[0], MESSAGE_CHAR_COUNT))