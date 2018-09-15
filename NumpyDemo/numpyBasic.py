import numpy as np

a = np.array([1, 2, 3, 4], dtype=complex)  # dtype set the type of array either complex or simple
print(a)  # [1.+0.j 2.+0.j 3.+0.j 4.+0.j]

a = np.array([1, 2, 3], ndmin=2)  # ndmin is the dimension of matrix which we want to get
print(a)  # [[1 2 3]]

a = np.array([[1, 2], [3, 4]])
print(a)  # [[1 2]
#           [3 4]]

dt = np.dtype([('age', np.int8)])  # int8 is the data type object in numpy int 8
# can also be represented in 'i1'.
# In Above function int8 is the name of datatype of filename 'age'

print(dt)  # [('age', 'i1')]

# apply this above dt to array
a=np.array([(10,),(20,),(30,)],dtype=dt)
print(a) #[(10,) (20,) (30,)]
print(a['age']) # [10 20 30]

# S20-for string i1- for int8 f4-for float 128
# Below one is the structured data type(custom or user deifned data type)
dt=np.dtype([('name','S20'),('age','i1'),('marks','f4')])
print(dt) # [('name', 'S20'), ('age', 'i1'), ('marks', '<f4')]

a=np.array([('arvind',19,23.04),('anisha',20,43.4)],dtype=dt)
print(a) # [(b'arvind', 19, 23.04) (b'anisha', 20, 43.4 )]
print(a['name']) # [b'arvind' b'anisha']
print(a['age']) # [19 20]
print(a['marks']) # [23.04 43.4 ]

a=np.array([[10,20,30],[1,2,3]])
a.shape=(3,2) # convert array a into 3 rows 2 columns
print(a)

b=a.reshape(3,2)
print(b)

a=np.zeros((3,2),dtype=np.int8) # intialize array a with zeroes and having dimension
# 3 rows and 2 columns
print(a)

# Slicing array
a=np.arange(20) # it will make an 1d array and filled it by 1,2,3...20
print(a) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
a=a[2:17:2] # 2 is starting index,& is end index and 2 is step
print(a) # [ 2  4  6  8 10 12 14 16]

# array to begin with
a = np.array([[1,2,3],[3,4,5],[4,5,6]])

print ('Our array is:' )
print (a)
print('\n')

# this returns array of items in the second column
print ('The items in the second column are:')
print (a[...,1])  # '...' ellipses
print ('\n')

# Now we will slice all items from the second row
print ('The items in the second row are:')
print (a[1,...])
print ('\n')

# Now we will slice all items from column 1 onwards
print ('The items column 1 onwards are:')
print (a[...,1:])

