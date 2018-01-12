#------------------DAY3------------

# Write a  function named check_fermat that takes four parameters—a, b, c and n—and that checks to see if Fermat’s theorem holds.
# If n is greater than 2 and it turns out to be true that an +bn = cn the program should print,“Holysmokes,Fermatwaswrong!”
# Otherwise the program should print, “No, that doesn’t work.”

# 2. Write a function that prompts the user to input values for a, b, c and n, converts them to integers,
# and uses check_fermat to check whether they violate Fermat’s theorem.


# import math
# def check_fermat(a,b,c,n):
#     if (n>2) :
#         if(math.pow(a,n)+math.pow(b,n)==math.pow(c,n)):
#             print("Holysmokes,Fermatwaswrong!")
#         else:
#             print('No, that doesn’t work.')
#     else:
#         print('an + bn =',math.pow(a,n)+math.pow(b,n),'\n','cn=',math.pow(c,n))
#
# def fun():
#     a=input('enter the values of a,b,c,n\n')
#     a=list(a)
#     for i in range(0,4):
#         a[i]=int(a[i])
#     check_fermat(*a)
#
# fun()

#---------------fibinacci series(exercise 6.7)

# def fibo(n):
#     n=int(n)
#     if(n==0):
#         return(0)
#     elif(n==1):
#         return(1)
#     else:
#         return(fibo(n-1)+fibo(n-2))
#
# a=input('enter the number u want the fibonacci value for')
# b=fibo(a)
# print('fibonacci value of',a,'is',b)

#for checking types we use isinstance()

# def factorial (n):
#     if (not isinstance(n, int)):
#         print ('Factorial is only defined for integers.')
#         return (None)
#     elif n < 0:
#         print ('Factorial is not defined for negative integers.')
#         return (None )
#     elif n == 0:
#         return (1)
#     else:
#         return (n * factorial(n-1))
#
# factorial(2.5)
# factorial(-2)
# print(factorial(6))

#exercise (6.4)---------to verify the output i got in page 8 of my practice sheets

# def b(z):
#     prod = a(z, z)
#     print (z, prod)
#     return prod
#
# def a(x, y):
#     x = x + 1
#     return x * y
#
# def c(x, y, z):
#     total = x + y + z
#     square = b(total)**2
#     return square
#
# x = 1
# y = x + 1
# print (c(x, y+3, x+y))


#--------------NUMPY---------------

# ---concepts completed today
#
#       *) basics of numpy-- attributes of 'ndarray' object
#       *) creating array using array function
#       *)printing arrays--  arange(),linspace(),reshape()





