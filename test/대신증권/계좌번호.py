import win32com.client


# 계좌번호 확인
def accountNumber():
    instCpTdUtil = win32com.client.Dispatch("CpTrade.CpTdUtil")
    instCpTdUtil.TradeInit() # 매매주문을 위한 초기화
    계좌번호 = instCpTdUtil.AccountNumber[0]

    print("계좌번호 : %s" % 계좌번호)



'''
import win32com.client


# 계좌번호 확인
instCpTdUtil = win32com.client.Dispatch("CpTrade.CpTdUtil")
instCpTdUtil.TradeInit() # 매매주문을 위한 초기화
계좌번호 = instCpTdUtil.AccountNumber[0]

print("계좌번호 : %s" % 계좌번호)
'''