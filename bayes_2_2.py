# 2.2 쿠키 문제
from thinkbayes import Pmf

pmf = Pmf()

# 사전분포
pmf.Set('Bowl 1', 0.5)
pmf.Set('Bowl 2', 0.5)

# 사후확률 = p(H) x p(D|H)
pmf.Mult('Bowl 1', 0.75)
pmf.Mult('Bowl 2', 0.5)

# 정규화
pmf.Normalize()
print(pmf.Prob('Bowl 1'))       # 0.6000000000000001 출력