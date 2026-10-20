import matplotlib.pyplot as plt
import numpy as np
import random

from sympy.stats.rv import probability


def ori_popular(num):
    popular = []
    for i in range(num):
        x = random.uniform(-1, 4)
        popular.append(x)
    return popular

def encode(popular):
    popular_gene = []
    for i in range(len(popular)):
        data = int((popular[i] - (-1)) / 3 * 2**18)
        bin_data = bin(data)
        for j in range(len(bin_data)-2, 18):
            bin_data = bin_data[0:2] + '0' + bin_data[2:]
        popular_gene.append(bin_data)
    return popular_gene

def decode(popular_gene):
    fitness = []
    for i in range(len(popular_gene)):
        x = (int(popular_gene[i],2)/2**18) * 3 -1
        value = x * np.sin(10*np.pi*x) + 2
        fitness.append(value)
    return fitness

def choice_ex(popular_gene):
    fitness = decode(popular_gene)

    # 轮盘赌要求权重非负，把整体平移到正数
    min_fit = min(fitness)
    weights = [f - min_fit + 1e-12 for f in fitness]
    total = sum(weights)

    probability_sum = []
    acc = 0.0
    for w in weights:
        acc += w / total
        probability_sum.append(acc)

    popular_new = []
    for i in range(int(len(fitness) / 2)):
        temp = []
        for j in range(2):
            rand = random.uniform(0, 1)
            # 找到累积概率首次 >= rand 的个体；rand 超过最后一个时选最后一个
            k = 0
            while k < len(probability_sum) - 1 and rand > probability_sum[k]:
                k += 1
            temp.append(popular_gene[k])

        if random.randint(0, 2):
            temps = temp[0][9:15]
            temp[0] = temp[0][0:9] + temp[1][9:15] + temp[0][15:]
            temp[1] = temp[1][0:9] + temps + temp[1][15:]

        popular_new.append(temp[0])
        popular_new.append(temp[1])

    return popular_new          # ← 必须在 for 循环外

def choice_ex_old(popular_gene):
    fitness = decode(popular_gene)
    sum_fit_value = 0
    for i in range(len(fitness)):
        sum_fit_value += fitness[i]
    probability = []
    for i in range(len(fitness)):
        probability.append(fitness[i]/sum_fit_value)
    probability_sum = []
    for i in range(len(fitness)):
        if i == 0:
            probability_sum.append(probability[i])
        else:
            probability_sum.append(probability_sum[i-1] + probability[i])
    popular_new = []
    for i in range(int(len(fitness)/2)):
        temp = []
        for j in range(2):
            rand = random.uniform(0, 1)
            for k in range(len(fitness)):
                if k == 0:
                    if rand < probability_sum[k]:
                        temp.append(popular_gene[k])
                else:
                    if (rand > probability_sum[k-1]) and (rand < probability_sum[k]):
                        temp.append(popular_gene[k])
            is_change = random.randint(0, 2)
            if is_change:
                temps = temp[0][9:15]
                temp[0] = temp[0][0:9] + temp[1][9:15] + temp[0][15:]
                temp[1] = temp[1][0:9] + temps + temp[1][15:]
            popular_new.append(temp[0])
            popular_new.append(temp[1])
    return popular_new

def variation(popular_new):
    for i in range(len(popular_new)):
        is_variation = random.uniform(0, 1)
        if is_variation < 0.02:
            rand = random.randint(2, 19)
            if popular_new[i][rand] == '0':
                popular_new[i] = popular_new[i][0:rand] + '1' + popular_new[i][rand+1:]
            else:
                popular_new[i] = popular_new[i][0:rand] + '0' + popular_new[i][rand+1:]
    return popular_new

if __name__ == '__main__':
    num = 100
    ori_popular = ori_popular(num)
    ori_popular_gene = encode(ori_popular)
    new_popular_gene = ori_popular_gene
    y = []
    for i in range(1000):
        new_popular_gene = choice_ex(new_popular_gene)
        new_popular_gene = variation(new_popular_gene)
        new_fitness = decode(new_popular_gene)
        sum_new_fitness = 0
        for j in new_fitness:
            sum_new_fitness += j
        y.append(sum_new_fitness/len(new_fitness))
    x = np.linspace(0,1000,1000)
    fig = plt.figure()
    axis = fig.add_subplot(111)
    axis.plot(x,y)
    plt.xlabel('number of iteration')
    plt.ylabel('fitness')
    plt.show()
    plt.savefig('遗传算法.png', dpi=800)