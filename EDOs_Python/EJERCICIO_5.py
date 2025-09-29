# ========== EJERCICIO 5 – Sistema sobreamortiguado ==========
import numpy as np
import matplotlib.pyplot as plt

r1, r2 = -2, -4
C1, C2 = 2, -1

def y(t):
    return C1*np.exp(r1*t) + C2*np.exp(r2*t)

t = np.linspace(0, 4, 500)
plt.figure(figsize=(8, 4))
plt.plot(t, y(t), label='y(t)')
plt.title('Respuesta sobreamortiguada de segundo orden')
plt.xlabel('Tiempo [s]'); plt.ylabel('y'); plt.grid(); plt.legend()
plt.savefig('imagen-ejercicio5.png', dpi=300, bbox_inches='tight')
plt.show()