import requests
import json
kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"

rest_api_key = '76969f41937bb5c65e87d79059215f0d'

headers = {
    "Content-Type": "application/octet-stream",
    "X-DSS-Service": "DICTATION",
    "Authorization": "KakaoAK " + rest_api_key,
}

with open('./audio_file/hello.wav', 'rb') as fp:
    audio = fp.read()

res = requests.post(kakao_speech_url, headers=headers, data=audio)
print(res.text)