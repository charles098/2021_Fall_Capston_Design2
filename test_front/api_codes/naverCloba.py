###### 자바스크립트에서 한글 깨짐 현상 방지용 ################################
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
###########################################################################

print('삼성전자 전일종가 알려줘')
'''
import requests

# 네이버 클로바 API - 15초/4원 과금

data = open('./uploads/' + sys.argv[1], "rb") # STT를 진행하고자 하는 음성 파일

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
    #print (response.text)
    print(response.text.split('":"')[1].split('"')[0].replace(' ',''))
    # 공백 없이 전부
else:
    print("Error : " + response.text)
'''
