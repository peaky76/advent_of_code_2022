import sys

sys.path.append("..")
from input import Input

CHOICES = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS',
}

SCORES = {
    'ROCK': 1, 
    'PAPER': 2, 
    'SCISSORS': 3
}

WINS = {
    'SCISSORS': 'PAPER',
    'PAPER': 'ROCK',
    'ROCK': 'SCISSORS'
}

CHOICE_STRATEGY = {
    'X': lambda them: 'ROCK',
    'Y': lambda them: 'PAPER',
    'Z': lambda them: 'SCISSORS'
}

RESULT_STRATEGY = {
    'X': lambda them: WINS[them], 
    'Y': lambda them: them, 
    'Z': lambda them: {v: k for k, v in WINS.items()}[them]
}

def determine_choices(match, strategy):
    them_letter, you_letter = match.split(' ')
    them = CHOICES[them_letter]
    you = strategy[you_letter](them)
    return (them, you)

def game_score(them, you):
    return 6 if WINS[you] == them else 3 if them == you else 0

def choice_score(you):
    return SCORES[you]

def total(matches, strategy):
    total = 0
    for match in matches:
        them, you = determine_choices(match, strategy)        
        total += game_score(them, you) + choice_score(you)
    return total
    
input = Input()

# PART ONE
# print(total(input.example, CHOICE_STRATEGY))
print(total(input.puzzle, CHOICE_STRATEGY)) 

# PART TWO
# print(total(input.example, RESULT_STRATEGY))
print(total(input.puzzle, RESULT_STRATEGY)) 
