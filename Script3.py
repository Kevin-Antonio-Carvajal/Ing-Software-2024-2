import matplotlib.pyplot as plt
import numpy as np

# Define los valores de x desde -10 a 10, incremento de 0.1
x = np.arange(-15., 15., 0.2)
# Calcula los valores de y usando la función cuadrática
y = x ** 2

# Crea la gráfica
plt.plot(x, y)

# Título y etiquetas de los ejes
plt.title('Gráfica de una Función Cuadrática')
plt.xlabel('x')
plt.ylabel('y = x^2')

# Muestra la gráfica
plt.show()

