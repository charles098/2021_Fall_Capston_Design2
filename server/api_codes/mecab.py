import MeCab 
###### 자바스크립트에서 한글 깨짐 현상 방지용 ################################
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
###########################################################################


m = MeCab.Tagger() 

corp = m.parse(sys.argv[1]);


# 넘어갈때 문자열로 넘어가기 때문에 공백으로 분리해준다
# 품사 태깅
sentence = ''
for word in corp.split('\n')[:-2]:
    tmp = word.split(',')[0].split('\t')
    sentence = sentence + tmp[0] + ' ' + tmp[1] + ' '

print(sentence)
