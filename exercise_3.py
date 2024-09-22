import numpy as np
import matplotlib.pyplot as plt

#b
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
plt.hist(result)
plt.title('Histograma realizado con muestras aleatorias')
plt.xlabel('Valor de X')
plt.ylabel('Cantidad de ocurrencias')
plt.show()
theoretical_number_wins = int((2 / 9) * SAMPLE_SIZE)
theoretical_number_losses = SAMPLE_SIZE - theoretical_number_wins
theoretical = np.concatenate((np.full(theoretical_number_wins, 1), np.full(theoretical_number_losses, 0)), axis=0)
plt.hist(theoretical, color='red')
plt.title('Histograma teorico')
plt.xlabel('Valor de X')
plt.ylabel('Cantidad de ocurrencias')
plt.show()

#d
THROWS = 20
result = []
theoretical_results = []
for i in range(SAMPLE_SIZE):
    number_wins = 0
    U1 = np.random.uniform(0, 1, THROWS)
    U2 = np.random.uniform(0, 1, THROWS)
    binomial_results = np.random.binomial(THROWS, 2 / 9)
    for j in range(THROWS):
        throw_1 = get_dice_number(U1[j])
        throw_2 = get_dice_number(U2[j])
        if throw_1 + throw_2 == 7 or throw_1 + throw_2 == 11:
            number_wins += 1
    result.append(number_wins)
    theoretical_results.append(binomial_results)

result = np.asarray(result)
theoretical_results = np.asarray(theoretical_results)
plt.hist(result)
plt.title('Histograma realizado con muestras aleatorias')
plt.xlabel('Valor de Y')
plt.ylabel('Cantidad de ocurrencias')
plt.show()
plt.hist(theoretical_results, color='red')
plt.title('Histograma teorico')
plt.xlabel('Valor de Y')
plt.ylabel('Cantidad de ocurrencias')
plt.show()