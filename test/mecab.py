import MeCab 
###### 자바스크립트에서 한글 깨짐 현상 방지용 ################################
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
###########################################################################


m = MeCab.Tagger() 


#corp = m.parse("종근당고려아연에스오일카카오네이버주식회사삼성전자.")
corp = m.parse(sys.argv[1]);

# 품사 태깅
for word in corp.split('\n'):
    print(word.split(',')[0].split('\t'))

