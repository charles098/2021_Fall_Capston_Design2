import win32com.client

# 입력값 - 주식 이름

type_val = {"상한가" : 8, "하한가" : 9, "전일종가" : 10, "현재가" : 11, "전일대비" : 12,
"시가" : 13, "고가" : 14, "저가" : 15, "매도호가" : 16, "매수호가" : 17, "누적거래량" : 18, "누적거래대금" : 19,
"신고가" : 21, "신고가날짜" : 22, "신저가" : 23, "신저가날짜" : 24, "PER" : 28, "상장주식수" : 31, "전일거래량" : 46,
"1년최고가" : 47, "1년최고가날짜" : 48, "1년최저가" : 49, "1년최저가날짜" : 50, "종가" : 11}

# - 특이사항
# 신저가일 -> 신저가1로 인식해서 '일'을 '날짜'로 수정. 즉, '신저가날짜'로 말해줘야 한다

def stockInfo(code : str, type : str):
    inStockMst = win32com.client.Dispatch("dscbo1.StockMst")
    inStockMst.SetInputValue(0, code)   
    inStockMst.BlockRequest()

    result = inStockMst.GetHeaderValue(type_val[type])    
    #print(result)
    #result = N2K.digit2txt(str(result))
    #print("{type} = {value}".format(type = type, value = result))
    
    date = [22, 24, 48, 50] # 날짜
    others = [18, 46] # ~주 입니다
    if result < 0:
        # 음수는 마이너스 붙여준다
        if type_val[type] == 28:
            return '마이너스' + str(result)
        elif type_val[type] == 12:
            return '마이너스' + str(result) + '원, 입니다.'
    elif type_val[type] in date:
        result = str(int(result))
        year = result[:4]
        month = result[4:6]
        day = result[6:]
        return year + '년,' + month + '월,' + day + '일, '
    elif type_val[type] in others:
        return str(result) + '주, 입니다.'
    else:
        return str(result) + '원, 입니다.'

# (숫자).is_integer() 를 사용하면 소수가 정수인지 판별 가능

def est_rank(high_low: int, cnt: int):
    # high_low = 1이면 high, 0이면 low

    objRq = win32com.client.Dispatch("CpSysDib.CpSvrNew7043")
    objRq.SetInputValue(0, ord('1')) # 거래소

    if high_low == 1: 
        objRq.SetInputValue(1, ord('2'))  # 상승
        objRq.SetInputValue(3, 21)  # 전일 대비 상위 순 ,  22는 전일대비 하위순
        objRq.SetInputValue(7, 0)  #  등락율 시작
        objRq.SetInputValue(8, 30)  # 등락율 끝
    else: 
        objRq.SetInputValue(1, ord('4'))  # 하락
        objRq.SetInputValue(3, 22)  # 전일 대비 상위 순 ,  22는 전일대비 하위순
        objRq.SetInputValue(7, '-30')  #  등락율 시작
        objRq.SetInputValue(8, 0)  # 등락율 끝

    objRq.SetInputValue(2, ord('1'))  # 당일
    objRq.SetInputValue(4, ord('1'))  # 관리 종목 제외
    objRq.SetInputValue(5, ord('0'))  # 거래량 전체
    objRq.SetInputValue(6, ord('0'))  # '표시 항목 선택 - '0': 시가대비

    objRq.BlockRequest();

    result = ''

    for i in range(cnt):
        #code = objRq.GetDataValue(0, i)  # 코드
        name = objRq.GetDataValue(1, i)  # 종목명
        #diffflag = objRq.GetDataValue(3, i)
        #diff = objRq.GetDataValue(4, i) # 대비
        diff_percent = objRq.GetDataValue(5, i) # 대비율(등락율)
        vol = objRq.GetDataValue(6, i)  # 거래량

        if high_low == 1:
            result += '종목명, ' + name + ', 등락율, ' + str(round(diff_percent,2)) + '%, 거래량, ' + str(vol) + ',\n'
        else:
            result += '종목명, ' + name + ', 등락율, 마이너스 ' + str(-1 * round(diff_percent,2)) + '%, 거래량, ' + str(vol) + ',\n'
        
    return result

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