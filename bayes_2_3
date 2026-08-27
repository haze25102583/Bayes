# 2.3 베이지안 프레임워크

from thinkbayes import Pmf

class Cookie(Pmf):
    def __init__(self, hypos):
        Pmf.__init__(self, values=hypos)
        self.mixes = {
            'Bowl 1': dict(vanilla=0.74, chocolate=0.25),
            'Bowl 2': dict(vanilla=0.5, chocolate=0.5)
        }
    
    # 사후확률
    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()
    
    # 우도
    def Likelihood(self, data, hypo):
        mix = self.mixes[hypo]
        like = mix[data]
        return like
    
# 가설 설정
hypos_cookie = ['Bowl 1', 'Bowl 2']
pmf_cookie = Cookie(hypos_cookie)

pmf_cookie.Update('vanilla')

for hypo, prob in pmf_cookie.Items():
    print(hypo, '   ', prob)

    """출력 결과
    Bowl 1     0.5967741935483871
    Bowl 2     0.40322580645161293
    """ 