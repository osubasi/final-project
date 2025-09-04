import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myinput = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myinput, headers=headers)
    formatted_response = json.loads(response.text)

    emotions = formatted_response['emotionPredictions']
    #print(emotions[0]['emotion'])
    dominant = ''
    score = 0
    mydict = {}
    for key, value in emotions[0]['emotion'].items():
        mydict[key] = value
        if(value > score):
            score = value
            dominant = key
    
    mydict['dominant_emotion'] = dominant
    
    if response.status_code == 200:
        return mydict

    elif response.status_code == 500:
        return -1
