#--------------NUMPY---------------

# ---concepts completed today (refer to the sheets( page 9 & 10 )
#
#       *) basics of numpy-- attributes of 'ndarray' object
#       *) creating array using array function
#       *)printing arrays--  arange(),linspace(),reshape()


# from math import pi
# import numpy as np
# a=np.ones(3, dtype=np.int32)
# b=np.linspace(0,pi,3)
# c=np.add(a,b) or c=a+b is also correct
# print(c)
# d=np.exp(c*1j)
# print(d)
# print(d.dtype.name)


# many unary operatons such as sum of all the elements of an array are implemented as methods of the 'ndarray' class
#example

# import numpy as np
# a=np.random.random((2,3))
# print(a)
# print(a.sum())----------------#performs sum of all the elemnts of array

#print(a.sum(axis=0))----------#axis=0 indicates row operation
                               #axis=1 indicates column operation
#example

# import numpy as np
# a=np.random.random((2,3))
# print(a)
# print(a.sum(axis=0))  #-----------prints the sum of rows of the array a
# print(a.sum(axis=1))  #-----------prints the sum of columns of the array a

#indexing , slicing and iterating--------------------------------
# 1D array

# import numpy as np
# a=np.arange(10)**3
# print(a)
# print(a[2:5]) #prints [ 8 27 64]
# a[:6:2]=-1000 #-----------means from the first posiiton till 6th [position ,assign -1000 to every 2nd element
# print(a)  # prints [-1000     1 -1000    27 -1000   125   216   343   512   729]
# #for reversing the array
# print(a[ : :-1]) #prints [  729   512   343   216   125 -1000    27 -1000     1 -1000]
# print(a[ : :-2]) #prints [729 343 125  27   1]

#for 2D array

# import numpy as np
# def f(x,y):
#     return(10*x+y)
#
# b=np.fromfunction(f,(5,4),dtype=int)
# print(b)
# print(b[1:3,1:3])
# print(b[ : ,2])
#
# #for getting the last row its b[-1]
# #b[-1] is equivalent to b[-1, : ] that is
# print(b[-1])
# print(b[-1,2:4]) #----------last row ,,,values in col 2 & 3 i.e 42 & 43
# print(b[ : ,-1])

#for 3D array
#refer path: numpy.org/numpy tutorial/indexing,slicing and iterating

#for iterating over multidimansional array

# import numpy as np
# def f(x,y):
#      return(10*x+y)
# b=np.fromfunction(f,(5,4),dtype=int)
# for i in b.flat:
#     print(i)


# import numpy as np
# a=np.floor(10*np.random.random((3,4)))
# print(a)
# print(a.shape)
# print(a.ravel())  #----------->ravel() is the method used to return the flattened array.-----------
# print(a.reshape(6,2))
# #-------------a.T is used to return the transpose of the array
# print(a.T)
# #--------------  -1 indicates last index....hence
# print(a.reshape(3,-1)) #------------returns the reshaped array
# print(a.reshape(2,6))
# print(a.resize(3,4)) #------- resize() performs reshape but returns only 'None'

#--------------------------------NEWAXIS ---------

# import numpy as np
# from numpy import newaxis
# a=np.array([4.,2.,3.])
# print(a[ : ,newaxis]) #-------basically transforms a 1D array into 2D column vector


#import numpy as np
# a = np.floor(10 * np.random.random((2, 12)))
# print(np.hsplit(a,3))   # Split a into 3
# print(np.hsplit(a,(3,4)))   # group col 3 as one(4 not included bcoz its the last value) and the remaining as 2 more
#                              # irrespective of number of parts the array has to be divided
# print(np.hsplit(a,(3,5)))   # group col 3 and 4 as one(5 not included bcoz its the last value) and the remaining as 2 more
#                              # irrespective of number of parts the array has to be divided


#-----------------LINEAR OPERATIONS on arrays--------------------

#a.transpose() --------------the function used for finding the transpose of the array ,matrix
#np.linalg.inv(a)---------------to find the inverse of the matrix
#u = np.eye(2) # unit 2x2 matrix; "eye" represents "I"
#a.shape = (2,-1,3) ----------------------- # -1 means "whatever is needed"





















