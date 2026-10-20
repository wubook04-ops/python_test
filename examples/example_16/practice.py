from random import random
import math
import matplotlib.pyplot as plt
#定义待求解函数
def func(x,y) -> str:
    res = 3*x**2 - 2.1*x**4 +x**6/3 + x*y - 3*y**2 + 3*y**4
    return res

#定义类
class SA():
#定义初始值，为每个实例单独赋值且定义初始温度、终温、内循环迭代次数、每次退火速率
    def __init__(self, func, iter=100, T0=100, Tf=0.01, alpha=0.99):
        #给实例附上值
        self.func = func
        self.iter = iter
        self.T = T0
        self.Tf = Tf
        self.alpha = alpha
        #给出100个范围内、随机的初值
        self.x = [random()*10-5 for i in range(self.iter)]
        self.y = [random()*10-5 for i in range(self.iter)]
        #初始化计算的容器，保存计算好的数值
        self.best_value = []
        self.history = {'f':[],'T':[]}

    #定义新产生的迭代值
    def generate_new(self,x,y):
        while True:
            x_new = x + self.T*(random() - random())
            y_new = y + self.T*(random() - random())
            #使用 if 语句检测新值是否符合要求
            if (-5<= x_new <=5) and (-5 <= y_new <= 5):
                break
        #返回符合要求的新值
        return x_new, y_new

    #判断产生的值是否可以作为新解
    def Metrosplis(self, f, f_new):
        #如果新值小于原值，直接取用
        if f_new <= f:
            return 1
        else:
            #使用一个阈值判断该值是否留
            p = math.exp((f - f_new)/ self.T)
            if p > random():
                return 1
            else:
                return 0

    #获取最优值
    def best(self):
        #建立一个空集合
        f_list = []
        #迭代目标次数找值
        for i in range(self.iter):
            #用实例的x, y 为方程赋值求解
            f = self.func(self.x[i], self.y[i])
            f_list.append(f)
        #找到集合中最小的值
        f_best = min(f_list)
        idx = f_list.index(f_best)
        return f_best, idx

    def run(self):
        count = 0
        #开始退火，温度下降迭代
        while self.T > self.Tf:
            #内循环迭代100次, 在0~99
            for i in range(self.iter):
                #开始利用self.func()将生成的self.x/y 值代入求解
                f = self.func(self.x[i], self.y[i])
                #利用开始生成的x,y 初值代入self.generate_new()产生新的迭代值
                x_new, y_new = self.generate_new(self.x[i], self.y[i])
                #将新的迭代值代入方程求解新的求解值
                f_new = self.func(x_new, y_new)
                #将新解值代入self.Metrosplis()中判断是否取值
                if self.Metrosplis(f, f_new):
                    self.x[i] = x_new
                    self.y[i] = y_new
                #如果判断不合格，保留原值（其可以忽略）
                else:
                    self.x[i] = self.x[i]
                    self.y[i] = self.y[i]

            #利用ft和_取得上迭代的最优值
            ft,_ = self.best()
            #将最优值和温度保存到history中
            self.history['f'].append(ft)
            self.history['T'].append(self.T)
            #每次迭代后，温度下降
            self.T = self.T * self.alpha
            count += 1
        #最后求取最优值self.best()
        f_best, idx = self.best()
        print(f'F = {f_best}, x = {self.x[idx]}, y = {self.y[idx]}')

sa = SA(func)
sa.run()
plt.plot(sa.history['T'], sa.history['f'])
plt.title('SA')
plt.xlabel('T')
plt.ylabel('f')
#plt.gca().invert_xaxis()
plt.show()