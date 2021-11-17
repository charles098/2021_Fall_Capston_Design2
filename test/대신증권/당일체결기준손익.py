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
