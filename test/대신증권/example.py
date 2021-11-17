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
nameToCode = inCpStockCode.NameToCode("금호석유")
print(codeToName)
print(nameToCode)

stock_name=['삼성전자','SK하이닉스','NAVER','카카오','삼성바이오로직스','LG화학','삼성SDI','현대차','기아','셀트리온','카카오뱅크',
'크래프톤','POSCO','KB금융','현대모비스','SK텔레콤','삼성물산','SK이노베이션','LG전자','신한지주','LG생활건강','엔씨소프트','SK바이오사이언스',
'SK','하이브','한국전력','LG','두산중공업','삼성생명','하나금융지주','삼성전기','삼성에스디에스','KT&G','넷마블','SK아이이테크놀로지','HMM',
'포스코케미칼','S-Oil','아모레퍼시픽','대한항공','삼성화재','우리금융지주','고려아연','기업은행','KT','SK바이오팜','한온시스템','LG디스플레이',
'롯데케미칼','한국조선해양','한화솔루션','SKC','LG유플러스','코웨이','강원랜드','현대글로비스','현대건설','CJ제일제당','LG이노텍','미래에셋증권',
'현대제철',',한국타이어앤테크놀로지','금호석유,','일진머티리얼즈','한국금융지주','현대중공업지주','두산밥캣','이마트','삼성엔지니어링','오리온','유한양행',
'삼성증권','아모레G','DB손해보험','쌍용C&E','한진칼','한솔케미칼','NH투자증권','한국가스공사','GS','삼성카드','한전기술','삼성중공업','한미사이언스','동서',
'GS건설','롯데지주','두산퓨얼셀','GS리테일','한미약품','에스원','호텔신라','메리츠증권','CJ대한통운','만도','롯데쇼핑','현대미포조선','한화생명','팬오션',
'한화시스템','BGF리테일','효성첨단소재','키움증권','OCI','BNK금융지주','CJ','KCC','녹십자','한국항공우주','SK케미칼','제일기획','DB하이텍','씨에스윈드',
'대우조선해양','효성티앤씨','DL이앤씨','신풍제약','대우건설','신세계','현대로템','하이트진로','한화','포스코인터내셔널','휠라홀딩스','현대해상','두산',
'코오롱인더','한화에어로스페이스','한전KPS','후성','현대위아','효성','한샘','롯데정밀화학','현대엘리베이','현대백화점','LS ELECTRIC','대웅','LS','영원무역',
'아시아나항공','한국앤컴퍼니','F&F홀딩스','농심','오뚜기','대한전선','HDC현대산업개발','동원시스템즈','동국제강','금호타이어','대웅제약','종근당','더블유게임즈',
'코스맥스','지누스','롯데관광개발','아이에스동서','영풍','SK네트웍스','녹십자홀딩스','롯데칠성','DL','이노션','화승엔터프라이즈','KG동부제철','신세계인터내셔날',
'CJ CGV','한올바이오파마','LX인터내셔널','태광산업','세방전지','대한유화','LIG넥스원','삼양홀딩스','오리온홀딩스','부광약품','영진약품','보령제약','현대그린푸드',
'동원산업','SK디스커버리','한섬','휴켐스','풍산','한세실업','GKL','한국콜마','쿠쿠홈시스','대상','넥센타이어','동원F&B','쿠쿠홀딩스','SNT모티브','현대홈쇼핑',
'현대두산인프라코어','LX홀딩스','LX하우시스','롯데하이마트','일양약품','삼양식품']


'''
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
instCpTd5331.SetInputValue(5, "N") # 도움말 default
#instCpTd5331.SetInputValue(5, "Y")
instCpTd5331.SetInputValue(6, ord("1")) # 도움말 default

instCpTd5331.BlockRequest()
Deposite = instCpTd5331.GetHeaderValue(45)
AvDeposite = instCpTd5331.GetHeaderValue(47)
현금주문가능금액 = instCpTd5331.GetHeaderValue(10)
현금주문 = instCpTd5331.GetHeaderValue(34)

print("예수금 = %d" % Deposite)
print("가용예수금 = %d" % AvDeposite)
print("현금주문가능금액 = %d" % 현금주문가능금액 )
print("현금주문 = %d" % 현금주문 )

'''
