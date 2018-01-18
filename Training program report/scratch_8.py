#--------------------------web scraping example-----------

# import urllib.request
# from bs4 import BeautifulSoup as soup
#
# conn = urllib.request.urlopen('https://www.amazon.in/Moto-Plus-Lunar-Grey-64GB/dp/B071HWTHPH?tag=googinhydr18418-21&tag=googinkenshoo-21&ascsubtag=498d931e-e56b-4077-9d3e-9cca3ff01c3f')
# #it returns the binary file
# html_raw = soup(conn, 'html.parser') #it generates html file from that binary file
# list = html_raw.findAll('span',{'class':'a-size-large'},{'id':'productTitle'})[0].text.split()
# string = ''
# for i in list:
#     string =string+ i+' '
#
# print(string)
#-----------------------------------------20 programming examples---------------

#Level1--------------
#question 3--------

# With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#code:
# n=int(input('enter a number\n'))
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i       #means d[key]=value
#
# print(d)

# values=input('enter the numbers')
#
# l=values.split() #splits the values recognizing 'space' and returns a list
# print(l)
# m=list(l)
# print(m)
# n=tuple(l)
# print(n)

#CLASSES and OBJECTS -------very imp point------. A class deﬁnition creates a new class object unlike C++

# for variables a.view() creates shallow copy and a.copy() creates deepcopy
# for objects (of type classes) ,it has "copy" module which provies methods such as copy(), deepcopy()
#     i)shallow_obj=copy.copy(original_obj)------creates shallow copy(i.e. doesnot copy embeddded object of the original object
#     ii)deep_obj=copy.deepcopy(original_obj)------creates a full copy(i.e.also copies embeddded object of the original object

# If you are not sure whether an object has a particular attribute,
# you can use the built-in function hasattr:
# >>> hasattr(p, 'x')
# True
# >>> hasattr(p, 'z')
# False
#-------------------------------------------------------------------------------

#def  __init__(self,hour=0,minutes=0,seconds=0):- is a constructor which contains self and its other parametres should
#                                                  have same name as the class attributes
#                                              ii)it is invoked when an object is instantiated(bcoz its a constructor)

#question 7)---

#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.

# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]


# a=input('enter 2 digits').split(',')
# b=[int(b) for b in a ]
# print(b)
# output=[[0 for j in range(b[1])] for i in range(b[0])]#--------- creating 2D list with zeroes
# for i in range(b[0]):
#     for j in range(b[1]):
#         output[i][j]=i*j
#
# print(output)

#-------------------
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
#
# #code---------
# lines=input('enter the lines in a comma separated sequence').split(',')
# line_list=list(lines)
# for i in line_list:
#     j=i.upper()
#     print(j)



#
# final=string.upper()
# print(final)