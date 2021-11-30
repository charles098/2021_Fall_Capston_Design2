import win32com.client
'''
# 보유 종목 정보 - 특정 보유종목 언급하면 해당 종목만 알림. 종목명, 평가손익, 수익률, 매도가능수량
def myStocks_Info():
    objRq = win32com.client.Dispatch("CpTrade.CpTd6033")
    g_objCpTrade = win32com.client.Dispatch('CpTrade.CpTdUtil')

    g_objCpTrade.TradeInit(0) # 매매주문을 위한 초기화

    acc = g_objCpTrade.AccountNumber[0]  # 계좌번호
    accFlag = g_objCpTrade.GoodsList(acc, 1)  # 주식상품 구분

    objRq.SetInputValue(0, acc)  # 계좌번호
    objRq.SetInputValue(1, accFlag[0])  # 상품구분 - 주식 상품 중 첫번째
    objRq.SetInputValue(2, 50)  # 요청 건수(최대 50)

    objRq.BlockRequest()

    cnt = objRq.GetHeaderValue(7) # 보유 종목 수

    for i in range(cnt):
        종목명 = objRq.GetDataValue(0, i)
        #결제잔고수량 = objRq.GetDataValue(3, i)
        #결제장부단가 = objRq.GetDataValue(4, i)
        #전일체결수량 = objRq.GetDataValue(5, i)
        #금일체결수량 = objRq.GetDataValue(6, i)
        #평가금액 = objRq.GetDataValue(9, i)
        평가손익 = objRq.GetDataValue(10, i)
        수익률 = objRq.GetDataValue(11, i)
        #종목코드 = objRq.GetDataValue(12, i)
        #주문구분 = objRq.GetDataValue(13, i)
        매도가능수량 = objRq.GetDataValue(15, i)
        #손익단가 = objRq.GetDataValue(18, i)

        result = '종목명  ' + 종목명 + '  평가손익  ' + str(round(평가손익,2)) + '원  수익률  '
        result += str(round(수익률,3)) + '%' + '  매도가능수량  ' + str(매도가능수량) + '개'

        if 수익률 < 0:
            result = '종목명  ' + 종목명 + '  평가손익  ' + str(round(평가손익,2)) + '원  수익률  마이너스 '
            result += str(-1 * round(수익률,3)) + '%' + '  매도가능수량  ' + str(매도가능수량) + '개'

        print(result)
'''

# 특정 종목 정보
def myStock_Info(code : str):
    inCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
    objRq = win32com.client.Dispatch("CpTrade.CpTd6033")
    g_objCpTrade = win32com.client.Dispatch('CpTrade.CpTdUtil')
    
    g_objCpTrade.TradeInit(0) # 매매주문을 위한 초기화

    stock = inCpStockCode.CodeToName(code)

    acc = g_objCpTrade.AccountNumber[0]  # 계좌번호
    accFlag = g_objCpTrade.GoodsList(acc, 1)  # 주식상품 구분

    objRq.SetInputValue(0, acc)  # 계좌번호
    objRq.SetInputValue(1, accFlag[0])  # 상품구분 - 주식 상품 중 첫번째
    objRq.SetInputValue(2, 50)  # 요청 건수(최대 50)

    objRq.BlockRequest()

    cnt = objRq.GetHeaderValue(7) # 보유 종목 수

    for i in range(cnt):
        종목명 = objRq.GetDataValue(0, i)
        if 종목명 == stock:
            #결제잔고수량 = objRq.GetDataValue(3, i)
            #결제장부단가 = objRq.GetDataValue(4, i)
            #전일체결수량 = objRq.GetDataValue(5, i)
            #금일체결수량 = objRq.GetDataValue(6, i)
            #평가금액 = objRq.GetDataValue(9, i)
            평가손익 = objRq.GetDataValue(10, i)
            수익률 = objRq.GetDataValue(11, i)
            #종목코드 = objRq.GetDataValue(12, i)
            #주문구분 = objRq.GetDataValue(13, i)
            매도가능수량 = objRq.GetDataValue(15, i)
            #손익단가 = objRq.GetDataValue(18, i)

            result = '평가손익  ' + str(round(평가손익,2)) + '원  수익률  '
            result += str(round(수익률,3)) + '%' + '  매도가능수량  ' + str(매도가능수량) + '개'

            if 수익률 < 0:
                result = '평가손익  ' + str(round(평가손익,2)) + '원  수익률  마이너스 '
                result += str(-1 * round(수익률,3)) + '%' + '  매도가능수량  ' + str(매도가능수량) + '개'

            return result


