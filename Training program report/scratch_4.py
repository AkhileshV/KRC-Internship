#-------------------------DAY 5-----------------

# Naturally, we can put i and j in a sequence (say a list) and then do the indexing with the list.
#
# >>>
# >>> l = [i,j]
# >>> a[l]                                       # equivalent to a[i,j]
# array([[ 2,  5],
#        [ 7, 11]])
# However, we can not do this by putting i and j into an array,
# because this array will be interpreted as indexing the first dimension of a.
#
# >>>
# >>> s = np.array( [i,j] )
# >>> a[s]     -----------------generates error----

#and some concepts of files i have completed
