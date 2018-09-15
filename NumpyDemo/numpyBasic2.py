import numpy as np

a=np.arange(0,60,5) # step=5
a=a.reshape(3,4)# 3 rows 4 columns
print(a)

# nditer is an iterator
for x in np.nditer(a):
    print(x)

b=a.T # Transpose of a matrix
print(b)

for x in np.nditer(a,order='F'): # it will iterate through column wise from up to down
    print(x)
for x in np.nditer(a,order='C'): # it will iterate through row wise from left to right
    print(x)

# Modifying array values

for x in np.nditer(a,op_flags=['readwrite']):
    x[...]=2*x
print("After Modifying the array")
print(a)

# Trignometric functions
a=np.array([0,30,45,60,90])
# converting degree into radian
cos=np.cos(a*np.pi/180)
print(cos)

print(np.arccos(cos)*180/np.pi) # inverse of cos



