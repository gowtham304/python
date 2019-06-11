import numpy as np
k=np.random.randint(1,20, size=15)
print(k)
k[k==k.max()]=0
print(k)