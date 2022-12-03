import sys

sys.path.append("..")
from input import Input

SHAPES = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS',
    'X': 'ROCK',
    'Y': 'PAPER',
    'Z': 'SCISSORS'
}

RESULTS = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

WINS = [
    ['SCISSORS', 'PAPER'],
    ['PAPER', 'ROCK'],
    ['ROCK', 'SCISSORS']
] 

def game_score(them, you):
    return 6 if [you, them] in WINS else 3 if them == you else 0

def choice_score(you):
    return {'ROCK': 1, 'PAPER': 2, 'SCISSORS': 3}[you]

def total(matches, xyz_interpretation):
    total = 0
    for match in matches:
        if xyz_interpretation == SHAPES:
            them, you = (SHAPES[x] for x in match.split(' '))
        else:
            them = SHAPES[match.split(' ')[0]]
            you_result = RESULTS[match.split(' ')[1]]
            if you_result == 6:
                you = [w[0] for w in WINS if w[1] == them][0]
            elif you_result == 3:
                you = them
            else:
                you = [w[1] for w in WINS if w[0] == them][0]    

        total += game_score(them, you) + choice_score(you)
    return total
    
input = Input()
# PART ONE
# print(total(input.example, SHAPES))
print(total(input.puzzle, SHAPES)) 

# PART TWO
# print(total(input.example, RESULTS))
print(total(input.puzzle, RESULTS)) 
