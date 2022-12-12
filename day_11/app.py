import operator
import sys

sys.path.append("..")
from input import Input
from math import lcm

class Monkey:

    OPS = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '//' : operator.floordiv
    }

    def __init__(self, num, operator, adjustor, test_divisible_by_n, true_to, false_to, objects):
        self.num = num
        operator = Monkey.OPS[operator]
        self.operator = operator
        self.adjustor = adjustor
        self.test_divisible_by_n = test_divisible_by_n
        self.true_to = true_to
        self.false_to = false_to
        self.objects = objects
        self.inspection_count = 0
        self.worry_reducer = lambda x: x // 3

    def distribute(self):
        self.inspect()
        distribution_list = [(self.true_to, object) if self.test(object) else (self.false_to, object) for object in self.objects]
        self.objects = []
        return distribution_list

    def inspect(self):
        self.objects = [self.worry_reducer(self.operation(object)) for object in self.objects]
        self.inspection_count += len(self.objects)

    def operation(self, x):
        adjustor = x if self.adjustor == 'old' else int(self.adjustor)
        return self.operator(x, adjustor)

    def test(self, x):
        return x % self.test_divisible_by_n == 0

def parse_monkeys(source):
    monkeys = ''.join(line for line in source if line).split('Monkey ')[1:]
    for monkey in monkeys:
        num, rem = monkey.split(':  Starting items: ')
        object_str, rem = rem.split('  Operation: new = old ')
        op_str, rem = rem.split('  Test: divisible by ')
        operator, adjustor = op_str.split(' ')
        test_divisible_by_n, rem = rem.split('    If true: throw to monkey ')
        true_to, false_to = rem.split('    If false: throw to monkey ')
        objects = [int(x) for x in object_str.split(',')]
        yield Monkey(int(num), operator, adjustor, int(test_divisible_by_n), int(true_to), int(false_to), objects)

def play_piggy_in_the_middle(monkeys, rounds):
    for _ in range(rounds):
        for monkey in monkeys:
            for item in monkey.distribute():
                monkeys[item[0]].objects.append(item[1])
    return monkeys

def calc_monkey_business(source, rounds, worry_more = False):
    monkeys = [m for m in parse_monkeys(source)]
    if worry_more:
        m_lcm = lcm(*[m.test_divisible_by_n for m in monkeys])
        worry_reducer = lambda x: x % m_lcm if x > m_lcm else x
        for monkey in monkeys:
            monkey.worry_reducer = worry_reducer 
    counts = sorted([monkey.inspection_count for monkey in play_piggy_in_the_middle(monkeys, rounds)])
    return counts[-2] * counts[-1]
    
input = Input()

# PART ONE
# print(calc_monkey_business(input.example, 20))
print(calc_monkey_business(input.puzzle, 20))

# PART TWO
# print(calc_monkey_business(input.example, 10000, True))
print(calc_monkey_business(input.puzzle, 10000, True))