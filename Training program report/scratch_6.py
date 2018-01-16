#[ref:https://www.geeksforgeeks.org/file-objects-python/]

# -----------------------------Appending a file------------------------

# f = open('F:\words.txt', 'a')
# lines = 'Welcome Geeks\n'
# f.write(lines)
# f.close()

#----------------------------------------------------------------------------------
#------------tell(): It returns an integer that tells us the file object’s position
# from the beginning of the file in the form of bytes
# Telling the file object position


# f = open('F:\words.txt', 'r')
# lines = f.read(10)
# print(lines)

# #tell()
# print(f.tell())
# f.close()
#----------------------------------------------------------------------------------------
#--------------------seek(offset, from_where): It is used to change the file object’s position.
#  ( Offset )indicates the number of bytes to be moved.
#   (from_where/whence) indicates from where the bytes are to be moved.-----[this argument is optional and defaults to 0,
#   which means absolute file positioning,
#   other values are 1 which means seek relative to the current position and 2 means seek relative to the file's end.]
#                                     [ref:https://www.tutorialspoint.com/python/file_seek.htm]
# Setting the file object position
# f = open('F:\words.txt', 'r')
# lines = f.read(10)
# print(lines)



# f = open('F:\words.txt', 'r')
# lines = f.read()
# print('from the beginning\n',lines)
#
# # seek()
#
# (f.seek(2, 0))
# lines = f.read()
# print('after seeking 2 positions from the beginning\n',lines)
# f.close()

#------------------------------------------------------------------

#Exercise 14.6.[ref:thinkpython] The urllib module provides methods for manipulating URLs and downloading information from the web.
# The following example downloads and prints a secret message from thinkpython.com:


#[[ urllib ]]is a package that collects several modules for working with URLs:
#   Modules available---

#  * urllib.request for opening and reading URLs
#  * urllib.error containing the exceptions raised by urllib.request
#  * urllib.parse for parsing URLs
#  * urllib.robotparser for parsing robots.txt files
#[ref:https://docs.python.org/3/howto/urllib2.html]

# import urllib.request
# conn = urllib.request.urlopen('http://thinkpython.com/secret.html')
# for line in conn:
#     print (line.strip())
#Run this code and follow the instructions you see there. Solution: http://thinkpython.com/ code/zip_code.py.




