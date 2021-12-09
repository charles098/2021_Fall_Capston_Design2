import win32com.client
import num_to_Korean as N2K

# 입력값 - 주식 이름

type_val = {"상한가" : 8, "하한가" : 9, "전일종가" : 10, "현재가" : 11, "전일대비" : 12,
"시가" : 13, "고가" : 14, "국가": 14, "저가" : 15, "매도호가" : 16, "매수호가" : 17, "누적거래량" : 18, "누적거래대금" : 19,
"신고가" : 21, "신고가일" : 22, "신저가" : 23, "신저가일" : 24, "PER" : 28, "상장주식수" : 31, "전일거래량" : 46,
"일년최고가" : 47, "일년최고가일" : 48, "일년최저가" : 49, "일년최저가일" : 50, "종가" : 11}

# (전일종가 - 현재가) / 전일종가

def stockInfo(code : str, type : str):
    inStockMst = win32com.client.Dispatch("dscbo1.StockMst")
    inStockMst.SetInputValue(0, code)   
    inStockMst.BlockRequest()

    result = inStockMst.GetHeaderValue(type_val[type])    
    print(result)
    result = N2K.digit2txt(str(result))
    print("{type} = {value}".format(type = type, value = result))

# (숫자).is_integer() 를 사용하면 소수가 정수인지 판별 가능

inStockMst = win32com.client.Dispatch("dscbo1.StockMst")
inStockMst.SetInputValue(0, 'A035720')   
inStockMst.BlockRequest()

#전일종가 = inStockMst.GetHeaderValue(10)    
전일대비 = inStockMst.GetHeaderValue(11)    
#print((전일종가 - 현재가) / 전일종가)
#print(전일종가)
print(전일대비)

'''
inStockMst = win32com.client.Dispatch("dscbo1.StockMst")
inStockMst.SetInputValue(0, "A005930")   
inStockMst.BlockRequest()

종목코드 = inStockMst.GetHeaderValue(0) #string
종목명 = inStockMst.GetHeaderValue(1) # string
상한가 = inStockMst.GetHeaderValue(8)
하한가 = inStockMst.GetHeaderValue(9)
전일종가 = inStockMst.GetHeaderValue(10)
현재가 = inStockMst.GetHeaderValue(11)
전일대비 = inStockMst.GetHeaderValue(12)
시가 = inStockMst.GetHeaderValue(13)
고가 = inStockMst.GetHeaderValue(14)
저가 = inStockMst.GetHeaderValue(15)
매도호가 = inStockMst.GetHeaderValue(16)
매수호가 = inStockMst.GetHeaderValue(17)
누적거래량 = inStockMst.GetHeaderValue(18)
누적거래대금 = inStockMst.GetHeaderValue(19)
신고가 = inStockMst.GetHeaderValue(21)
신고가일 = inStockMst.GetHeaderValue(22)
신저가 = inStockMst.GetHeaderValue(23)
신저가일 = inStockMst.GetHeaderValue(24)
PER = inStockMst.GetHeaderValue(28)
상장주식수 = inStockMst.GetHeaderValue(31) # string
전일거래량 = inStockMst.GetHeaderValue(46)
일년최고가 = inStockMst.GetHeaderValue(47)
일년최고가일 = inStockMst.GetHeaderValue(48)
일년최저가 = inStockMst.GetHeaderValue(49)
일년최저가일 = inStockMst.GetHeaderValue(50)

print("종목코드= %s" % 종목코드)
print("종목명 = %s" % 종목명)
print("상한가 = %f" %  상한가)
print("하한가 = %f" % 하한가)
print("전일종가 = %f" % 전일종가)
print("현재가 = %f" % 현재가)
print("전일대비 = %f" % 전일대비)
print("시가 = %f" % 시가)
print("고가 = %f" % 고가)
print("저가 = %f" % 저가)
print("매도호가 = %f" % 매도호가)
print("매수호가 = %f" % 매수호가)
print("누적거래량 = %f" % 누적거래량)
print("누적거래대금 = %f" % 누적거래대금)
print("신고가 = %f" % 신고가)
print("신고가일 = %f" % 신고가일)
print("신저가 = %f" % 신저가)
print("신저가일 = %f" % 신저가일)
print("PER = %f" % PER)
print("상장주식수 = %s" % 상장주식수)
print("전일거래량 = %f" % 전일거래량)
print("52주 최고가 = %f" % 일년최고가)
print("52주 최고가일 = %f" % 일년최고가일)
print("52주 최저가 = %f" % 일년최저가)
print("52주 최저가일 = %f" % 일년최저가일)

# (숫자).is_integer() 를 사용하면 소수가 정수인지 판별 가능
'''