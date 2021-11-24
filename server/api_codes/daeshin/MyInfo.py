import win32com.client


# 예수금 확인 - 결제일에 미수금 발생해서 반대매매 발생할 수도 있음
def deposit():
    instCpTdUtil = win32com.client.Dispatch("CpTrade.CpTdUtil")
    instCpTdUtil.TradeInit() # 매매주문을 위한 초기화
    AccountNumber = instCpTdUtil.AccountNumber[0]

    instCpTd5331 = win32com.client.Dispatch("CpTrade.CpTdNew5331A")

    instCpTd5331.SetInputValue(0, AccountNumber)
    instCpTd5331.SetInputValue(1, "10")
    instCpTd5331.SetInputValue(2, "") # 도움말 default
    instCpTd5331.SetInputValue(3, "01") # 도움말 default
    instCpTd5331.SetInputValue(4, 0) # 도움말 default
    instCpTd5331.SetInputValue(5, "N") # 도움말 default
    #instCpTd5331.SetInputValue(5, "Y")
    instCpTd5331.SetInputValue(6, ord("1")) # 도움말 default

    instCpTd5331.BlockRequest()
    Deposit = instCpTd5331.GetHeaderValue(45)

    return str(Deposit) + '원, 입니다.'


# 주문가능금액 확인 - 증거금 등으로 사용한 금액을 제외한 예수금을 의미
def orderable_account():
    instCpTdUtil = win32com.client.Dispatch("CpTrade.CpTdUtil")
    instCpTdUtil.TradeInit() # 매매주문을 위한 초기화
    AccountNumber = instCpTdUtil.AccountNumber[0]

    instCpTd5331 = win32com.client.Dispatch("CpTrade.CpTdNew5331A")

    instCpTd5331.SetInputValue(0, AccountNumber)
    instCpTd5331.SetInputValue(1, "10")
    instCpTd5331.SetInputValue(2, "") # 도움말 default
    instCpTd5331.SetInputValue(3, "01") # 도움말 default
    instCpTd5331.SetInputValue(4, 0) # 도움말 default
    instCpTd5331.SetInputValue(5, "N") # 도움말 default
    #instCpTd5331.SetInputValue(5, "Y")
    instCpTd5331.SetInputValue(6, ord("1")) # 도움말 default

    instCpTd5331.BlockRequest()
    Orderable_account = instCpTd5331.GetHeaderValue(10)

    return str(Orderable_account) + '원, 입니다.'


# 계좌번호 확인
def accountNumber():
    instCpTdUtil = win32com.client.Dispatch("CpTrade.CpTdUtil")
    instCpTdUtil.TradeInit() # 매매주문을 위한 초기화
    accNum = instCpTdUtil.AccountNumber[0]

    return str(accNum) + ', 입니다.'


# 계좌수익률
def accountInfo():
    g_objCpTrade = win32com.client.Dispatch('CpTrade.CpTdUtil')

    g_objCpTrade.TradeInit(0)

    # Cp6032 : 주식 잔고 조회````
    acc = g_objCpTrade.AccountNumber[0]  # 계좌번호
    accFlag = g_objCpTrade.GoodsList(acc, 1)  # 주식상품 구분
    print(acc, accFlag[0])

    objRq = win32com.client.Dispatch("CpTrade.CpTd6033")

    objRq.SetInputValue(0, acc)  # 계좌번호
    objRq.SetInputValue(1, accFlag[0])  # 상품구분 - 주식 상품 중 첫번째
    objRq.SetInputValue(2, 50)  # 요청건수 default 14건, 최대값 50. 최대값으로 설정

    objRq.BlockRequest()

   #계좌명 = objRq.GetHeaderValue(0)
   #결제잔고수량 = objRq.GetHeaderValue(1)
   #체결잔고수량 = objRq.GetHeaderValue(2)
   #평가금액 = objRq.GetHeaderValue(3)
    평가손익 = objRq.GetHeaderValue(4)
    수익률 = objRq.GetHeaderValue(8)

    result = '평가손익은, ' + str(round(평가손익,2)) + '원, 수익률은, ' + str(round(수익률,3)) + '% 입니다.'

    if 수익률 < 0:
        result = '평가손익은, ' + str(round(평가손익,2)) + '원, 수익률은, 마이너스 ' + str(-1 * round(수익률,3)) + '% 입니다.'

    return result


# 보유 주식 정보 - 특정 보유종목 언급하면 해당 종목만 알림. 종목명, 평가손익, 수익률, 매도가능수량
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
            result += '종목명, ' + 종목명 + ', 평가손익, ' + str(round(평가손익,2)) + '원, 수익률, 마이너스 '
            result += str(-1 * round(수익률,3)) + '%' + ', 매도가능수량, ' + str(매도가능수량) + '개,\n'
        else:
            result += '종목명, ' + 종목명 + ', 평가손익, ' + str(round(평가손익,2)) + '원, 수익률, '
            result += str(round(수익률,3)) + '%' + ', 매도가능수량, ' + str(매도가능수량) + '개,\n'
    
    return result


# 특정 주식 정보
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

            result = '평가손익, ' + str(round(평가손익,2)) + '원, 수익률, '
            result += str(round(수익률,3)) + '%' + ', 매도가능수량, ' + str(매도가능수량) + '개'

            if 수익률 < 0:
                result = '평가손익, ' + str(round(평가손익,2)) + '원, 수익률, 마이너스 '
                result += str(-1 * round(수익률,3)) + '%' + ', 매도가능수량, ' + str(매도가능수량) + '개'

            return result