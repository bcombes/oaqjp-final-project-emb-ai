from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

text_response = 'For the given statement, the system response is '


@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():

    # Get JSON data from request
    data = request.get_json()

    response = emotion_detector(data['text'])

    text = text_response

    for emotion, value in response.items():
        if(emotion != 'dominant_emotion'):
            text += "\'{emotion}\': {value},".format(emotion=emotion, value=value)

    text += ". The dominant emotion is {dominant_emotion}".format(dominant_emotion=response['dominant_emotion'])

    return text       

if __name__ == '__main__':
    app.run(debug=True)