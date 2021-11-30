import sys
from PyQt5.QtWidgets import *
import win32com.client
 

# 상승종목
objRq = win32com.client.Dispatch("CpSysDib.CpSvrNew7043")
objRq.SetInputValue(0, ord('1')) # 거래소
objRq.SetInputValue(1, ord('2'))  # 상승 ,  4는 하락
objRq.SetInputValue(2, ord('1'))  # 당일
objRq.SetInputValue(3, 21)  # 전일 대비 상위 순 ,  22는 전일대비 하위순
objRq.SetInputValue(4, ord('1'))  # 관리 종목 제외
objRq.SetInputValue(5, ord('0'))  # 거래량 전체
objRq.SetInputValue(6, ord('0'))  # '표시 항목 선택 - '0': 시가대비
objRq.SetInputValue(7, 0)  #  등락율 시작
objRq.SetInputValue(8, 30)  # 등락율 끝

objRq.BlockRequest();

# 상위 10종목
for i in range(5):
    code = objRq.GetDataValue(0, i)  # 코드
    
    name = objRq.GetDataValue(1, i)  # 종목명
    diffflag = objRq.GetDataValue(3, i)
    diff = objRq.GetDataValue(4, i) # 대비
    diff_percent = objRq.GetDataValue(5, i) # 대비율(등락율)
    vol = objRq.GetDataValue(6, i)  # 거래량
    print(code, name, diffflag, diff, diff_percent, vol)


print()


# 하락종목
objRq = win32com.client.Dispatch("CpSysDib.CpSvrNew7043")
objRq.SetInputValue(0, ord('1')) # 거래소
objRq.SetInputValue(1, ord('4'))  # 상승 ,  4는 하락
objRq.SetInputValue(2, ord('1'))  # 당일
objRq.SetInputValue(3, 22)  # 전일 대비 상위 순 ,  22는 전일대비 하위순
objRq.SetInputValue(4, ord('1'))  # 관리 종목 제외
objRq.SetInputValue(5, ord('0'))  # 거래량 전체
objRq.SetInputValue(6, ord('0'))  # '표시 항목 선택 - '0': 시가대비
objRq.SetInputValue(7, '-30')  #  등락율 시작
objRq.SetInputValue(8, 0)  # 등락율 끝

objRq.BlockRequest();

# 하위 10종목
for i in range(10):
    code = objRq.GetDataValue(0, i)  # 코드
    
    name = objRq.GetDataValue(1, i)  # 종목명
    diffflag = objRq.GetDataValue(3, i)
    diff = objRq.GetDataValue(4, i) # 대비
    diff_percent = objRq.GetDataValue(5, i) # 대비율(등락율)
    vol = objRq.GetDataValue(6, i)  # 거래량
    print(code, name, diffflag, diff, diff_percent, vol)
