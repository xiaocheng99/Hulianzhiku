import numpy as np
a = np.arange(24)
a = a.reshape([6,4])
slices = [a[k:k+2] for k in range(0, 6, 2)]
print(slices)