def myStocks_Info():
    objRq = win32com.client.Dispatch("CpTrade.CpTd6033")
    g_objCpTrade = win32com.client.Dispatch('CpTrade.CpTdUtil')

    g_objCpTrade.TradeInit(0) # 매매주문을 위한 초기화

    acc = g_objCpTrade.AccountNumber[0]  # 계좌번호
    accFlag = g_objCpTrade.GoodsList(acc, 1)  # 주식상품 구분

    objRq.SetInputValue(0, acc)  # 계좌번호
    objRq.SetInputValue(1, accFlag[0])  # 상품구분 - 주식 상품 중 첫번째
    objRq.SetInputValue(2, 50)  # 요청 건수(최대 50)

    objRq.BlockRequest()

    cnt = objRq.GetHeaderValue(7) # 보유 종목 수

    result = ''

    for i in range(cnt):
        종목명 = objRq.GetDataValue(0, i)
        #결제잔고수량 = objRq.GetDataValue(3, i)
        #결제장부단가 = objRq.GetDataValue(4, i)
        #전일체결수량 = objRq.GetDataValue(5, i)
        #금일체결수량 = objRq.GetDataValue(6, i)
        #평가금액 = objRq.GetDataValue(9, i)
        평가손익 = objRq.GetDataValue(10, i)
        수익률 = objRq.GetDataValue(11, i)
        #종목코드 = objRq.GetDataValue(12, i)
        #주문구분 = objRq.GetDataValue(13, i)
        매도가능수량 = objRq.GetDataValue(15, i)
        #손익단가 = objRq.GetDataValue(18, i)
        

        if 수익률 < 0:
            result += '종목명  ' + 종목명 + '  평가손익  ' + str(round(평가손익,2)) + '원  수익률  마이너스 '
            result += str(-1 * round(수익률,3)) + '%' + '  매도가능수량  ' + str(매도가능수량) + '개\n'
        else:
            result += '종목명  ' + 종목명 + '  평가손익  ' + str(round(평가손익,2)) + '원  수익률  '
            result += str(round(수익률,3)) + '%' + '  매도가능수량  ' + str(매도가능수량) + '개\n'

    return result


inCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
objRq = win32com.client.Dispatch("CpTrade.CpTd6033")
g_objCpTrade = win32com.client.Dispatch('CpTrade.CpTdUtil')

g_objCpTrade.TradeInit(0) # 매매주문을 위한 초기화

stock = inCpStockCode.CodeToName('A005930')

acc = g_objCpTrade.AccountNumber[0]  # 계좌번호
accFlag = g_objCpTrade.GoodsList(acc, 1)  # 주식상품 구분

objRq.SetInputValue(0, acc)  # 계좌번호
objRq.SetInputValue(1, accFlag[0])  # 상품구분 - 주식 상품 중 첫번째
objRq.SetInputValue(2, 50)  # 요청 건수(최대 50)

objRq.BlockRequest()

cnt = objRq.GetHeaderValue(7) # 보유 종목 수
result = "해당 주식을 보유하고 있지 않습니다."
for i in range(cnt):
    종목명 = objRq.GetDataValue(0, i)
    if 종목명 == stock:
        #결제잔고수량 = objRq.GetDataValue(3, i)
        #결제장부단가 = objRq.GetDataValue(4, i)
        #전일체결수량 = objRq.GetDataValue(5, i)
        #금일체결수량 = objRq.GetDataValue(6, i)
        #평가금액 = objRq.GetDataValue(9, i)
        평가손익 = objRq.GetDataValue(10, i)
        수익률 = objRq.GetDataValue(11, i)
        #종목코드 = objRq.GetDataValue(12, i)
        #주문구분 = objRq.GetDataValue(13, i)
        매도가능수량 = objRq.GetDataValue(15, i)
        #손익단가 = objRq.GetDataValue(18, i)

        result = '평가손익, ' + str(round(평가손익,2)) + '원, 수익률, '
        result += str(round(수익률,3)) + '%' + ', 매도가능수량, ' + str(매도가능수량) + '개'

        if 수익률 < 0:
            result = '평가손익, ' + str(round(평가손익,2)) + '원, 수익률, 마이너스 '
            result += str(-1 * round(수익률,3)) + '%' + ', 매도가능수량, ' + str(매도가능수량) + '개'

print(result)