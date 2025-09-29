# ========== EJERCICIO 1 – Sistema masa-resorte-amortiguador ==========
import numpy as np
import matplotlib.pyplot as plt

# Parámetros
m, c, k = 2, 8, 32
alpha = c/(2*m)
omega = np.sqrt(k/m - alpha**2)

# Solución analítica
def x(t):
    return np.exp(-alpha*t)*(0.1*np.cos(omega*t) + (0.1*alpha/omega)*np.sin(omega*t))

t = np.linspace(0, 5, 1000)
plt.figure(figsize=(8, 4))
plt.plot(t, x(t), label='Desplazamiento x(t) [m]')
plt.title('Respuesta del sistema masa-resorte-amortiguador')
plt.xlabel('Tiempo [s]'); plt.ylabel('x [m]'); plt.grid(); plt.legend()
plt.savefig('imagen-ejercicio1.png', dpi=300, bbox_inches='tight')
plt.show()