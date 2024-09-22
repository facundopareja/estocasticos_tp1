import numpy as np
import matplotlib.pyplot as plt

# a
# Dos formas de obtener 11 = 5 + 6 = 6 + 5
# Varias formas de obtener 7 = 1 + 6 = 2 + 5 = 3 + 4 = 4 + 3 = 5 + 2 = 6 + 1
# Asumiendo dados indpendientes, cada caso tiene chance 1/36 de suceder
# Luego, la probabilidad de ganar un lanzamiento es = 8/36 = 2/9
# La probabilidad que modela esto es Bernoulli con parametro 2/9.

# b
SAMPLE_SIZE = 10000

def get_dice_number(value):
    if value < 1/6:
        return 1
    elif 1/6 <= value < 2/6:
        return 2
    elif 2/6 <= value < 3/6:
        return 3
    elif 3/6 <= value < 4/6:
        return 4
    elif 4/6 <= value < 5/6:
        return 5
    elif value >= 5/6:
        return 6

U1 = np.random.uniform(0, 1, SAMPLE_SIZE)
U2 = np.random.uniform(0, 1, SAMPLE_SIZE)

result = []

for i in range(SAMPLE_SIZE):
    throw_1 = get_dice_number(U1[i])
    throw_2 = get_dice_number(U2[i])
    if throw_1 + throw_2 == 7 or throw_1 + throw_2 == 11:
        result.append(1)
    else:
        result.append(0)

result = np.asarray(result)
ocurrences = np.unique_counts(result)
print(f"La fraccion teorica de exitos deberia ser {2/9}")
print(f"La fraccion de exitos del total es {ocurrences[1][1]/SAMPLE_SIZE}")
plt.hist(result)
plt.show()

# c
# Para determinar la cantidad de exitos en n e experimentos Bernoulli
# se utiliza una distribucion Binomial (n, 2/9)

# d
THROWS = 20
result = []
for i in range(SAMPLE_SIZE):
    number_wins = 0
    U1 = np.random.uniform(0, 1, THROWS)
    U2 = np.random.uniform(0, 1, THROWS)
    for j in range(THROWS):
        throw_1 = get_dice_number(U1[j])
        throw_2 = get_dice_number(U2[j])
        if throw_1 + throw_2 == 7 or throw_1 + throw_2 == 11:
            number_wins += 1
    result.append(number_wins)
result = np.asarray(result)
plt.hist(result)
plt.show()