from matplotlib import pyplot as plt
import numpy as np

class DRAW_GRAPH():

    def __init__(self,n,p):
        self.n=n
        self.p=p

    def cal_binomial(self):
        for i in range(self.n+1):
            n=self.n
            p=self.p
            nCi=self.factorial(n)/(self.factorial(i)*self.factorial(n-i))
            px= nCi * p**i * (1-p)**(n-i)
            print(px)

    def factorial(self, n):
        if n>1:
            return n * self.factorial(n-1)
        else:
            return 1
    def draw_graph(self):
                
a=DRAW_GRAPH()
print(a.cal_binomial())
