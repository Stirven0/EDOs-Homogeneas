# ========== EJERCICIO 3 – Nivel de tanque ==========
import numpy as np
import matplotlib.pyplot as plt

A, k = 5, 0.5
h0 = 2
tau = A/k

def h(t):
    return h0 * np.exp(-t/tau)

t = np.linspace(0, 60, 500)
plt.figure(figsize=(8, 4))
plt.plot(t, h(t), label='Altura h(t) [m]')
plt.title('Nivel del tanque vs tiempo')
plt.xlabel('Tiempo [s]'); plt.ylabel('h [m]'); plt.grid(); plt.legend()
plt.savefig('imagen-ejercicio3.png', dpi=300, bbox_inches='tight')
plt.show()