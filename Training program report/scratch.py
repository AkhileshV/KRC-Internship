##transpose of a matrix using numpy....

# import numpy
# matrix=[[1,2,3],[4,5,6]]
# print(matrix)
# print("\n")
# print(numpy.transpose(matrix))


##To tell Python, that we want to use the global variable, we have to use the keyword “global”,
##This function modifies global variable 's'

# def f():
#     global s
#     print(s)
#     s = "Look for Geeksforgeeks Python Section"
#     print(s)
#
#
# # Global Scope
# s = "Python is great!"
# f()
# print(s)

#a good example for variable scope (global and local)

# a = 1
#
#
# # Uses global because there is no local 'a'
# def f():
#     print('Inside f() : ', a)
#
#
# # Variable 'a' is redefined as a local
# def g():
#     a = 2
#     print('Inside g() : ', a)
#
#
# # Uses global keyword to modify global 'a'
# def h():
#     global a
#     a = 3
#     print('Inside h():', a)
#
#
# # Global scope
# print('global : ', a)
# f()
# print('global : ', a)
# g()
# print('global : ', a)
# h()
# print('global : ', a)

#code for checking whether a num is even or odd

# from functools import *
#
#
# # A normal function
# def add( a, b, c):
#     return 100 * a + 10 * b + c
#
#
# # A partial function with b = 1 and c = 2
# add_part = partial(add,b=1, c=2)
#
# # Calling partial function
# print(add_part(3))

#packing and unpacking
#for UNPACKING

# def fun(a,b,c,d):
#     print(a,b,c,d)
#
#
# # Driver Code
# my_list = [1, 2, 3, 4]
#
# # This doesn't work
# fun(*my_list)

#for PACKING

# def fun(*args):
#     for i in range(0,len(args)):
#       print(args[i])
#
# # Driver Code
#
# # Unpacking list into four arguments
# fun(1,2,3,4)

#example code for packing and unpacking together

#def fun1(a, b, c):
#    print(a, b, c)


# Another sample function.
# This is an example of PACKING. All arguments passed
# to fun2 are packed into tuple *args.
# def fun2(*args):
#     # Convert args tuple to a list so we can modify it
#     args = list(args)
#
#     # Modifying args
#     args[0] = 'Geeksforgeeks'
#     args[1] = 'awesome'
#
#     # UNPACKING args and calling fun1()
#     fun1(*args)
#
#
# # Driver code
# fun2('Hello', 'beautiful', 'world!')


#end parameter
# This Python program must be run with
# Python 3 as it won't work with 2.7.

# ends the output with '@'
# print("Python", end='@')
# print("GeeksforGeeks")
#----------------------------------------------
# Python code to demonstrate Type conversion
# using int(), float()

# initializing string
s = "10010"

# printing string converting to int base 2
# c = int(s,2)
# print("After converting to integer base 2 : ", end="")
# print(c)
#
# # printing string converting to float
# e = float(s)
# print("After converting to float : ", end="")
# print(e)

#demo for dict()

# tup = (('a', 1) ,('f', 2), ('g', 3))
# # printing tuple converting to expression dictionary
# c = dict(tup)
# print ("After converting tuple to dictionary : ",end="")
# print (c)

#
# Byte objects are sequence of Bytes, whereas Strings are sequence of characters.
# Byte objects are in machine readable form internally, Strings are only in human readable form.
# Since Byte objects are machine readable, they can be directly stored on the disk. Whereas, Strings need encoding before which they can be stored on disk.
