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

sentence = sentence.replace('한계 매수', '한개 매수') # 한개를 계속 한계로 인식해서 있으면 바꿔줌
sentence = sentence.replace('한계 매도', '한개 매도') # 한개를 계속 한계로 인식해서 있으면 바꿔줌
sentence = sentence.replace('오차 매도호가', '5차 매도호가') # 한개를 계속 한계로 인식해서 있으면 바꿔줌

print(sentence)
