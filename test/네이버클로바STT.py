# 네이버 클로바 API - 15초/4원 과금
import requests

data = open("./audio_file/2021-12-11T07_55_07.101Z.wav", "rb") # STT를 진행하고자 하는 음성 파일

Lang = "Kor" # Kor / Jpn / Chn / Eng
URL = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + Lang
    
ID = "sb21okbjmh" # 인증 정보의 Client ID
Secret = "iFVd8KWihMzJnXRFGbpBQ6vutUT0FhmLzTSAnklV" # 인증 정보의 Client Secret
    
headers = {
    "Content-Type": "application/octet-stream", # Fix
    "X-NCP-APIGW-API-KEY-ID": ID,
    "X-NCP-APIGW-API-KEY": Secret,
}
response = requests.post(URL,  data=data, headers=headers)
rescode = response.status_code

if(rescode == 200):
    #print(response.text.split('":"')[1].split('"')[0].replace(' ',''))
    print(response.text)
else:
    print("Error : " + response.text)