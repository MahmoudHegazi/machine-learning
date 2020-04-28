#write a python program that generates
#a 20 * 20 array of integer random variables between 0 and 255

import numpy as np

np.random.randint(255, size=(20, 20))


# python program create 5 arrays with 2 number for each array
print("\nUse numpy to create a [5,2] dimension array with random number")
c = np.random.rand(5, 2)
print(c)

