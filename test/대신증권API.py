import win32com.client
###### 자바스크립트에서 한글 깨짐 현상 방지용 ################################
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
###########################################################################


# 주식 코드로 종목명 가져오기 
inCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
codeToName = inCpStockCode.CodeToName("A005930")
nameToCode = inCpStockCode.NameToCode("삼성전자")
print(codeToName)
#print(nameToCode)

# 현재가 가져오기
inStockMst = win32com.client.Dispatch("dscbo1.StockMst")
inStockMst.SetInputValue(0, "A005930")   
inStockMst.BlockRequest()
current = inStockMst.GetHeaderValue(11)         # 현재가
yesterday_end = inStockMst.GetHeaderValue(10)   # 전일종가
#print(current)
print(yesterday_end)


#잔고 확인
inCpTd6033 = win32com.client.Dispatch('CpTrade.CpTd6033')
instCpTdUtil = win32com.client.Dispatch("CpTrade.CpTdUtil")
instCpTdUtil.TradeInit()
accountNumber = instCpTdUtil.AccountNumber[0]
inCpTd6033.SetInputValue(0, accountNumber)
value = inCpTd6033.GetHeaderValue(0) # 계좌 번호
inCpTd6033.BlockRequest()
print(accountNumber)
print(value)


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
#instCpTd5331.SetInputValue(5, "N") # 도움말 default
instCpTd5331.SetInputValue(5, "Y")
instCpTd5331.SetInputValue(6, ord("1")) # 도움말 default

instCpTd5331.BlockRequest()
Deposite = instCpTd5331.GetHeaderValue(45)
AvDeposite = instCpTd5331.GetHeaderValue(47)
현금주문가능금액 = instCpTd5331.GetHeaderValue(10)
현금주문 = instCpTd5331.GetHeaderValue(4)

print("예수금 = %d" % Deposite)
print("가용예수금 = %d" % AvDeposite)
print("현금주문가능금액 = %d" % 현금주문가능금액 )
print("현금주문 = %d" % 현금주문 )


