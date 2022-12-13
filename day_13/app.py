import sys
import functools
 
sys.path.append("..")
from input import Input

def get_pairs(source):
    pairs = []
    pair = []
    for line in source:
        if line:
            pair.append(parse_signal(line))
        else:
            pairs.append(pair)
            pair = []
    pairs.append(pair)
    return pairs

def parse_signal(signal):
  answer = []
  item = ''
  while signal:
    c = signal[0] 
    signal = signal[1:]
    
    if item != '' and c in [',', ']']:
      answer.append(item)
        
    if c == ',':
      item = ''
    elif c == '[':
      item, signal = parse_signal(signal)
      if not signal:
        return item
    elif c == ']':
      return (answer, signal)
    else:  
      item = int(str(item) + c)

def is_right_order(x, y):
    if isinstance(x, int) and isinstance(y, int):
        if x < y:
            return True
        if y < x:
            return False
        return None
    
    elif isinstance(x, list) and isinstance(y, list):
        cross_comparisons = [is_right_order(a, b) for a, b in zip(x,y)]
        right_order_by_len = True if len(y) > len(x) else False if len(y) < len(x) else None
        for x in cross_comparisons:
            if x is not None:
                return x
        return right_order_by_len 

    else:
        x = [x] if isinstance(x, int) else x
        y = [y] if isinstance(y, int) else y
        return is_right_order(x, y)

def sort_packets(packets):
    return sorted(packets, key=functools.cmp_to_key(lambda x, y: -int(is_right_order(x, y))))

def get_index_sum_of_right_ordered_packets(source):
    return sum([i + 1 if is_right_order(*pair) else 0 for i, pair in enumerate(get_pairs(source))])

def get_decoder_key(signal):
    packets = [parse_signal(line) for line in signal if parse_signal(line) is not None]
    dividers = [[[2]], [[6]]]
    sorted_packets = sort_packets(packets + dividers)
    return (sorted_packets.index(dividers[0]) + 1) * (sorted_packets.index(dividers[1]) + 1)

input = Input()

# PART ONE
# print(get_index_sum_of_right_ordered_packets(input.example))
print(get_index_sum_of_right_ordered_packets(input.puzzle))

# PART TWO
# print(get_decoder_key(input.example))
print(get_decoder_key(input.puzzle))