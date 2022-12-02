with open("input.txt", "r") as file:
    guide = [l.split(" ") for l in file.read().splitlines()]

# Dictionary to hold rock paper scissor wins and loses
rock_paper_scissor = {
    "A": {
        "X": 3,
        "Y": 6,
        "Z": 0
    },
    "B": {
        "X": 0,
        "Y": 3,
        "Z": 6
    },
    "C": {
        "X": 6,
        "Y": 0,
        "Z": 3
    }
}

# Dictionary to hold the scores for selection
scores = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

# Part 1 : Based on starategy guide calculate total.
score = 0
for opponent_choice, my_choice in guide:
    score += rock_paper_scissor[opponent_choice][my_choice] + scores[my_choice]
print(score)

# Part 2 : Consider my_choice as the outcome of game and calculate total.
# Dictionary to hold rock paper scissor wins and loses
rock_paper_scissor_outcome = {
    "A": {
        "X": "Z",
        "Y": "X",
        "Z": "Y"
    },
    "B": {
        "X": "X",
        "Y": "Y",
        "Z": "Z"
    },
    "C": {
        "X": "Y",
        "Y": "Z",
        "Z": "X"
    }
}

score = 0
for opponent_choice, my_choice in guide:
    outcome_choice = rock_paper_scissor_outcome[opponent_choice][my_choice]
    score += rock_paper_scissor[opponent_choice][outcome_choice] + scores[outcome_choice]
print(score)