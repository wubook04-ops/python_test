import numpy as np
DNA_size = 24
POPULATION_size = 200
GENERATION_number = 50
Cross_rate = 0.8
Variation_rate = 0.01
X_range = [-5, 5]
Y_range = [-5, 5]

def problem_function(x, y):
    return x**2 + np.sin(2*y)

def decoding_DNA(popular_matrix):
    x_matrix = popular_matrix[:, 1::2]
    y_matrix = popular_matrix[:, 0::2]
    decoding_vector = 2 ** np.arange(DNA_size)[::-1]
    population_x_vector = x_matrix.dot(decoding_vector) / (2**DNA_size -1) * (X_range[1] - X_range[0]) + X_range[0]
    population_y_vector = y_matrix.dot(decoding_vector) / (2**DNA_size -1) * (Y_range[1] - Y_range[0]) + Y_range[0]
    return population_x_vector, population_y_vector

def DNA_cross(child_DNA, population_matrix):
    if np.random.rand() < Cross_rate:
        mother_DNA = population_matrix[np.random.randint(POPULATION_size)]
        cross_posotion = np.random.randint(DNA_size * 2)
    child_DNA[cross_posotion] = mother_DNA[cross_posotion:]

def DNA_variation(child_DNA):
    if np.random.rand() < Variation_rate:
        variation_posotion = np.random.randint(DNA_size * 2)
        child_DNA[variation_posotion] = child_DNA[variation_posotion] ^ 1

def update_population(population_matrix):
    new_population_matrix = []
    for father_DNA in population_matrix:
        child_DNA = father_DNA
        DNA_cross(child_DNA, population_matrix)
