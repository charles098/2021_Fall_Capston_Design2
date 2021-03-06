# mecab의 STOCK 태그를 종목코드로 변환 
mecab_to_code = { 
'삼성전자': 'A005930',
 'sk하이닉스': 'A000660',
 '네이버': 'A035420',
 '카카오': 'A035720',
 '삼성바이오로직스': 'A207940',
 'lg화학': 'A051910',
 '삼성sdi': 'A006400',
 '현대차': 'A005380',
 '기아': 'A000270',
 '셀트리온': 'A068270',
 '카카오뱅크': 'A323410',
 '크래프톤': 'A259960',
 '포스코': 'A005490',
 'kb금융': 'A105560',
 '현대모비스': 'A012330',
 'sk텔레콤': 'A017670',
 '삼성물산': 'A028260',
 'sk이노베이션': 'A096770',
 'lg전자': 'A066570',
 '신한지주': 'A055550',
 '엘지생활건강': 'A051900',
 '엔씨소프트': 'A036570',
 'sk바이오사이언스': 'A302440',
 'sk': 'A034730',
 '하이브': 'A352820',
 '한국전력': 'A015760',
 'lg': 'A003550',
 '두산중공업': 'A034020',
 '삼성생명': 'A032830',
 '하나금융지주': 'A086790',
 '삼성전기': 'A009150',
 '삼성sds': 'A018260',
 '케이티앤지': 'A033780',
 '넷마블': 'A251270',
 'sk아이이테크놀로지': 'A361610',
 'hmm': 'A011200',
 '포스코 케미칼': 'A003670',
 's-oil': 'A010950',
 '아모레퍼시픽': 'A090430',
 '대한항공': 'A003490',
 '삼성화재': 'A000810',
 '우리금융지주': 'A316140',
 '고려아연': 'A010130',
 '기업은행': 'A024110',
 'kt': 'A030200',
 'sk바이오팜': 'A326030',
 '한온시스템': 'A018880',
 'lg디스플레이': 'A034220',
 '롯데케미칼': 'A011170',
 '한국조선 해양': 'A009540',
 '한화솔루션': 'A009830',
 'skc': 'A011790',
 'lg유플러스': 'A032640',
 '코웨이': 'A021240',
 '강원랜드': 'A035250',
 '현대글로비스': 'A086280',
 '현대건설': 'A000720',
 'cj제일제당': 'A097950',
 'lg이노텍': 'A011070',
 '미레에셋증권': 'A006800',
 '현대제철': 'A004020',
 '한국타이어앤테크놀로지': 'A161390',
 '금호석유': 'A011780',
 '일진머티리얼즈': 'A020150',
 '한국금융지주': 'A071050',
 '현대중공업지주': 'A267250',
 '두산밥캣': 'A241560',
 '이마트': 'A139480',
 '삼성엔지니어링': 'A028050',
 '오리온': 'A271560',
 '유한양행': 'A000100',
 '삼성증권': 'A016360',
 '아모레g': 'A002790',
 'db손해보험': 'A005830',
 '쌍용씨앤비': 'A003410',
 '한진칼': 'A180640',
 '한솔케미칼': 'A014680',
 'nh투자증권': 'A005940',
 '한국가스공사': 'A036460',
 'gs': 'A078930',
 '삼성카드': 'A029780',
 '한전기술': 'A052690',
 '삼성중공업': 'A010140',
 '한미사이언스': 'A008930',
 '동서': 'A026960',
 'gs건설': 'A006360',
 '롯데지주': 'A004990',
 '두산퓨얼셀': 'A336260',
 'gs리테일': 'A007070',
 '한미약품': 'A128940',
 's1': 'A012750',
 '호텔신라': 'A008770',
 '메리츠증권': 'A008560',
 'cj대한통운': 'A000120',
 '만도': 'A204320',
 '롯데쇼핑': 'A023530',
 '현대미포조선': 'A010620',
 '한화 생명': 'A088350',
 '팬오션': 'A028670',
 '한화시스템': 'A272210',
 'bgf리테일': 'A282330',
 '효성첨단소재': 'A298050',
 '키움증권': 'A039490',
 'oci': 'A010060',
 'bnk금융지주': 'A138930',
 'cj': 'A001040',
 'kcc': 'A002380',
 '녹십자': 'A006280',
 '한국항공우주': 'A047810',
 'sk케미칼': 'A285130',
 '제일기획': 'A030000',
 'db하이텍': 'A000990',
 '씨에스윈드': 'A112610',
 '대우조선해양': 'A042660',
 '효성티앤씨': 'A298020',
 'dl 이엔씨': 'A375500',
 '신풍제약': 'A019170',
 '대우건설': 'A047040',
 '신세계': 'A004170',
 '현대로템': 'A064350',
 '하이트진로': 'A000080',
 '한화': 'A000880',
 '포스코인터내셔널': 'A047050',
 '휠라홀딩스': 'A081660',
 '현대해상': 'A001450',
 '두산': 'A000150',
 '코오롱인더': 'A120110',
 '한화에어로스페이스': 'A012450',
 '한전kps': 'A051600',
 '후성': 'A093370',
 '현대위아': 'A011210',
 '효성': 'A004800',
 '한샘': 'A009240',
 '롯데정밀화학': 'A004000',
 '현대엘리베이': 'A017800',
 '현대백화점': 'A069960',
 'lselectric': 'A010120',
 '대웅': 'A003090',
 'ls': 'A006260',
 '영원무역': 'A111770',
 '아시아나항공': 'A020560',
 '한국엔컴퍼니': 'A000240',
 '에프앤에스홀딩스': 'A007700',
 '농심': 'A004370',
 '오뚜기': 'A007310',
 '대한전선': 'A001440',
 'hdc현대산업개발': 'A294870',
 '동원시스템즈': 'A014820',
 '동국제강': 'A001230',
 '금호타이어': 'A073240',
 '대웅제약': 'A069620',
 '종근당': 'A185750',
 '더블유게임즈': 'A192080',
 '코스맥스': 'A192820',
 '지누스': 'A013890',
 '롯데관광개발': 'A032350',
 '아이에스동서': 'A010780',
 '영풍': 'A000670',
 'sk네트웍스': 'A001740',
 '녹십자홀딩스': 'A005250',
 '롯데칠성': 'A005300',
 'dl': 'A000210',
 '이노션': 'A214320',
 '화승엔터프라이즈': 'A241590',
 'kg동부제철': 'A016380',
 '신세계인터내셔날': 'A031430',
 'cjcgv': 'A079160',
 '한올바이오파마': 'A009420',
 'lx인터내셔널': 'A001120',
 '태광산업': 'A003240',
 '세방전지': 'A004490',
 '대한유화': 'A006650',
 'lig넥스원': 'A079550',
 '삼양홀딩스': 'A000070',
 '오리온홀딩스': 'A001800',
 '부광약품': 'A003000',
 '영진약품': 'A003520',
 '보령제약': 'A003850',
 '현대그린푸드': 'A005440',
 '동원산업': 'A006040',
 'sk디스커버리': 'A006120',
 '한섬': 'A020000',
 '휴켐스': 'A069260',
 '풍산': 'A103140',
 '한세실업': 'A105630',
 'gkl': 'A114090',
 '한국콜마': 'A161890',
 '쿠쿠홈시스': 'A284740',
 '대상': 'A001680',
 '넥센타이어': 'A002350',
 '동원에프앤비': 'A049770',
 '쿠쿠홀딩스': 'A192400',
 'snt모티브': 'A064960',
 '현대홈쇼핑': 'A057050',
 '현대두산인프라코어': 'A042670',
 'lx홀딩스': 'A383800',
 'lx하우시스': 'A108670',
 '롯데하이마트': 'A071840',
 '일양약품': 'A007570',
 '삼양식품': 'A003230'}


