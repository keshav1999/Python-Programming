# num= int(input())
# def squareroot(num):
#     lo=0
#     hi=num
#     mid=(lo+hi)/2
#     while abs(mid*mid -num)>.000001:
#         if num<mid*mid:
#             hi=mid
#             mid=(hi+lo)/2
#         elif num>mid*mid:
#             lo=mid
#             mid=(hi+lo)/2
#     return mid
# print(squareroot(num))


##########    lists
# x=5
#marks=[90,95,100,70,33,40,80]
# print(len(marks))
# print(marks[2])
# print(marks[-7])
#
# #strings are immutable whereas lists are mutable
# marks[0]=91
# print(marks)
#
# print(marks[1:4])
# print(marks[2:])
# print(marks[:4])
# print(marks[1:7:2])
# print(marks[-1::-1])
# print(marks[::-1])

# for i in range(len(marks)):
#     print(marks[i])
# for i in marks:
#     print(i)

# for i,v in enumerate(marks):
#     print(i,v)

# num=int(input())
# def linearsearch(n):
#     l=len(marks)
#     for i in range(l):
#         if marks[i]==num:
#             print("found")
#             return
#     print("not found")
# linearsearch(num)

# print(marks.index(90))
# print(marks.count(90))

# marks.append(85)
# print(marks)
#
# marks.insert(1,85)
# print(marks)
#
# marks.pop()
# print(marks)
#
# marks.pop(1)
# print(marks)
#
# marks.remove(90)
# print(marks)

# num=int()
# list=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# def binarysearch(ls,num):
#     lo=0
#     hi=len(ls)-1
#     while hi>=lo:
#         mid=(lo+hi)/2
#         if ls[mid]==num:
#             print("found")
#             return mid
#         elif ls[mid] < num:
#             lo=mid+1
#         else:
#             hi=mid-1
#     return None
# print(binarysearch(list,num))


# to swap two numbers
# a =4
# b=5
# print(a,b)
# a,b=b,a
# print(a,b)

# a=4
# b=5
# def swap(x,y):
#     x,y=y,x
# swap(a,b)
# print(a,b)


# list=[1,2,3,4,5,6,7,8,9,10]

# def swap(arr,i,j):
#     arr[i],arr[j]=arr[j],arr[i]
# # print(list)
# # swap( list , 0 ,1)
# # print(list)
#
# def reverse(list):
#     j=len(list) -1
#     for i in range(len(list)//2):
#         swap(list,i,j)
#         j-=1
# reverse(list)
# print(list)


# s="Hello World"
# def substrings(s):
#     le=len(s)
#     for i in range(le):
#         a=""
#         for j in range(i,le):
#             a+=s[j]
#             print(a)
# substrings(s)
