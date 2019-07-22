# from functools import reduce
# maps
# def double(x):
#     return 2*x
# arr= [1,2,3,4]
# arr2 = list(map(double,arr))
#
# print(arr2)


# arr=[1,2,3,4]
# arr2=list(map(lambda x:x*x,arr))
# print(arr2)
# print(arr)

# filter
# arr3 = list(filter(lambda x:x%2==0,arr))
# print(arr3)
#
# double = lambda x : 2*x
# print(double(5))

# reduce

# print(reduce(lambda x,y : x+y,arr))

# feets=[1,2,3,4.5,6.7,-1,0]
# arr=(list(filter(lambda x : x>=0,feets)))
# arr1= list(map(lambda x : x*12,arr))
# arr2= reduce(lambda x,y : x+y,arr1)
# print(arr)
# print(arr1)
# print(arr2)

# a=[1,2,3,4]
# b=[2,2,4,4]
# c=[0,1,0,1]
# d= list(map(lambda x,y,z:x+y+z,a,b,c))
# print(d)

# z=list(zip(a,b))
# print(z)
#
# z1=dict(zip(a,b))
# print(z1)

# from functools import partial
# def multiply(x,y):
#     return x*y
# double = partial(multiply,2)
# print(double(3))
# def pow(x,y):
#     return y**x
# square = partial(pow,2)
# print(square(5))
#
#
# square = lambda a:pow(a,2)
# print(square(4))
#





# sentence = "the tallest tree in the forest is also the oldest tree"
# words = sentence.split()
# result = [word for word in words if word!="in" and word!="is"]
# print(result)
# # mat= [[-1]*numcols for i in numrows]
#
# result1= list(filter(lambda x: x!="in" and x!="is",words))
# reslut2= list(map(lambda s:len(s),result1))
# print(result1)
# print(reslut2)




# import re
# pattern = re.compile(r"[a-zA-Z0-9]+@gmail.com")
# result= re.search(pattern,"My email is coding@gmail.com")
# print(result)
# print(result.start())
# print(result.end())
# print(result.group(0))
# web ="(http[s]?:\/\/)?www.[a-zA-Z0-9]+.com" # can be checked in pattern


import random
random.seed()
print(5 + random.random()*5)

