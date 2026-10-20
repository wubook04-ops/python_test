import random
import numpy as np


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
    def encode(self):
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
        sum_fitness_value = 0
        for i in range(len(fitness)):
            sum_fitness_value += fitness[i]
        probability_fitness = []
        for i in range(len(fitness)):
            u = fitness[i] / sum_fitness_value
            probability_fitness.append(u)
        temp = []
        for i in range(int(len(fitness)/2)):