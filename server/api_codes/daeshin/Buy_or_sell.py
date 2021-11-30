import win32com.client

# 매수 주문 요청
def buy(code : str, count : int, price = 0): 
    # 연결 여부 체크
    objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
    bConnect = objCpCybos.IsConnect
    if (bConnect == 0):
        return "PLUS가 정상적으로 연결되지 않음. "
    
    # 주문 초기화
    objTrade =  win32com.client.Dispatch("CpTrade.CpTdUtil")
    initCheck = objTrade.TradeInit(0)
    if (initCheck != 0):
        return "주문 초기화 실패"
    
    # 주식 매수 주문
    acc = objTrade.AccountNumber[0] #계좌번호
    accFlag = objTrade.GoodsList(acc, 1)  # 주식상품 구분
    #print(acc, accFlag[0])
    objStockOrder = win32com.client.Dispatch("CpTrade.CpTd0311")
    objStockOrder.SetInputValue(0, "2")   # 2: 매수, 1: 매도
    objStockOrder.SetInputValue(1, acc )   #  계좌번호
    objStockOrder.SetInputValue(2, accFlag[0])   # 상품구분 - 주식 상품 중 첫번째
    objStockOrder.SetInputValue(3, code)   # 종목코드 - A003540 - 대신증권 종목
    objStockOrder.SetInputValue(4, count)   # 매수수량

    if price != 0: 
        objStockOrder.SetInputValue(5, price)   # 주문단가  - 14,100원
        objStockOrder.SetInputValue(8, "01")   # 주문호가 구분코드 - 01: 보통
    else:
        objStockOrder.SetInputValue(8, "13")   # 주문호가 구분코드 - 01: 최우선

    objStockOrder.SetInputValue(7, "0")   # 주문 조건 구분 코드, 0: 기본 1: IOC 2:FOK
    
    # 매수 주문 요청
    objStockOrder.BlockRequest()
    
    rqStatus = objStockOrder.GetDibStatus()
    rqRet = objStockOrder.GetDibMsg1()
    #print("통신상태", rqStatus, rqRet)

    if rqStatus != 0:
        return rqRet
        #exit()

    return "매수 주문이 완료되었습니다."



# 매도 주문 요청
def sell(code : str, count : int, price = 0): 
    # 연결 여부 체크
    objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
    bConnect = objCpCybos.IsConnect
    if (bConnect == 0):
        return "PLUS가 정상적으로 연결되지 않음. "
        #exit()
    
    # 주문 초기화
    objTrade =  win32com.client.Dispatch("CpTrade.CpTdUtil")
    initCheck = objTrade.TradeInit(0)
    if (initCheck != 0):
        return "주문 초기화 실패"
        #exit()
    
    
    # 주식 매도 주문
    acc = objTrade.AccountNumber[0] #계좌번호
    accFlag = objTrade.GoodsList(acc, 1)  # 주식상품 구분
    #print(acc, accFlag[0])
    objStockOrder = win32com.client.Dispatch("CpTrade.CpTd0311")
    objStockOrder.SetInputValue(0, "1")   # 2: 매수, 1: 매도
    objStockOrder.SetInputValue(1, acc )   #  계좌번호
    objStockOrder.SetInputValue(2, accFlag[0])   # 상품구분 - 주식 상품 중 첫번째
    objStockOrder.SetInputValue(3, code)   # 종목코드 - A003540 - 대신증권 종목
    objStockOrder.SetInputValue(4, count)   # 매수수량 10주
    
    if price != 0: 
        objStockOrder.SetInputValue(5, price)   # 주문단가  - 14,100원
        objStockOrder.SetInputValue(8, "01")   # 주문호가 구분코드 - 01: 보통
    else:
        objStockOrder.SetInputValue(8, "13")   # 주문호가 구분코드 - 13: 최우선

    objStockOrder.SetInputValue(7, "0")   # 주문 조건 구분 코드, 0: 기본 1: IOC 2:FOK
    
    # 매도 주문 요청
    objStockOrder.BlockRequest()
    
    rqStatus = objStockOrder.GetDibStatus()
    rqRet = objStockOrder.GetDibMsg1()
    #print("통신상태", rqStatus, rqRet)

    if rqStatus != 0:
        return rqRet
        #exit()
    
    return "매도 주문이 완료되었습니다."


def sell_all(code: str):
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

    result = '해당 주식을 보유하고 있지 않습니다.'

    for i in range(cnt):
        종목코드 = objRq.GetDataValue(12, i)
        if 종목코드 == code:
            매도가능수량 = objRq.GetDataValue(15, i)
            result = sell(종목코드, 매도가능수량)
    return result
            