import sys

import numpy as np


l = range(1000)

print(sys.getsizeof(2))

array = np.arange(1000)
print(array.itemsize)

print(type(l))