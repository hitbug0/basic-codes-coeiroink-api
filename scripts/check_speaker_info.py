import json
import requests

# やり取りするローカルサーバ
URL = "http://localhost:50032/"

# スピーカーの情報を一覧表示
def check_speaker_info():
    response = requests.get(URL+"v1/speakers")
    speakers = response.json()
    for speaker in speakers:
        print("\n"+"="*30)
        print(f"name: {speaker['speakerName']}\nid:   {speaker['speakerUuid']}")
        styles = speaker['styles']
        print('styles:')
        for style in styles:
            print(f"     {style['styleId']:>4} : {style['styleName']}")

check_speaker_info()