import random
import numpy as np
import matplotlib.pyplot as plt

class GA:
    #We need the number of generations, mutation probability at beginning.
    def __init__(self,x,num=100,mp=0.02):
        self.num = num
        self.mp = mp
        self.x = x

    # Define the function of expecting.
    def func(self):
        res = self.x * np.sin(10 * np.pi * self.x) + 2
        return res

    #Generating an array of original seeds.
    def original_popular(self):
        original_popular = []
        for i in range(self.num):
            u = random.uniform(-1,4)
            original_popular.append(u)
        return original_popular

    #Encoding the original popular.
    def encode(self,):
        popular_gene = []
        original_popular = self.original_popular()
        for i in range(len(original_popular)):
            data = int((original_popular[i] - (-1)) / 5 * 2**18)
            bin_data = '0b' + bin(data)[2:].zfill(18)
            popular_gene.append(bin_data)
        return popular_gene

    #Decoding the encoding popular
    def decode(self):
        popular_gene = self.encode()
        fitness = []
        for i in range(len(popular_gene)):
            x = -1 + int(popular_gene[i],2) / 2**18 * 5
            value = self.func(x)
            fitness.append(value)
        return fitness

    #Selection and crossover
    def choice_ex(self):
        fitness = self.decode()
        popular_gene = self.encode()
        sum_fitness_value = 0
        for i in range(len(fitness)):
            sum_fitness_value += fitness[i]
        probability_fitness = []
        v = 0
        for i in range(len(fitness)):
            u = fitness[i] / sum_fitness_value
            v = v + u
            probability_fitness.append(v)
        popular_new = []
        for p in range(int(len(fitness)/2)):
            temp = []
            for j in range(2):
                rand = random.uniform(0,1)
                for k in range(len(fitness)):
                    if k == 0:
                        if probability_fitness[k] > rand:
                            temp.append(popular_gene[k])
                    else:
                        if (rand > probability_fitness[k-1]) and (probability_fitness[k] > rand):
                            temp.append(popular_gene[k])
                is_change = random.randint(0,2)
                if is_change:
                    temps = temp[0][9:15]
                    temp[0] = temp[0][:9] + temp[1][9:15] + temp[0][15:]
                    temp[1] = temp[1][:9] + temps + temp[1][15:]
            popular_new.append(temp[0])
            popular_new.append(temp[1])
        return popular_new

    #Defining the variation.
    def variation(self,):
        popular_gene = self.choice_ex()
        for i in range(len(popular_gene)):
            rand_mp = random.uniform(0,1)
            if rand_mp < self.mp:
                rand_se = random.randint(2, 19)
                if popular_gene[i][rand_se] == 0:
                    popular_gene[i] = popular_gene[i][:rand_se] + '1' + popular_gene[i][rand_se + 1:]
                else:
                    popular_gene[i] = popular_gene[i][:rand_se] + '0' + popular_gene[i][rand_se + 1:]
        return popular_gene

#Main process
if __name__ == '__main__':
    ga = GA(num=100)
    x = ga.original_popular()
    new_popular = ga.encode()
    y = []
    for i in range(1000):
        new_popular_gene = ga.choice_ex(new_popular_gene)
        new_popular_gene = ga.variation()
        new_fitness = ga.decode(new_popular_gene)
        sum_new_fitness = 0
        for j in new_fitness:
            sum_new_fitness += j
        y.append(sum_new_fitness / len(new_fitness))
    x = np.linspace(0,1000,1000)
    fig = plt.figure()
    axis = fig.add_subplot(111)
    axis.plot(x,y)
    plt.xlabel('number of iterations')
    plt.ylabel('fitness')
    plt.show()