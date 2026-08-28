# 3.3 사전 확률로 할 수 있는 것

from thinkbayes import Suite

class Train(Suite):
    def Likelihood(self, data, hypo):
        if hypo < data:
            return 0
        else:
            return 1.0/hypo
        
def Mean(suite):            # 사후 확률의 평균
    total = 0
    for hypo, prob in suite.Items():
        total += hypo * prob
    return total
        
for lim in [500, 1000, 2000]:
    hypos = range(1, lim)     # N은 1~1000 어떤 값이든 동일한 확률로 선택
    suite = Train(hypos)

    for data in [60, 30, 90]:
        suite.Update(data)
    print(Mean(suite))      
    
    """
    상한선 | 사후 평균
    500     151.8034860627796
    1000    164.29208953758172
    2000    171.33451161537926
    """