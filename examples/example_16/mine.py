from random import random
import math

def func(x,y):
    res = 3*x**2 - 2.1*x**4 + x**6/3 + x*y - 3*y**2 + 3*y**4
    return res

class SA():
    def __init__(self, func, T0=100, Tf=0.01, alpha=0.99, n_iter = 100):
        #Metropolis algorithm needs the original temperature, the final temperature, the decrease step alpha,
        #the number of iteration,
        self.n_iter = n_iter
        self.func = func
        self.T0 = T0
        self.T = T0
        self.Tf = Tf
        self.alpha = alpha
        #产生初始迭代集合
        self.x = []
        for i in range(self.n_iter):
            self.x.append(10*random() - 5)
        self.y = [10*random() - 5 for i in range(self.n_iter)]
        self.history = {'f':[], 'T':[]}

    #创造新值，有初始x, y 迭代
    def generate_new(self, x, y):
        #判断是否为真，返回新值并判断
        while True:
            x_new = x + (random() - random()) * self.T
            y_new = y + (random() - random()) * self.T
            #如果新值符合要求，则退出循环
            if (-5 <= x_new <= 5) and (-5 <= y_new <= 5):
                break
        return x_new, y_new

    #判断新解值是否接受，如果接受返回1， 拒绝返回0
    def Metrosplis(self, f,f_new):
        if f_new <= f:
            return 1
        else:
            #利用阈值判断非理想值是否取舍
            p = math.exp((f-f_new)/self.T)
            if random() < p:
                return 1
            else:
                return 0

    #选取目标最优值
    def best(self):
        #建立个空集合放置
        f_list = []
        for i in range(self.n_iter):
            f = self.func(self.x[i], self.y[i])
            f_list.append(f)
        f_best = min(f_list)
        idx = f_list.index(f_best)
        return f_best, idx

    #开始编写后续计算所需的集合
    def run(self):
        while self.T >= self.Tf:
            #内循环迭代
            for i in range(self.n_iter):
                f = self.func(self.x[i], self.y[i])
                x_new, y_new = self.generate_new(self.x[i], self.y[i])
                f_new = self.func(x_new, y_new)
                if self.Metrosplis(f,f_new):
                    self.x[i] = x_new
                    self.y[i] = y_new
            ft,_ = self.best()
            self.history['f'].append(ft)
            self.history['T'].append(self.T)
            self.T *= self.alpha

        f_best, idx = self.best()
        print(f'F = {f_best}, x = {self.x[idx]}, y = {self.y[idx]}')

sa = SA(func)
sa.run()