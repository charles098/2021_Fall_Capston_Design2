import win32com.client
import time
 
def not_executed(flag: int, stock_code : str):
    # flag == 1 : 취소 내역 조회
    # flag == 2 : 단일 주문 취소, code 존재
    # flag == 3 : 주문 전체 취소

    objRq = win32com.client.Dispatch("CpTrade.CpTd5339")
    g_objCpTrade = win32com.client.Dispatch("CpTrade.CpTdUtil")
    objCancelOrder = win32com.client.Dispatch("CpTrade.CpTd0314")  # 취소
    g_objCpStatus = win32com.client.Dispatch("CpUtil.CpCybos")

    g_objCpTrade.TradeInit(0)

    acc = g_objCpTrade.AccountNumber[0]  # 계좌번호
    accFlag = g_objCpTrade.GoodsList(acc, 1)  # 주식상품 구분

    objRq.SetInputValue(0, acc)
    objRq.SetInputValue(1, accFlag[0])
    objRq.SetInputValue(4, "0") # 전체
    objRq.SetInputValue(5, "1") # 정렬 기준 - 역순
    objRq.SetInputValue(6, "0") # 전체
    objRq.SetInputValue(7, 20) # 요청 개수 - 최대 20개

    cancel_dic = {}
    cancel_idx = 0
    result = ''

    # 미체결 연속 조회를 위해 while 문 사용
    while True :
        ret = objRq.BlockRequest()
        if objRq.GetDibStatus() != 0:
            return str(objRq.GetDibMsg1())

        if (ret == 2 or ret == 3):
            return "통신 오류" + str(ret)

        # 통신 초과 요청 방지에 의한 요류 인 경우
        while (ret == 4) : # 연속 주문 오류 임. 이 경우는 남은 시간동안 반드시 대기해야 함.
            remainTime = g_objCpStatus.LimitRequestRemainTime
            #print("연속 통신 초과에 의해 재 통신처리 : ",remainTime/1000, "초 대기" )
            time.sleep(remainTime / 1000)
            ret = objRq.BlockRequest()


        # 수신 개수
        cnt = objRq.GetHeaderValue(5)
        cancel_idx = cnt
        #print("[Cp5339] 수신 개수 ", cnt)
        if cnt == 0 :
            break
        
        for i in range(cnt):
            orderNum = str(objRq.GetDataValue(1, i))
            #orderPrev  = objRq.GetDataValue(2, i)
            code  = objRq.GetDataValue(3, i)  # 종목코드
            name  = objRq.GetDataValue(4, i)  # 종목명
            #orderDesc  = objRq.GetDataValue(5, i)  # 주문구분내용
            amount  = str(objRq.GetDataValue(6, i))  # 주문수량
            price  = str(objRq.GetDataValue(7, i))  # 주문단가
            ContAmount = str(objRq.GetDataValue(8, i))  # 체결수량
            #credit  = objRq.GetDataValue(9, i)  # 신용구분
            modAvali  = objRq.GetDataValue(11, i)  # 정정취소 가능수량
            buysell  = objRq.GetDataValue(13, i)  # 매매구분코드
            if buysell == '1': buysell = '매도'
            else: buysell = '매수'
            #creditdate  = objRq.GetDataValue(17, i)  # 대출일
            #orderFlagDesc  = str(objRq.GetDataValue(19, i))  # 주문호가구분코드내용
            #orderFlag  = objRq.GetDataValue(21, i)  # 주문호가구분코드
            
            if flag == 2 and stock_code == code: 
                cancel_dic['orderNum'] = orderNum
                cancel_dic['modAvali'] = modAvali
                cancel_dic['code'] = code
            
            if flag == 3:
                cancel_dic[i] = []
                cancel_dic[i].append(orderNum)
                cancel_dic[i].append(code)
                cancel_dic[i].append(modAvali)

            result += '종목명, ' + name + ', 주문수량, ' + amount + '개, 미체결수량, ' + str(int(amount) - int(ContAmount))
            result += '개, 주문단가, ' + price + '원, 매수매도, ' + buysell + ',\n'

        # 연속 처리 체크 - 다음 데이터가 없으면 중지
        if objRq.Continue == False :
            #print("[Cp5339] 연속 조회 여부: 다음 데이터가 없음")
            break
    
    if flag == 1: 
        if result == '':
            return "미체결된 내역이 존재하지 않습니다."
        return result
    
    if flag == 2:
        if len(cancel_dic) == 0: 
            return "해당 주식을 보유하고 있지 않습니다"
        objCancelOrder.SetInputValue(1, cancel_dic["orderNum"])  # 원주문 번호 - 정정을 하려는 주문 번호
        objCancelOrder.SetInputValue(2, acc)  # 상품구분 - 주식 상품 중 첫번째
        objCancelOrder.SetInputValue(3, accFlag[0])  # 상품구분 - 주식 상품 중 첫번째
        objCancelOrder.SetInputValue(4, cancel_dic["code"])  # 종목코드
        objCancelOrder.SetInputValue(5, cancel_dic["modAvali"])  # 정정 수량, 0 이면 잔량 취소임
        #print(cancel_dic["orderNum"], cancel_dic["code"], cancel_dic["modAvali"])
        
        ret = 0
        while True:
            ret = objCancelOrder.BlockRequest()
            if ret == 0:
                break;
            #print("[CpRPOrder/RequestCancel] 주문 요청 실패 ret : ", ret)
            if ret == 4:
                remainTime = g_objCpStatus.LimitRequestRemainTime
                print("연속 통신 초과에 의해 재 통신처리 : ", remainTime / 1000, "초 대기")
                time.sleep(remainTime / 1000)
                continue
            else:   # 1 통신 요청 실패 3 그 외의 오류 4: 주문요청제한 개수 초과
                #print('취소')
                break;
        return str(objCancelOrder.GetDibMsg1())    
        #return "주문 취소 완료"

    if flag == 3:
        # 주식 취소 주문
        if cancel_idx == 0:
            return "미체결된 내역이 존재하지 않습니다."
        for i in range(cancel_idx):
            objCancelOrder.SetInputValue(1, cancel_dic[i][0])  # 원주문 번호 - 정정을 하려는 주문 번호
            objCancelOrder.SetInputValue(2, acc)  # 상품구분 - 주식 상품 중 첫번째
            objCancelOrder.SetInputValue(3, accFlag[0])  # 상품구분 - 주식 상품 중 첫번째
            objCancelOrder.SetInputValue(4, cancel_dic[i][1])  # 종목코드
            objCancelOrder.SetInputValue(5, cancel_dic[i][2])  # 정정 수량, 0 이면 잔량 취소임
            #print(cancel_dic[i][0], cancel_dic[i][1], cancel_dic[i][2])
            # 취소주문 요청
            ret = 0
            while True:
                ret = objCancelOrder.BlockRequest()
                if ret == 0:
                    break;
                #print("[CpRPOrder/RequestCancel] 주문 요청 실패 ret : ", ret)
                if ret == 4:
                    remainTime = g_objCpStatus.LimitRequestRemainTime
                    #print("연속 통신 초과에 의해 재 통신처리 : ", remainTime / 1000, "초 대기")
                    time.sleep(remainTime / 1000)
                    continue
                else:   # 1 통신 요청 실패 3 그 외의 오류 4: 주문요청제한 개수 초과
                    #print('취소')
                    break;
            #print(objCancelOrder.GetDibStatus(), objCancelOrder.GetDibMsg1())
        return str(objCancelOrder.GetDibMsg1())
        #return "전종목 주문 취소 완료"