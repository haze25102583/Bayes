# 2.6 M&M 문제
from thinkbayes import Pmf
from thinkbayes import Suite

mix94 = dict(brown=30,
             yellow=20,
             red=20,
             green=10,
             orange=10,
             tan=10)

mix96 = dict(blue=24,
             green=20,
             orange=16,
             yellow=14,
             red=13,
             brown=13)

hypoA = dict(bag1=mix94, bag2=mix96)
hypoB = dict(bag1=mix96, bag2=mix94)

hypotheses = dict(A=hypoA, B=hypoB)

class M_and_M(Suite):
    def __init__(self, hypos, hypotheses):
        Suite.__init__(self, values=hypos)
        self.hypotheses = hypotheses
        
    def Likelihood(self, data, hypo):
        bag, color = data
        mix = self.hypotheses[hypo][bag]
        like = mix[color]
        return like

suite = M_and_M('AB', hypotheses)

suite.Update(('bag1', 'yellow'))
suite.Update(('bag2', 'green'))
suite.Print()

"""
출력
A 0.7407407407407407
B 0.2592592592592592
"""