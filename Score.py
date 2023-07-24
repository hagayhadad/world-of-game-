
from Utils import SCORES_FILE_NAME

def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5

    try:
        # Try to read the current score from the scores file
        with open(SCORES_FILE_NAME, 'r') as file:
            current_score = int(file.readline())
    except FileNotFoundError:
        # If the scores file doesn't exist, create a new one
        current_score = 0

    # Add the new score to the current score
    current_score += POINTS_OF_WINNING

    # Save the updated score to the scores file
    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(str(current_score))

def first_score():

    try:
        # Try to read the current score from the scores file
        with open(SCORES_FILE_NAME, 'r') as file:
            current_score = 0
    except FileNotFoundError:
        # If the scores file doesn't exist, create a new one
        current_score = 0

    # Save the updated score to the scores file
    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(str(current_score))
