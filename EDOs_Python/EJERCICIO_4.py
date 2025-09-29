# ========== EJERCICIO 4 – Decaimiento de población ==========
import numpy as np
import matplotlib.pyplot as plt

P0, lam = 100_000, 0.05
t_half = np.log(0.5)/(-lam)

def P(t):
    return P0 * np.exp(-lam*t)

t = np.linspace(0, 50, 400)
plt.figure(figsize=(8, 4))
plt.plot(t, P(t)/1000, label='Población [miles]')
plt.axhline(P0/2/1000, color='r', ls='--', label=f'Mitad: {t_half:.1f} años')
plt.title('Decaimiento exponencial de población')
plt.xlabel('Tiempo [años]'); plt.ylabel('Población [miles]'); plt.grid(); plt.legend()
plt.savefig('imagen-ejercicio4.png', dpi=300, bbox_inches='tight')
plt.show()