'''
녹음된 이름. mecab의 output, 토큰은 STOCK

record = [
'삼성전자', 'sk하이닉스', '네이버', '카카오', '삼성바이오로직스',
'lg화학', '삼성sdi', '현대차', '기아', '셀트리온', '카카오뱅크',
'크래프톤', '포스코', 'kb금융', '현대모비스', 'sk텔레콤', '삼성물산', 
'sk이노베이션', 'lg전자', '신한지주', '엘지생활건강','엔씨소프트',
'sk바이오사이언스', 'sk', '하이브', '한국전력', 'lg', '두산중공업', 
'삼성생명', '하나금융지주', '삼성전기', '삼성sds', '케이티앤지', '넷마블',
'sk아이이테크놀로지', 'hmm', '포스코 케미칼', 's-oil', '아모레퍼시픽', 
'대한항공','삼성화재', '우리금융지주', '고려아연', '기업은행', 'kt', 
'sk바이오팜', '한온시스템', 'lg디스플레이', '롯데케미칼', '한국조선 해양',
'한화솔루션', 'skc', 'lg유플러스', '코웨이', '강원랜드', '현대글로비스', 
'현대건설', 'cj제일제당', 'lg이노텍', '미레에셋증권','현대제철', 
'한국타이어앤테크놀로지', '금호석유', '일진머티리얼즈', '한국금융지주', 
'현대중공업지주', '두산밥캣','이마트','삼성엔지니어링', '오리온', 
'유한양행', '삼성증권', '아모레g', 'db손해보험', '쌍용씨앤비', 
'한진칼', '한솔케미칼', 'nh투자증권',
'한국가스공사', 'gs','삼성카드', '한전기술', '삼성중공업', '한미사이언스', 
'동서', 'gs건설', '롯데지주', '두산퓨얼셀', 'gs리테일', '한미약품',
's1', '호텔신라', '메리츠증권', 'cj대한통운', '만도', '롯데쇼핑', 
'현대미포조선', '한화 생명', '팬오션', '한화시스템','bgf리테일', 
'효성첨단소재', '키움증권', 'oci', 'bnk금융지주', 'cj', 'kcc', 
'녹십자', '한국항공우주', 'sk케미칼','제일기획', 'db하이텍', '씨에스윈드', 
'대우조선해양', '효성티앤씨', 'dl 이엔씨', '신풍제약', '대우건설', '신세계', 
'현대로템', '하이트진로', '한화','포스코인터내셔널', 
'휠라홀딩스', '현대해상','두산', '코오롱인더','한화에어로스페이스', 
'한전kps', '후성', '현대위아', '효성', '한샘', '롯데정밀화학',
'현대엘리베이', '현대백화점', 'lselectric', '대웅', 'ls', '영원무역',
'아시아나항공', '한국엔컴퍼니', '에프앤에스홀딩스', '농심', '오뚜기', 
'대한전선','hdc현대산업개발', '동원시스템즈', '동국제강', '금호타이어', 
'대웅제약', '종근당', '더블유게임즈', '코스맥스', '지누스', '롯데관광개발', 
'아이에스동서', '영풍','sk네트웍스', '녹십자홀딩스','롯데칠성', 'dl', 
'이노션' ,'화승엔터프라이즈','kg동부제철', '신세계인터내셔날', 
'cjcgv', '한올바이오파마', 'lx인터내셔널','태광산업', '세방전지',
'대한유화', 'lig넥스원', '삼양홀딩스', '오리온홀딩스', '부광약품', 
'영진약품', '보령제약', '현대그린푸드', '동원산업','sk디스커버리',
'한섬', '휴켐스', '풍산', '한세실업', 'gkl', '한국콜마', '쿠쿠홈시스',
'대상', '넥센타이어','동원에프앤비', '쿠쿠홀딩스', 'snt모티브',
'현대홈쇼핑', '현대두산인프라코어','lx홀딩스', 'lx하우시스', 
'롯데하이마트', '일양약품', '삼양식품']
'''

