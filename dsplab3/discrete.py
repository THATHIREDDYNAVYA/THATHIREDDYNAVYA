import numpy as np
import matplotlib.pyplot as plt
n=np.arange(-5,6)
x = np.array([-2, 3, 0, -1, 2, 3, 1, 0, 0, 0, 0])
plt.figure(figsize=(8, 4))
plt.stem(n, x)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Discrete Time Signal')
plt.grid()
plt.show()
