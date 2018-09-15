import numpy as np
from matplotlib import pyplot as plt

a = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
b = np.array([[1, 0, 1], [0, -1, 2], [-1, 1, 2]])
print(np.add(a, b))  # add two matrix
print(np.subtract(a, b))
print(np.multiply(a, b)) # result[1][1]=a[1][1]*b[1][1] only. it doesn't multiply as we want
# So to do this we use dot function
# print(np.divide(a,b))
print(np.invert(a))
print(np.power(a, 5))
print(np.square(a))
print(np.add(a, np.array([1, 2, 3])))
print(a * 2)  # it will multiply all the elements of matrix with 2
print(a + 2)
print(a % 2)
print(np.mean(a))  # apply mean in whole array
# 4.333333333333333
print(np.mean(a, axis=0))  # apply mean operation in column
# [3.33333333 4.33333333 5.33333333]
print(np.mean(a, axis=1, dtype=int))  # apply mean operation in row
# [2 4 7]

# standard deviation
# formula for std = sqrt(mean(abs(x - x.mean())**2))
print(np.std([1,2,3,4])) # 1.118033988749895

# formula for variance var = mean(abs(x - x.mean())**2)
print(np.var([1,2,3,4])) # 1.25


# Inverse of a matrix

x = np.array([[1,2],[3,4]])
y = np.linalg.inv(x) # iverse of matrix
print(x)
print(y)
print(np.dot(x,y)) # checking identity matrix
print(np.identity(5))


x = np.arange(1,11)
y = 2 * x + 5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")

# Below ms-radius of plotted point
plt.plot(x,y,"ro",ms=10) # r here refers to red color which will be our line color
# plt.plot(x,y+20,'o') # o referes to type of type of line style
plt.show()
