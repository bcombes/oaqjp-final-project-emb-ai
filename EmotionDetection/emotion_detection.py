import requests

def emotion_detector(text_to_analyze):

    if text_to_analyze is None or text_to_analyze == "":
        return { 'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, headers=headers, json=data)

    emotions =  response.json()["emotionPredictions"][0]["emotion"]

    dominant_emotion = None

    for emotion, value in emotions.items():
        if dominant_emotion is None:
            dominant_emotion = emotion
        elif emotions[emotion] > emotions[dominant_emotion]:
            dominant_emotion = emotion   

    emotions['dominant_emotion'] = dominant_emotion

    return emotions;
