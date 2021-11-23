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
    AvDeposit = instCpTd5331.GetHeaderValue(47)
    주문가능금액 = instCpTd5331.GetHeaderValue(10)

    print("예수금 = %d" % Deposit)
    #print("주문가능금액 = %d" % 주문가능금액 )


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
    주문가능금액 = instCpTd5331.GetHeaderValue(10)

    print("주문가능금액 = %d" % 주문가능금액 )



'''
import win32com.client


# 잔고 예수금 확인
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
Deposite = instCpTd5331.GetHeaderValue(45)
AvDeposite = instCpTd5331.GetHeaderValue(47)
주문가능금액 = instCpTd5331.GetHeaderValue(10)

print("예수금 = %d" % Deposite)
print("주문가능금액 = %d" % 주문가능금액 )

'''