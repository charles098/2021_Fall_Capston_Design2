import win32com.client
###### 자바스크립트에서 한글 깨짐 현상 방지용 ################################
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
###########################################################################


# 주식 코드로 종목명 가져오기 
inCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
codeToName = inCpStockCode.CodeToName("A000100")
nameToCode = inCpStockCode.NameToCode("유한양행")
print(codeToName)
print(nameToCode)


inStockMst = win32com.client.Dispatch("dscbo1.StockMst")
inStockMst.SetInputValue(0, "A000660")   
inStockMst.BlockRequest()
current = inStockMst.GetHeaderValue(11)         # 현재가
print(current)