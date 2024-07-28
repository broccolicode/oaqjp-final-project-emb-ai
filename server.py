"""
This module sets up a Flask web application that detects emotions from user input.
It includes two routes: one for rendering the index page and another for handling
emotion detection requests.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def sent_analyzer():
    """
    This function catches the request and tests for emotion detection
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text! Please try again!"

    dominant_emotion = response.pop('dominant_emotion')
    emotions_str = ', '.join([f"'{k}': {v}" for k, v in response.items()])
    emotions_list = emotions_str.rsplit(', ', 1)
    emotions_str = ' and '.join(emotions_list)

    # Form the final sentence
    emotions = f"{emotions_str}. The dominant emotion is {dominant_emotion}"

    return f"For the given statement, the system response is {emotions}."


@app.route("/")
def render_index_page():
    """
    This function renders the index page for the web application
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
