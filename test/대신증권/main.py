
# 전처리 진행
# 1. 입력값 주식명을 주식코드로 바꿔줌
# 2. 명령에 맞는 함수 호출해줌

# 입력값 형식 function()

import 예수금_주문가능금액 as Deposit_orderableAccount
import 매수_매도 as Buy_or_sell
import 계좌번호 as AccountNum
import 주식정보 as StockInfo
import Stock_Code as s2c  # s2c.stock_code -> {주식이름 : 주식코드} 사전

#AccountNum.accountNumber() # 계좌번호

#Deposit_orderableAccount.deposit() # 예수금
#Deposit_orderableAccount.orderable_account() # 주문가능금액

#Buy_or_sell.buy("A003540", 10, 14100) # 매수 (종목코드, 수량, 가격)
#Buy_or_sell.sell("A003540", 10, 14100) # 매도 (종목코드, 수량, 가격)


# StockInfo.stockInfo("A005930", "상한가")
# 상한가, 하한가, 전일종가, 현재가, 전일대비, 시가, 고가, 저가, 매도호가, 매수호가, 누적거래량, 누적거래대금
# 신고가, 신고가일, 신저가, 신저가일, PER, 상장주식수, 전일거래량, 일년최고가, 일년최고가일, 일년최저가, 일년최저가일