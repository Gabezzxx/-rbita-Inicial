import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

angulos = np.linspace(0,2 * np.pi, 360)

print("Quantidade de pontos:", len(angulos) )
print("Primeiro Angulo:", angulos[0]) 
print("ultimo angulo:", round(angulos[-1], 3))

raio = 10

x = raio * np.cos(angulos)
y = raio * np.sin(angulos)

print("x[0]=", round(x[0], 2), "y[0]=", round(y[0], 2))
print("x[90]=", round(x[90], 2), "y[90]=", round(y[90], 2))

plt.figure(figsize=(6, 6))
plt.plot(x, y, label="Trajetória")
plt.title("Órbita do satélite")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.show()

