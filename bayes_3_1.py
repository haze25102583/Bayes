# 3.1 주사위 문제
from thinkbayes import Suite

class Dice(Suite):
    def Likelihood(self, data, hypo):
        if hypo < data:
            return 0
        else:
            return 1.0/hypo

suite = Dice([4, 6, 8, 12, 20])
suite.Update(6)     # 주사위를 굴렸을 때 6이 나옴
suite.Print()

"""
4 0.0
6 0.392156862745098
8 0.29411764705882354
12 0.196078431372549
20 0.11764705882352942
"""
print(" =============== ")

for roll in [6, 8, 7, 7, 5, 4]:     # 주사위를 굴렸을 때 다음의 숫자가 차례로 나옴
    suite.Update(roll)
suite.Print()

"""
4 0.0
6 0.0
8 0.9432484536722124
12 0.055206128061290875
20 0.001545418266496554
"""