''' 
주식명, 코드 원본 
stock_code = {
'삼성전자': 'A005930', 
'SK하이닉스': 'A000660', 
'NAVER': 'A035420', 
'카카오': 'A035720', 
'삼성바이오로직스': 'A207940', 
'LG화학': 'A051910', 
'삼성SDI': 'A006400', 
'현대차': 'A005380', 
'기아': 'A000270',
'셀트리온': 'A068270', 
'카카오뱅크': 'A323410', 
'크래프톤': 'A259960', 
'POSCO': 'A005490', 
'KB금융': 'A105560', 
'현대모비스': 'A012330', 
'SK텔레콤': 'A017670', 
'삼성물산': 'A028260', 
'SK이노베이션': 'A096770',
'LG전자': 'A066570', 
'신한지주': 'A055550', 
'LG생활건강': 'A051900', 
'엔씨소프트': 'A036570', 
'SK바이오사이언스': 'A302440', 
'SK': 'A034730', 
'하이브': 'A352820', 
'한국전력': 'A015760', 
'LG': 'A003550', 
'두산중공업': 'A034020', 
'삼성생명': 'A032830', 
'하나금융지주': 'A086790', 
'삼성전기': 'A009150', 
'삼성에스디에스': 'A018260', 
'KT&G': 'A033780', 
'넷마블': 'A251270', 
'SK아이이테크놀로지': 'A361610', 
'HMM': 'A011200', 
'포스코케미칼': 'A003670', 
'S-Oil': 'A010950', 
'아모레퍼시픽': 'A090430', 
'대한항공': 'A003490', 
'삼성화재': 'A000810', 
'우리금융지주': 'A316140', 
'고려아연': 'A010130', 
'기업은행': 'A024110', 
'KT': 'A030200', 
'SK바이오팜': 'A326030', 
'한온시스템': 'A018880', 
'LG디스플레이': 'A034220', 
'롯데케미칼': 'A011170', 
'한국조선해양': 'A009540', 
'한화솔루션': 'A009830', 
'SKC': 'A011790', 
'LG유플러스': 'A032640', 
'코웨이': 'A021240', 
'강원랜드': 'A035250', 
'현대글로비스': 'A086280', 
'현대건설': 'A000720', 
'CJ제일제당': 'A097950', 
'LG이노텍': 'A011070', 
'미래에셋증권': 'A006800', 
'현대제철': 'A004020', 
'한국타이어앤테크놀로지': 'A161390', 
'금호석유,': 'A011780', 
'일진머티리얼즈': 'A020150', 
'한국금융지주': 'A071050', 
'현대중공업지주': 'A267250', 
'두산밥캣': 'A241560', 
'이마트': 'A139480', 
'삼성엔지니어링': 'A028050', 
'오리온': 'A271560', 
'유한양행': 'A000100', 
'삼성증권': 'A016360', 
'아모레G': 'A002790', 
'DB손해보험': 'A005830', 
'쌍용C&E': 'A003410', 
'한진칼': 'A180640', 
'한솔케미칼': 'A014680', 
'NH투자증권': 'A005940', 
'한국가스공사': 'A036460', 
'GS': 'A078930', 
'삼성카드': 'A029780', 
'한전기술': 'A052690', 
'삼성중공업': 'A010140', 
'한미사이언스': 'A008930', 
'동서': 'A026960', 
'GS건설': 'A006360', 
'롯데지주': 'A004990', 
'두산퓨얼셀': 'A336260', 
'GS리테일': 'A007070', 
'한미약품': 'A128940', 
'에스원': 'A012750', 
'호텔신라': 'A008770', 
'메리츠증권': 'A008560', 
'CJ대한통운': 'A000120', 
'만도': 'A204320', 
'롯데쇼핑': 'A023530', 
'현대미포조선': 'A010620', 
'한화생명': 'A088350', 
'팬오션': 'A028670', 
'한화시스템': 'A272210',
'BGF리테일': 'A282330', 
'효성첨단소재': 'A298050', 
'키움증권': 'A039490', 
'OCI': 'A010060', 
'BNK금융지주': 'A138930',
'CJ': 'A001040',
'KCC': 'A002380', 
'녹십자': 'A006280', 
'한국항공우주': 'A047810',
'SK케미칼': 'A285130',
'제일기획': 'A030000',
'DB하이텍': 'A000990',
'씨에스윈드': 'A112610',
'대우조선해양': 'A042660',
'효성티앤씨': 'A298020',
'DL이앤씨': 'A375500',
'신풍제약': 'A019170',
'대우건설': 'A047040',
'신세계': 'A004170',
'현대로템': 'A064350',
'하이트진로': 'A000080',
'한화': 'A000880', 
'포스코인터내셔널': 'A047050', 
'휠라홀딩스': 'A081660', 
'현대해상': 'A001450', 
'두산': 'A000150', 
'코오롱인더': 'A120110',
'한화에어로스페이스': 'A012450',
'한전KPS': 'A051600',
'후성': 'A093370',
'현대위아': 'A011210',
'효성': 'A004800',
'한샘': 'A009240',
'롯데정밀화학': 'A004000',
'현대엘리베이': 'A017800',
'현대백화점': 'A069960',
'LS ELECTRIC': 'A010120',
'대웅': 'A003090',
'LS': 'A006260', 
'영원무역': 'A111770', 
'아시아나항공': 'A020560', 
'한국앤컴퍼니': 'A000240', 
'F&F홀딩스': 'A007700', 
'농심': 'A004370', 
'오뚜기': 'A007310', 
'대한전선': 'A001440', 
'HDC현대산업개발': 'A294870', 
'동원시스템즈': 'A014820', 
'동국제강': 'A001230', 
'금호타이어': 'A073240', 
'대웅제약': 'A069620', 
'종근당': 'A185750', 
'더블유게임즈': 'A192080', 
'코스맥스': 'A192820', 
'지누스': 'A013890', 
'롯데관광개발': 'A032350', 
'아이에스동서': 'A010780', 
'영풍': 'A000670', 
'SK네트웍스': 'A001740', 
'녹십자홀딩스': 'A005250', 
'롯데칠성': 'A005300', 
'DL': 'A000210', 
'이노션': 'A214320', 
'화승엔터프라이즈': 'A241590',
'KG동부제철': 'A016380', 
'신세계인터내셔날': 'A031430', 
'CJ CGV': 'A079160', 
'한올바이오파마': 'A009420', 
'LX 인터내셔널': 'A001120', 
'태광산업': 'A003240', 
'세방전지': 'A004490', 
'대한유화': 'A006650', 
'LIG넥스원': 'A079550', 
'삼양홀딩스': 'A000070', 
'오리온홀딩스': 'A001800', 
'부광약품': 'A003000', 
'영진약품': 'A003520', 
'보령제약': 'A003850', 
'현대그린푸드': 'A005440', 
'동원산업': 'A006040', 
'SK디스커버리': 'A006120', 
'한섬': 'A020000', 
'휴켐스': 'A069260', 
'풍산': 'A103140', 
'한세실업': 'A105630', 
'GKL': 'A114090', 
'한국콜마': 'A161890', 
'쿠쿠홈시스': 'A284740', 
'대상': 'A001680', 
'넥센타이어': 'A002350', 
'동원F&B': 'A049770', 
'쿠쿠홀딩스': 'A192400', 
'SNT모티브': 'A064960', 
'현대홈쇼핑': 'A057050', 
'현대두산인프라코어': 'A042670', 
'LX홀딩스': 'A383800', 
'LX하우시스': 'A108670', 
'롯데하이마트': 'A071840', 
'일양약품': 'A007570', 
'삼양식품': 'A003230'}
'''
