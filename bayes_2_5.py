# 2.5 프레임워크 캡슐화
from thinkbayes import Pmf

class Suite(Pmf):
    
    """가설과 가설들의 확률로 구성된 스윗을 나타냄"""
    # 스윗
    # 1. 상호배제 : 집합 중 하나의 가설만 참
    # 2. 전체 포괄 : 다른 가능성이 전혀 x
    
    def __init__(self, hypo=tuple()):
        """분포 초기화"""
        
    def Update(self, data):
        """데이터 기반의 가설을 각각 갱신"""
        
    def Print(self):
        """가설과 확률 출력"""
        
from thinkbayes import Suite

class Monty(Suite):
    
    def Likelihood(self, data, hypo):
        if hypo == data:
            return 0
        elif hypo == 'A':
            return 0.5
        else:
            return 1
        
suite = Monty('ABC')
suite.Update('B')
suite.Print()

"""출력
A 0.3333333333333333
B 0.0
C 0.6666666666666666
"""