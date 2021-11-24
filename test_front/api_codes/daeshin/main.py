###### 자바스크립트에서 한글 깨짐 현상 방지용 ################################
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
###########################################################################
import StockInfo
import Stock2code
import Buy_or_sell
import MyInfo

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

result = '스부아, 쿳하니, 므'
'''
# 1. 'STOCK_INFO'가 tag_word.keys()에 있으면 [주식 정보 함수] 호출 ex) 삼성전자 현재가
if 'STOCK_INFO' in tag_word.keys():
    result = StockInfo.stockInfo(Stock2code.stock_code[tag_word['STOCK']], tag_word['STOCK_INFO'])

# 2. 매수 주문 - 주문조건 : 보통, 주문호가 : 최우선  , 주식 단위는 '개'로 통일 ex) 삼성전다 다섯개 매수
if 'BUY' in tag_word.keys():
    result = Buy_or_sell.buy(Stock2code.stock_code[tag_word['STOCK']], int(tag_word['SN']))

# 3. 매도 주문 - 주문조건 : 보통, 주문호가 : 최우선  , 주식 단위는 '개'로 통일 ex) 삼성전자 열일곱개 매도
if 'SELL' in tag_word.keys():
    result = Buy_or_sell.sell(Stock2code.stock_code[tag_word['STOCK']], int(tag_word['SN']))

# 4. 예수금, 주문가능금액, 계좌번호 ex) 예수금 확인
if 'DEPOSIT' in tag_word.keys(): result = MyInfo.deposit() # 예수금
if 'ORDERABLE_ACCOUNT' in tag_word.keys(): result = MyInfo.orderable_account() # 주문가능금액
if 'ACCOUNT_NUMBER' in tag_word.keys(): result = MyInfo.accountNumber() # 계좌번호

# 5. 계좌정보 -> 계좌수익률, 계좌평가손익
if 'ACCOUNT_INFO' in tag_word.keys(): result = MyInfo.accountInfo()

# 6. 보유주식정보 -> 종목명, 평가손익, 수익률, 매도가능수량 ex) 보유주식정보 확인
# 7. 특정주식정보 -> 평가손익, 수익률, 매도가능수량 ex) 삼성전자 보유주식정보
if 'MYSTOCK_INFO' in tag_word.keys() :
    if 'STOCK' in tag_word.keys(): result = MyInfo.myStock_Info(Stock2code.stock_code[tag_word['STOCK']])
    else: result = MyInfo.myStocks_Info() 
'''

print(result)


