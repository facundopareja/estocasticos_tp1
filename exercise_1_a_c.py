import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

SAMPLE_SIZE = 10000
BINS = 50

U1 = np.random.uniform(0, 1, SAMPLE_SIZE)
U2 = np.random.uniform(0, 1, SAMPLE_SIZE)

def box_muller_z1_function(U1, U2):
    return np.sqrt(-2 * np.log(U1)) * np.cos(2 * np.pi * U2)

def box_muller_z2_function(U1, U2):
    return np.sqrt(-2 * np.log(U1)) * np.sin(2 * np.pi * U2)

Z1 = np.apply_along_axis(box_muller_z1_function, 0, U1, U2)
Z2 = np.apply_along_axis(box_muller_z2_function, 0, U1, U2)

print(f"La media estimada para Z1 es {np.mean(Z1)}")
print(f"La varianza estimada para Z1 es {np.var(Z1)}")

print(f"La media estimada para Z2 es {np.mean(Z2)}")
print(f"La varianza estimada para Z2 es {np.var(Z2)}")

plt.hist(Z1, bins = BINS)
plt.show()
plt.hist(Z2, bins = BINS, color='orange')
plt.show()

plt.scatter(Z1, Z2, color = 'green')
plt.show()

print(np.corrcoef(Z1,Z2))

def x1_transformation_function(x):
    return np.sqrt(2) * x


def x2_transformation_function(x):
    return (np.sqrt(2) * x) + 1


def x3_transformation_function(x):
    return (2 * x) + 1

# Aplicando los resultados del inciso b) transformo linealmente una variable normal estandar
# para obtener lo pedido.

X1 = np.apply_along_axis(x1_transformation_function, 0, Z1)
X2 = np.apply_along_axis(x2_transformation_function, 0, Z1)
X3 = np.apply_along_axis(x3_transformation_function, 0, Z1)

print(f"La media teorica para X1 es 0 y la estimada es {np.mean(X1)}")
print(f"La varianza teorica para X1 es 2 y la estimada es {np.var(X1)}")

print(f"La media teorica para X2 es 1 y la estimada es {np.mean(X2)}")
print(f"La varianza teorica para X2 es 2 y la estimada es {np.var(X2)}")

print(f"La media teorica para X3 es 1 y la estimada es {np.mean(X3)}")
print(f"La varianza teorica para X3 es 4 y la estimada es {np.var(X3)}")

def compare_hist_pdf(values, mu, variance):
    plt.hist(values, bins=50, density=True)
    sigma = np.sqrt(variance)
    x = np.linspace(mu - 5 * sigma, mu + 5 * sigma, SAMPLE_SIZE)
    plt.plot(x, stats.norm.pdf(x, mu, sigma), color='r')
    plt.show()

compare_hist_pdf(X1, 0, 2)
compare_hist_pdf(X2, 1, 2)
compare_hist_pdf(X3, 1, 4)