import numpy as np
arr = np.arange(0,12)
print(arr)
 
#print(arr[0])
#print(arr[1]) #2nd element
#print(arr[2]) #3rd element

#print(arr[0:3])
#print(arr[2:6])

arr[0:3] = 20
print(arr)

arr2 = arr[0:6]
#print(arr2)

arr2[:] = 29 #all elements are modified
print(arr2)
print(arr)

arrcopy = arr.copy()