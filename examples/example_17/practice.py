import matplotlib.pyplot as plt
import numpy as np
import random

#Initialization the groups
def ori_popular(num):
    #初始化原始种群
    popular = []
    for i in range(num):
        #生成一个[-1, 4]范围内随机浮点数
        x = random.uniform(-1, 4)
        popular.append(x)
    return popular

#编码
def encode(popular):
    popular_gene = []
    #为每一个种群进行编码
    for i in range(len(popular)):
        #染色体序列为18位
        #data归一化, 将[-1, 4]范围平移至[0, 5]后除以5, 扩展至二进制的18 位
        #选取2**18 意旨为足够的精度
        data = int((popular[i] - (-1))/ 5 * 2**18)
        #将整型转化为二进制, 其以字符串的形式存在
        bin_data = bin(data)
        #如果序列长度不足则补充0
        for j in range(len(bin_data)-2, 18):
            bin_data = bin_data[:2] + '0' + bin_data[2:]
        popular_gene.append(bin_data)
    return popular_gene

#解码
def decode(popular_gene):
    fitness = []
    for i in range(len(popular_gene)):
        #将上面编码后的popular_gene转化为原来种群
        x = (-1) + int(popular_gene[i],2)/(2**18) * 5
        #适应度的函数
        value = x * np.sin(10 * np.pi * x) + 2
        fitness.append(value)
    return fitness

#选择和交叉, 选择轮盘赌法, 交叉概率是0.66
def choice_ex(popular_gene):
    fitness = decode(popular_gene)
    #权重的积累
    sum_fit_value = 0
    for i in range(len(fitness)):
        sum_fit_value += fitness[i]
    #可能性的定义（权重）
    probility = []
    for i in range(len(fitness)):
        probility.append(fitness[i]/sum_fit_value)
    #概率分布
    probility_sum = []
    #循环作用是将以上概率累加, 分配到probility_sum的集合中，以len(fitness)下标
    #代表各个区间段的概率值，比如[0.1, 0.3, 0.5, 0.7, 1.0], 随机数位于0.2时取index=2, 位于0.8时取index=4
    for i in range(len(fitness)):
        if i == 0:
            probility_sum.append(probility[i])
        else:
            probility_sum.append(probility_sum[i-1] + probility[i])
    #种群的选择
    popular_new = []
    #分为两个父代
    for i in range(int(len(fitness)/2)):
        temp = []
        #为每个父代生成一个存放位置
        for j in range(2):
            #在0~1 随机生成一个浮点数
            rand = random.uniform(0, 1)
            #轮盘赌选择
            k = 0
            #判断k值和rand取值是否在概率分布区间, 如果符合要求则迭代
            while k < (len(probility_sum)-1) and rand > (probility_sum[k]):
                k += 1
            #不符合要求则直接赋值
            temp.append(popular_gene[k])

        #交叉概率，利用布尔值判断, 真的概率为2/3
        if random.randint(0, 2):
            #先取出父代1的9-15的基因
            temps = temp[0][9:15]
            #将父代2的9-15的基因插入父代1
            temp[0] = temp[0][0:9] + temp[1][9:15] + temp[0][15:]
            #将父代1的基因插入父代2
            temp[1] = temp[1][0:9] + temps + temp[1][15:]
        #收集子代
        popular_new.append(temp[0])
        popular_new.append(temp[1])
    return popular_new

#变异
def variation(popular_new):
    #遍历种群中的每一个个体
    for i in range(len(popular_new)):
        #生成随机数, 为后续判断是否变异提供支持
        is_variation = random.uniform(0, 1)
        #判断是否变异, 变异概率设为2%
        if is_variation < 0.02:
            #随机取位于3-18位上的位点，准备变异
            rand = random.randint(2, 19)
            if popular_new[i][rand] == '0':
                popular_new[i] = popular_new[i][0:rand] + '1' + popular_new[i][rand+1:]
            else:
                popular_new[i] = popular_new[i][0:rand] + '0' + popular_new[i][rand+1:]
    return popular_new

#主程序
if __name__ == '__main__':
    #初始化原始种群, 100个个体
    num = 100
    ori_popular = ori_popular(num)
    #得到原始种群的基因, 18位基因
    ori_popular_gene = encode(ori_popular)
    new_popular_gene = ori_popular_gene
    y = []
    #迭代次数1000次, 繁殖1000代
    for i in range(1000):
        #选择和交叉操作
        new_popular_gene = choice_ex(new_popular_gene)
        #变异操作
        new_popular_gene = variation(new_popular_gene)
        #取当代所有个体的适度平均值
        new_fitness = decode(new_popular_gene)
        #计算适度的总值
        sum_new_fitness = 0
        for j in new_fitness:
            sum_new_fitness += j
        y.append(sum_new_fitness/len(new_fitness))
    x = np.linspace(0, 1000, 1000)
    fig = plt.figure()
    axis = fig.add_subplot(111)
    axis.plot(x, y)
    plt.xlabel('numbel of iterations')
    plt.ylabel('fitness')
    plt.show()