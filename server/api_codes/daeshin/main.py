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
import Not_executed
import win32com.client

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

result = '문제발생'

# 1. 'STOCK_INFO'가 tag_word.keys()에 있으면 [주식 정보 함수] 호출 ex) 삼성전자 현재가
if 'STOCK_INFO' in tag_word.keys():
    result = StockInfo.stockInfo(Stock2code.stock_code[tag_word['STOCK']], tag_word['STOCK_INFO'])

# 2. 매수 주문 - 주문조건 : 보통, 주문호가 : 최우선  , 주식 단위는 '개'로 통일 ex) 삼성전자 다섯개 매수
if 'BUY' in tag_word.keys():
    if 'CUSTOM_BUY' in tag_word.keys(): # N차 매수호가로 매수 ex) 삼성전자 3차매수호가에 두개 매수
        num = int(tag_word['CUSTOM_BUY'][0])
        objStockMst = win32com.client.Dispatch("DsCbo1.StockMst")
        objStockMst.SetInputValue(0, Stock2code.stock_code[tag_word['STOCK']])
        objStockMst.BlockRequest()
        price = objStockMst.GetDataValue(0, num - 1)  # NUM차 매수호가
        result = Buy_or_sell.buy(Stock2code.stock_code[tag_word['STOCK']], int(tag_word['SN']), price)
    elif 'CUSTOM_SELL' in tag_word.keys(): # N차 매도호가로 매도 ex) 삼성전자 2차매도호가에 네개 매도
        num = int(tag_word['CUSTOM_SELL'][0])
        objStockMst = win32com.client.Dispatch("DsCbo1.StockMst")
        objStockMst.SetInputValue(0, Stock2code.stock_code[tag_word['STOCK']])
        objStockMst.BlockRequest()
        price = objStockMst.GetDataValue(1, num)  # NUM차 매도호가
        result = Buy_or_sell.buy(Stock2code.stock_code[tag_word['STOCK']], int(tag_word['SN']), price)
    else:
        if tags_list.count('SN') == 1:
            result = Buy_or_sell.buy(Stock2code.stock_code[tag_word['STOCK']], int(tag_word['SN']))

# 3. 매도 주문 - 주문조건 : 보통, 주문호가 : 최우선  , 주식 단위는 '개'로 통일 ex) 삼성전자 열일곱개 매도
if 'SELL' in tag_word.keys():
    if 'CUSTOM_SELL' in tag_word.keys(): # N차 매도호가로 매도 ex) 삼성전자 2차매도호가에 네개 매도
        num = int(tag_word['CUSTOM_SELL'][0])
        objStockMst = win32com.client.Dispatch("DsCbo1.StockMst")
        objStockMst.SetInputValue(0, Stock2code.stock_code[tag_word['STOCK']])
        objStockMst.BlockRequest()
        price = objStockMst.GetDataValue(1, num)  # NUM차 매도호가
        result = Buy_or_sell.sell(Stock2code.stock_code[tag_word['STOCK']], int(tag_word['SN']), price)
    elif 'CUSTOM_BUY' in tag_word.keys(): # N차 매수호가로 매수 ex) 삼성전자 3차매수호가에 두개 매수
        num = int(tag_word['CUSTOM_BUY'][0])
        objStockMst = win32com.client.Dispatch("DsCbo1.StockMst")
        objStockMst.SetInputValue(0, Stock2code.stock_code[tag_word['STOCK']])
        objStockMst.BlockRequest()
        price = objStockMst.GetDataValue(0, num - 1)  # NUM차 매수호가
        result = Buy_or_sell.sell(Stock2code.stock_code[tag_word['STOCK']], int(tag_word['SN']), price)
    else:
        if tags_list.count('SN') == 1:
            result = Buy_or_sell.sell(Stock2code.stock_code[tag_word['STOCK']], int(tag_word['SN']))

# 4. 전체 매도 ex) 삼성전자 전체매도
if 'SELL_ALL' in tag_word.keys():
    result = Buy_or_sell.sell_all(Stock2code.stock_code[tag_word['STOCK']])

# 5. 예수금, 주문가능금액, 계좌번호 ex) 예수금 확인
if 'DEPOSIT' in tag_word.keys(): result = MyInfo.deposit() # 예수금
if 'ORDERABLE_ACCOUNT' in tag_word.keys(): result = MyInfo.orderable_account() # 주문가능금액
if 'ACCOUNT_NUMBER' in tag_word.keys(): result = MyInfo.accountNumber() # 계좌번호

# 6. 계좌정보 -> 계좌수익률, 계좌평가손익
if 'ACCOUNT_INFO' in tag_word.keys(): result = MyInfo.accountInfo()

# 7. 보유주식정보 -> 종목명, 평가손익, 수익률, 매도가능수량 ex) 보유주식정보 확인
# 8. 특정주식정보 -> 평가손익, 수익률, 매도가능수량 ex) 삼성전자 보유주식정보
if 'MYSTOCK_INFO' in tag_word.keys() :
    if 'STOCK' in tag_word.keys(): result = MyInfo.myStock_Info(Stock2code.stock_code[tag_word['STOCK']])
    else: result = MyInfo.myStocks_Info() 

# 9. 최고상승종목 ex) 최고상승종목 15개 알려줘
if 'HIGHEST_RANK' in tag_word.keys():
    result = StockInfo.est_rank(1, int(tag_word['SN']))

# 10. 최고하락종목 ex) 최고하락종목 8개 알려줘
if 'LOWEST_RANK' in tag_word.keys():
    result = StockInfo.est_rank(0, int(tag_word['SN']))

# 11. 미체결 내역 조회
if 'SHOW_NOT_EXECUTED' in tag_word.keys():
    result = Not_executed.not_executed(1, "None")

# 12. 단일 주문 취소  ex) "삼성전자 주문 취소"
if (('CANCEL_SINGLE' in tag_word.keys()) and ('STOCK' in tag_word.keys())):
    result = Not_executed.not_executed(2, Stock2code.stock_code[tag_word['STOCK']])

# 13. 전종목 주문 취소
if 'CANCEL_ALL' in tag_word.keys():
    result = Not_executed.not_executed(3, "None")

print(result)

