import itertools
import sys
from collections import defaultdict

sys.path.append("..")
from input import Input

def find_shortest_route(a, b, route_dict):
    if a == b:
        return None

    visited = []
    queue = [[a]]
     
    while queue:
        path = queue.pop(0)
        node = path[-1]
         
        if node not in visited:
            neighbours = route_dict[node]
             
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)

                if neighbour == b:
                    return new_path
                else:
                    queue.append(new_path)
                
            visited.append(node)
    
    return None

def parse_valve(line):
    line = line.replace('Valve ', '').replace(' has flow rate=','|').replace('; tunnels lead to valves ','|').replace('; tunnel leads to valve ','|')
    name, rate, valves_str = line.split('|')
    valves = valves_str.split(', ')
    return (name, rate, valves)

def get_valve_rates(parsed_valves):
    return {valve[0]: int(valve[1]) for valve in parsed_valves}

def get_valve_tunnels(parsed_valves):
    return {valve[0]: valve[2] for valve in parsed_valves}
    

def calc_part_one(source):
    parsed_valves = [parse_valve(line) for line in source]
    valve_rates = get_valve_rates(parsed_valves)
    valve_tunnels = get_valve_tunnels(parsed_valves)

    start = 'AA'
    useful_valves = [valve for valve, rate in valve_rates.items() if rate > 0]
    
    best_paths = defaultdict(list)

    def best_path(start, valves_to_visit = []):
        key = f"{start}->{'/'.join(sorted(valves_to_visit))}"
        if best_paths.keys() and key in best_paths.keys():
            return best_paths[key]
        elif not valves_to_visit:
            best_paths[f"{start}->"] = [1, valve_rates[start], 0, [start]]           
            return best_paths[f"{start}->"]    
        else:
            poss_results = []
            for valve in valves_to_visit:
                others = [x for x in valves_to_visit if x != valve]
                step_a, rate_a, total_a, route_a = best_path(start)
                step_b, rate_b, total_b, route_b = best_path(valve, others)
                join_steps = len(find_shortest_route(start, valve, valve_tunnels)) - 1
                combined = [step_a + step_b + join_steps, rate_a + rate_b, total_a + total_b + join_steps * rate_a, [*route_a, *route_b]]
                poss_results.append(combined)            
            max_steps = max(x[0] for x in poss_results)
            best_paths[key] = max(poss_results, key=lambda x: x[2] + (max_steps - x[0]) * x[1])
            return best_paths[key]

        #     poss_results = []
        #     for valve in valves:
        #         others = [x for x in valves if x != valve]
        #         step_a, rate_a, total_a, route_a = best_path([valve])
        #         step_b, rate_b, total_b, route_b = best_path([*others])
        #         join_steps = len(find_shortest_route(valve, route_b[0], valve_tunnels)) - 1
        #         combined = [step_a + step_b + join_steps, rate_a + rate_b, total_a + total_b + join_steps * rate_a, [*route_a, *route_b]]
        #         poss_results.append(combined)
        #     max_steps = max(x[0] for x in poss_results)
        #     best_paths[key] = max(poss_results, key=lambda x: x[2] + (max_steps - x[0]) * x[1])
        #     return best_paths[key]

    print(best_path('BB', ['CC', 'DD']))
    for k, v in best_paths.items():
        print(f'{k}: {v}')
    
    # print(best_path('DD'))
    
    # # useful_valve_pairs = [x for x in itertools.permutations(useful_valves, 2)]

    # path = {(valve): (1, valve_rates[valve], 0) for valve in useful_valves}

    # for i in range(2, 3):
    #     combos = [x for x in itertools.combinations(useful_valves, i)]
    #     for combo in combos:
    #         for valve in combo:
    #             rem = [x for x in combo if x != valve]
    #             if len(rem) == 1:
    #                 steps = len(find_shortest_route(valve, rem[0], valve_tunnels))
    #                 current_rate = path[valve][1] + valve_rates[rem[0]]
    #                 total_rate = path[valve][2] + path[valve][1] * steps
    #                 path[(valve, rem[0])] = (steps + path[valve][0], current_rate, total_rate)

    # print(path)

                    # else:

                #     a_1 = steps_between[(item, rem[0])]
                #     a_2 = steps_between[(rem[0], rem[1])]
                #     b_1 = steps_between[(item, rem[1])]
                #     b_2 = steps_between[(rem[::-1][0], rem[::-1][1])]
                #     steps = max([a_1[0] + a_2[0], b_1[0] + b_2[0]]) + 1
                #     res_1 = steps * valve_rates[item] + (steps - a_1[0]) * valve_rates[rem[0]]
                #     res_2 = steps * valve_rates[item] + (steps - b_1[0]) * valve_rates[rem[0]]
                #     if res_1 > res_2:
                #         steps_between[(item, *rem)] = (steps, all_valves_total)
                #     else:
                #         steps_between[(item, *rem[::-1])] = (steps, all_valves_total)  
        
    # path = defaultdict(None)
    # for pair in useful_valve_pairs:
    #     a, b = pair
    #     steps = len(find_shortest_route(a, b, valve_tunnels)) - 1
    #     path[pair] = (steps, valve_rates[pair[0]])
    
    # print(valve_rates)
    # print(steps_between)

    # # sequences = defaultdict(list)
    # for i in range(3, 4): # len(useful_valves)):
    #     combos = [x for x in itertools.combinations(useful_valves, i)]
    #     for combo in combos:
    #         all_valves_total = sum([valve_rates[x] for x in combo])
    #         for item in combo:
    #             rem = [x for x in combo if x != item]
    #             a_1 = steps_between[(item, rem[0])]
    #             a_2 = steps_between[(rem[0], rem[1])]
    #             b_1 = steps_between[(item, rem[1])]
    #             b_2 = steps_between[(rem[::-1][0], rem[::-1][1])]
    #             steps = max([a_1[0] + a_2[0], b_1[0] + b_2[0]]) + 1
    #             res_1 = steps * valve_rates[item] + (steps - a_1[0]) * valve_rates[rem[0]]
    #             res_2 = steps * valve_rates[item] + (steps - b_1[0]) * valve_rates[rem[0]]
    #             if res_1 > res_2:
    #                 steps_between[(item, *rem)] = (steps, all_valves_total)
    #             else:
    #                 steps_between[(item, *rem[::-1])] = (steps, all_valves_total)

    # print(steps_between)
    # # for valve in useful_valves:
    #     t = find_shortest_route(start, valve, valve_tunnels) + 1

    # for valve in useful_valves:
    #     steps = len(find_shortest_route(start, valve, valve_tunnels)) - 1
    #     steps_between[(start, valve)] = steps

    # for k, v in steps_between.items():
    #     if sum([x in k for x in ['CC', 'DD', 'EE']]) == 2:
    #         print(f'{k}: {v}')

    # answers = defaultdict(None)
    # for perm in valve_switch_on_perms:
    #     full_perm = ['AA', *perm]
    #     t = 0
    #     total_pressure = 0
    #     current_pressure = 0

    #     for i in range(len(full_perm) - 1):
    #         a, b = full_perm[i], full_perm[i + 1]
    #         steps = min(connection_times[(a, b)] + 1, 30 - t)
    #         t += steps
    #         total_pressure += current_pressure * steps
    #         current_pressure += valve_rates[b]
    #         if t == 30:
    #             break

    #     total_pressure += current_pressure * (30 - t)    
    #     answers['/'.join(full_perm)] = total_pressure

    # winner = max(answers, key=answers.get)
    # return answers[winner]

input = Input()

# PART ONE
print(calc_part_one(input.example))
# print(calc_part_one(input.puzzle))

# PART TWO
# print(connection_times[('AA', 'DD')])


