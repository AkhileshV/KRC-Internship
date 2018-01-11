#-----------------DAY 2-----------

#print('spam'*3)

# Suppose  the cover price of a book is $24.95, but book stores get a 40 % discount.Shipping costs $3
# for the ﬁrst copy and 75cents for each additional copy.What is the total wholesale cost for
# 60
# copies?

#exercise 2.5 of  thinkpython book
#[[example 2]]
#--------------------------------------------------------
# copy1=0.6*24.95+3
# rest_of_copies=(0.6*24.95+0.75)*59
# total=copy1+rest_of_copies
# print(total)

##[[example 3]]
#---------------------------------------------------------
# #If I leave my house  at 6: 52 am and run 1 mile at  an easy
# pace(8: 15 per mile), then  3  miles  at  tempo(7: 12 per  mile)
# and 1 mile  at easy pace  again, what  time  do  I get home for breakfast?
# total=[0,0,0]
# initial=[6,52,0]
# easy_pace=[8,15]
# tempo=[7,12]
# for i in range(1,3):
#   total[i]=easy_pace[i-1]*2+tempo[i-1]*3
# for i in range(0,3):
#   initial[i]+=2*total[i]
# while(initial[2]>=60):
#     initial[1]+=1
#     if(initial[1]>=60):
#         initial[0]+=1
#         initial[1]-=60
#     initial[2]-=60
# print('he will reach his home back at:\n ',initial[0],':',initial[1],':',initial[2],' am')

# def print_lyrics():
#     print( "I'm a lumberjack, and I'm okay.")
#     print( "I sleep all night and I work all day.")
# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()
#
# repeat_lyrics

#to get the pattern specified in exercise 3.5 page 30

# def fun1():
#     print('+','- '*4,'+','- '*4,'+')
# def fun2():
#     for i in range(0,4):
#         print('|','  '*4,'|','  '*4,'|')
#
# fun1()
# fun2()
# fun1()
# fun2()
# fun1()


#to find the factorial using recurssion funtion-------------

# def fact(n):
#     if(n==0 or n==1):
#         return(1)
#     else:
#        return(n*fact(n-1))
#
#
# s=fact(5)
# print(s)



