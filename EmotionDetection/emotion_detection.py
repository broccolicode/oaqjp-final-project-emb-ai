import requests
import json




def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = {"raw_document": {"text": text_to_analyse}}  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj,headers=header)

    if response.status_code == 500:
        return None
    if response.status_code == 400:
        return None

    # Send a POST request to the API with the text and headers
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    emotions['dominant_emotion'] = max(emotions, key=emotions.get)

    return emotions