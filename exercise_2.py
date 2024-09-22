import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

SAMPLE_SIZE = 10000
u = 2
var = 3

def g_function(x, expectancy, variance):
    term_1 = 1/(np.sqrt(2 * np.pi * variance))
    term_2 = np.exp(-(np.power(x - expectancy, 2))/(2 * variance))
    return term_1 * term_2

vfunc = np.vectorize(g_function)

def estimate_integral(expectancy, variance, a, b):
    X = np.random.uniform(a, b, SAMPLE_SIZE)
    G = vfunc(X, expectancy, variance)
    print("El valor obtenido para la estimacion es")
    print(((b - a) / SAMPLE_SIZE) * np.sum(G))
    print("El valor obtenido para la integracion realizada directamente con SciPy es")
    print(sp.integrate.quad(lambda x: g_function(x, expectancy, variance), a, b)[0])

# a)
print("Inciso A")
a = u - np.sqrt(var)
b = u + np.sqrt(var)
estimate_integral(u, var, a, b)

#b
print("Inciso B")
a = u - (2 * np.sqrt(var))
b = u + (2 * np.sqrt(var))
estimate_integral(u, var, a, b)

#c
print("Inciso C")
a = u - (3 * np.sqrt(var))
b = u + (3 * np.sqrt(var))
estimate_integral(u, var, a, b)

#d
print("Inciso D")
SAMPLE_SIZES = [10, 100, 1000, 10000, 100000, 1000000]
I = 0.682687273250961
M = 50
result_list = []

a = u - np.sqrt(var)
b = u + np.sqrt(var)

for size in SAMPLE_SIZES:
    total_sum = 0
    for i in range(M):
        X = np.random.uniform(a, b, size)
        G = vfunc(X, u, var)
        estimation = ((b-a)/size) * np.sum(G)
        total_sum += np.power(estimation - I, 2)
    mse_estimation = total_sum / M
    result_list.append(mse_estimation)
    print(f"La estimacion para {size} muestras resulta ")
    print(estimation)
    print(f"El error para {size} muestras resulta ")
    print(mse_estimation)

mse = np.asarray(result_list)
plt.plot(SAMPLE_SIZES, mse, 'rs')
plt.title('Numero de muestras vs. MSE')
plt.xlabel('Numero de muestras')
plt.ylabel('MSE')
plt.show()