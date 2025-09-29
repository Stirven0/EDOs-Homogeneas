# ========== EJERCICIO 2 – Circuito RLC serie ==========
import numpy as np
import matplotlib.pyplot as plt

R, L, C = 100, 0.5, 10e-6
alpha = R/(2*L)
omega = np.sqrt(1/(L*C) - alpha**2)

def i(t):
    return np.exp(-alpha*t)*(0.1*np.cos(omega*t) + (0.1*alpha/omega)*np.sin(omega*t))

t = np.linspace(0, 0.1, 1000)
plt.figure(figsize=(8, 4))
plt.plot(t, 1000*i(t), label='Corriente i(t) [mA]')
plt.title('Corriente en circuito RLC subamortiguado')
plt.xlabel('Tiempo [s]'); plt.ylabel('i [mA]'); plt.grid(); plt.legend()
plt.savefig('imagen-ejercicio2.png', dpi=300, bbox_inches='tight')
plt.show()