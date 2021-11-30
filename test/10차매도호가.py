
import win32com.client
'''
inStockMst = win32com.client.Dispatch("dscbo1.StockJpBid")
inStockMst.SetInputValue(0, 'A005930')   
inStockMst.Subscribe()
print(inStockMst.GetHeaderValue(3)) # 1차 매도호가
print(inStockMst.GetHeaderValue(3)) # 1차 매수호가
'''

objStockMst = win32com.client.Dispatch("DsCbo1.StockMst")
 

objStockMst.SetInputValue(0, 'A005930')
objStockMst.BlockRequest()

# 10차호가
for i in range(10):
    print(objStockMst.GetDataValue(0, i))  # 매도호가
    #print(objStockMst.GetDataValue(1, i) ) # 매수호가
    #print(objStockMst.GetDataValue(2, i))  # 매도호가 잔량
    #print(objStockMst.GetDataValue(3, i) ) # 매수호가 잔량
    #print()
