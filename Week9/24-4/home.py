import matplotlib.pyplot as plt
import numpy as np
t=np.arange(1,10,0.1)
x=np.sin(0.2*3.14*t)
plt.subplot(1,2,1)
plt.plot(t,x)
plt.subplot(1,2,2)
y=np.cos(0.5*3.14*t)
t1=np.arange(1,10,0.1)
plt.plot(t1,y)
plt.show()
