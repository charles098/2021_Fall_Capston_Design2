import requests
###### 자바스크립트에서 한글 깨짐 현상 방지용 ################################
import sys
import io
import os
import datetime
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
###########################################################################
result = sys.argv[1]
TTSfilename = sys.argv[2]

# 카카오 TTS 진행
kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"

rest_api_key = '76969f41937bb5c65e87d79059215f0d'

headers = {
    "Content-Type": "application/xml",
    "Authorization": "KakaoAK " + rest_api_key,
}

# text = "평가손익, -10618원, 수익률, 마이너스 1.7%, 매도가능수량, 7개"

res = requests.post(kakao_speech_url, headers=headers, 
                    data=f"<speak>{result}</speak>".encode('utf-8'))
#print(os.getcwd())
#new_fileName = str(datetime.datetime.now()).replace(':','_') + '.mp3'

#with open('./ttsFile/' + new_fileName, 'wb') as file:
 #   file.write(res.content)

#print(new_fileName, result)

with open('./ttsFile/' + TTSfilename, 'wb') as file:
    file.write(res.content)

print(result)
