# MainScores.py

from flask import Flask

from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)



def read_score():
    try:
        # Try to read the current score from the scores file
        with open(SCORES_FILE_NAME, 'r') as file:
            current_score = int(file.readline())
            return current_score
    except FileNotFoundError:
        # If the scores file doesn't exist, return the BAD_RETURN_CODE
        return BAD_RETURN_CODE

@app.route('/')
def score_server():
    # Read the score from the scores file
    score = read_score()

    # Prepare the HTML response
    if score != BAD_RETURN_CODE:
        html_response = f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1>The score is <div id="score">{score}</div></h1>
        </body>
        </html>
        """
    else:
        html_response = f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1><div id="score" style="color:red">Error: Unable to read score.</div></h1>
        </body>
        </html>
        """

    return html_response

if __name__ == '__main__':
    app.run()
