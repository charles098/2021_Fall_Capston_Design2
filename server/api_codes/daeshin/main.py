###### 자바스크립트에서 한글 깨짐 현상 방지용 ################################
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
###########################################################################
import StockInfo
import Stock2code

# mecab으로부터 받은 것은 문자열
# 공백으로 분리되어있다. 단어 + 태그 순서 
tags = sys.argv[1]
tags = tags.strip() # 앞뒤 공백 먼저 제거 

tags_list = tags.split()

# {태그 : 단어} 사전 생성
tag_word = {}
for i in range(int(len(tags_list) / 2)):
    # 2 * i 인덱스 원소는 단어
    # 2 * i + 1 인덱스 원소는 태그
    tag_word[tags_list[2 * i + 1]] = tags_list[2 * i]
#print(tag_word)



if 'STOCK_INFO' in tag_word.keys():
    # 1. 'STOCK_INFO'가 tag_word.keys()에 있으면 [주식 정보 함수] 호출
    result = StockInfo.stockInfo(Stock2code.stock_code[tag_word['STOCK']], tag_word['STOCK_INFO'])
    print(result)
