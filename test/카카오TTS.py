import requests
import sys
import os
kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"

rest_api_key = '76969f41937bb5c65e87d79059215f0d'

headers = {
    "Content-Type": "application/xml",
    "Authorization": "KakaoAK " + rest_api_key,
}

text = "평가손익, -10618원, 수익률, 마이너스 1.7%, 매도가능수량, 7개"

res = requests.post(kakao_speech_url, headers=headers, 
                    data=f"<speak>{text}</speak>".encode('utf-8'))
print(type(res.content))
print(os.getcwd())
with open('./test/audio_file/output.mp3', 'wb') as file:
    file.write(res.content)
    print('완료')

