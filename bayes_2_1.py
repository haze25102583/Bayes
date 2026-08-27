from thinkbayes import Pmf      # 확률 질량 함수: probability mass function

# 분포 : 어떤 값, 그 값의 확률의 집합

# 육면체 주사위의 결과 분포
pmf = Pmf()
for x in [1, 2, 3, 4, 5, 6]:
    pmf.Set(x, 1/6.0)           # 각 값에 1/6의 확률값 set
print(pmf.Prob(x))              # 0.16666666666666666 출력

word_list = ['it', 'is', 'the', 'cat', '. ', 'the', 'cat', 'is', 'so', 'cute']

# 연속적인 각 단어를 count
pmf = Pmf()
for word in word_list:
    pmf.Incr(word, 1)           # 각 단어마다 확률 1씩 높임

# 정규화 -> 확률 합이 1
pmf.Normalize()
print(pmf.Prob('the'))          # 0.2 출력
