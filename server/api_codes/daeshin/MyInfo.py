import win32com.client


# 예수금 확인
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

    return Deposit

# 주문가능금액 확인
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
    주문가능금액 = instCpTd5331.GetHeaderValue(10)

    return 주문가능금액

