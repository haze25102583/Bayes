# 2.4 몬티 홀 문제

from thinkbayes import Pmf

class Monty(Pmf):
    
    def __init__(self, hypos):
        Pmf.__init__(self, values=hypos)
        
    # 사후 확률
    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()
        
    # 우도
    def Likelihood(self, data, hypo):
        if hypo == data:
            return 0
        elif hypo == 'A':
            return 0.5
        else:
            return 1
        
hypos = 'ABC'
pmf = Monty(hypos)

data = 'B'
pmf.Update(data)

for hypo, prob in pmf.Items():
    print(hypo, '   ', prob)