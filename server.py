'''
    Here's the module doc string
'''
from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

TEXT_RESPONSE = 'For the given statement, the system response is '


@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    '''
    This is the http end-point for doc string control
    '''

    # Get JSON data from request
    data = request.get_json()

    response = emotion_detector(data['text'])

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    text = TEXT_RESPONSE
    dominant_emotion = None
    end_template = f". The dominant emotion is {dominant_emotion}"

    for emotion, value in response.items():
        if emotion != 'dominant_emotion':
            text += f"\'{emotion}\': {value},".format(emotion=emotion, value=value)

    text += end_template.format(dominant_emotion=response['dominant_emotion'])

    return text

if __name__ == '__main__':
    app.run(debug=True)
