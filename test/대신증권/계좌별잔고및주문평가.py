import win32com.client

g_objCodeMgr = win32com.client.Dispatch('CpUtil.CpCodeMgr')
g_objCpStatus = win32com.client.Dispatch('CpUtil.CpCybos')
g_objCpTrade = win32com.client.Dispatch('CpTrade.CpTdUtil')

g_objCpTrade.TradeInit(0)

# Cp6032 : 주식 잔고 조회````
acc = g_objCpTrade.AccountNumber[0]  # 계좌번호
accFlag = g_objCpTrade.GoodsList(acc, 1)  # 주식상품 구분
print(acc, accFlag[0])

objRq = win32com.client.Dispatch("CpTrade.CpTd6033")


objRq.SetInputValue(0, acc)  # 계좌번호
objRq.SetInputValue(1, accFlag[0])  # 상품구분 - 주식 상품 중 첫번째
objRq.SetInputValue(2, 3)  # 요청건수 default 14건

objRq.BlockRequest()

계좌명 = objRq.GetHeaderValue(0)
결제잔고수량 = objRq.GetHeaderValue(1)
체결잔고수량 = objRq.GetHeaderValue(2)
평가금액 = objRq.GetHeaderValue(3)
평가손익 = objRq.GetHeaderValue(4)
수익률 = objRq.GetHeaderValue(8)

print("계좌명= %s" % 계좌명)
print("결제잔고수량 = %s" % 결제잔고수량)
print("체결잔고수량 = %f" %  체결잔고수량)
print("평가금액 = %f" % 평가금액)
print("평가손익 = %f" % 평가손익)
print("수익률 = %f" % 수익률)

print()

for i in range(3):
    종목명 = objRq.GetDataValue(0, i)
    결제잔고수량 = objRq.GetDataValue(3, i)
    결제장부단가 = objRq.GetDataValue(4, i)
    전일체결수량 = objRq.GetDataValue(5, i)
    금일체결수량 = objRq.GetDataValue(6, i)
    평가금액 = objRq.GetDataValue(9, i)
    평가손익 = objRq.GetDataValue(10, i)
    수익률 = objRq.GetDataValue(11, i)
    종목코드 = objRq.GetDataValue(12, i)
    주문구분 = objRq.GetDataValue(13, i)
    매도가능수량 = objRq.GetDataValue(15, i)
    손익단가 = objRq.GetDataValue(18, i)

    print("종목명 = %s" % 종목명)
    print("결제잔고수량 = %s" % 결제잔고수량)
    print("결제장부단가 = %f" %  결제장부단가)
    print("전일체결수량 = %f" % 전일체결수량)
    print("평가금액 = %f" % 평가금액)
    print("평가손익 = %f" % 평가손익)
    print("수익률 = %s" % 수익률)
    print("종목코드 = %s" % 종목코드)
    print("주문구분 = %f" %  주문구분)
    print("매도가능수량 = %f" % 매도가능수량)
    print("손익단가 = %f" % 손익단가)
    print()

'''
참고 code

import win32com.client

g_objCodeMgr = win32com.client.Dispatch('CpUtil.CpCodeMgr')
g_objCpStatus = win32com.client.Dispatch('CpUtil.CpCybos')
g_objCpTrade = win32com.client.Dispatch('CpTrade.CpTdUtil')

g_objCpTrade.TradeInit(0)

# Cp6032 : 주식 잔고 조회
acc = g_objCpTrade.AccountNumber[0]  # 계좌번호
accFlag = g_objCpTrade.GoodsList(acc, 1)  # 주식상품 구분
print(acc, accFlag[0])

objRq = win32com.client.Dispatch("CpTrade.CpTd6032")


objRq.SetInputValue(0, acc)  # 계좌번호
objRq.SetInputValue(1, accFlag[0])  # 상품구분 - 주식 상품 중 첫번째


objRq.BlockRequest()


cnt = objRq.GetHeaderValue(0)
print('데이터 조회 개수', cnt)


sumJango = objRq.GetHeaderValue(1)
sumSellM = objRq.GetHeaderValue(2)
sumRate = objRq.GetHeaderValue(3)

print('잔량평가손익', sumJango, '매도실현손익',sumSellM, '수익률',sumRate)


for i in range(cnt):
    item = {}
    item['종목코드'] = objRq.GetDataValue(12, i)  # 종목코드
    item['종목명'] = objRq.GetDataValue(0, i)  # 종목명
    item['신용일자'] = objRq.GetDataValue(1, i)
    item['전일잔고'] = objRq.GetDataValue(2, i)
    item['금일매수수량'] = objRq.GetDataValue(3, i)
    item['금일매도수량'] = objRq.GetDataValue(4, i)
    item['금일잔고'] = objRq.GetDataValue(5, i)
    item['평균매입단가'] = objRq.GetDataValue(6, i)
    item['평균매도단가'] = objRq.GetDataValue(7, i)
    item['현재가'] = objRq.GetDataValue(8, i)
    item['잔량평가손익'] = objRq.GetDataValue(9, i)
    item['매도실현손익'] = objRq.GetDataValue(10, i)
    item['수익률'] = objRq.GetDataValue(11, i)

    print(item)

'''