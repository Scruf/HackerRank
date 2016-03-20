%matplotlib inline 

import matplotlib.pyplot as plt


x = np.linspace(0,10,30)
y = np.sin(x)
z = y + np.random.normal(size=30)*0.2
plt.plot(x,y, 'ro',label='A sine wave')
plt,plot(x,z,'b-', label='Noisy sine')
plt.legend(loc ='lower right')
plt.xlabel('X axis')
plt.ylable('Y axis')
