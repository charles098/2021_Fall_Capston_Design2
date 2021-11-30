import MeCab 
###### 자바스크립트에서 한글 깨짐 현상 방지용 ################################
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
###########################################################################


m = MeCab.Tagger() 


#corp = m.parse("종근당고려아연에스오일카카오네이버주식회사삼성전자.")
#corp = m.parse('삼성전자sk하이닉스네이버카카오삼성바이오로직스lg화학삼성sdi현대차기아셀트리온카카오뱅크크래프톤포스코kb금융현대모비스sk텔레콤삼성물산sk이노베이션lg전자신한지주')
#corp = m.parse(sys.argv[1]);
corp = m.parse('sk하이닉스3차차매도호가에2개매도')

# 품사 태깅
#for word in corp.split('\n'):
#    print(word.split(',')[0].split('\t'))


tags = ''
for word in corp.split('\n')[:-2]:
    tmp = word.split(',')[0].split('\t')
    tags = tags + tmp[0] + ' ' + tmp[1] + ' '

tags = tags.strip() # 앞뒤 공백 먼저 제거 

tags_list = tags.split()

# {태그 : 단어} 사전 생성
tag_word = {}
for i in range(int(len(tags_list) / 2)):
    # 2 * i 인덱스 원소는 단어
    # 2 * i + 1 인덱스 원소는 태그
    tag_word[tags_list[2 * i + 1]] = tags_list[2 * i]
print(tags_list.count('SN'))
print(tag_word)