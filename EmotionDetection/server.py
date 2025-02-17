from flask import flask
from emotion_detection import emotion_detector

app = Flask('emotion detector')



@app.route('/emotionDetector')
def detect_emotion();
