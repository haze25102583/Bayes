# 3.2 기관차 문제

# 베이지안 추론법
#  1. 데이터를 보기 전에 N에 대하여 알고 있는 것?
#  2. N에 어떤 값이 주어졌을 때, 관측한 데이터의 우도?

from thinkbayes import Suite


hypos = range(1, 1001)     # N은 1~1000 어떤 값이든 동일한 확률로 선택

class Train(Suite):
    def Likelihood(self, data, hypo):
        if hypo < data:
            return 0
        else:
            return 1.0/hypo
        
suite = Train(hypos)
suite.Update(60)

def Mean(suite):            # 사후 확률의 평균
    total = 0
    for hypo, prob in suite.Items():
        total += hypo * prob
    return total

print(Mean(suite))      # 333.41989326371095 출력
print(suite.Mean())     # 333.41989326371095 출력