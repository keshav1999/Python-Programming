# list=[1,1,2,2,333,23,22,1,1,2323,232311,1]
# num=1
# count=0
# for i in list:
#     if i==num:
#         count+=1
# print(count)

# s="Hello World"
# a=""
# for i in s:
#     if i>='a' and i<='z':
#         a+=str.upper(i)
#     elif i>='A' and i<='Z':
#         a+=str.lower(i)
#     else:
#         a+=i
# print(a)palindro

# def ispalindrome(s):
#     left=0
#     right=len(s)-1
#     while left<right:
#         if s[left]!=s[right]:
#             return False
#         left+=1
#         right-=1
#     return True
#
#
# s="Hello World"
# def substrings(s):
#     result=[]
#     le=len(s)
#     for i in range(le):
#         a=""
#         for j in range(i,le):
#             a+=s[j]
#             if ispalindrome(a):
#                 result.append(a)
#     return result
# print(substrings(s))



# def swap(arr,i,j):
#     arr[i],arr[j]=arr[j],arr[i]
#
#
# #bubble sort
# list=[1,34,45,2323,545,232,4,67,756,665,5656,6565,454,3]
# def bubblesort(lis):
#     le=len(lis)
#     for i in range(le-1):
#         for j in range(0,le-i-1):
#             if lis[j]>lis[j+1]:
#                 swap(lis,j,j+1)
# bubblesort(list)
# print(list)




# # selection sort
# def selection(lis):
#     le=len(lis)
#     for pos in range(0,le-1):
#         for j in range(1+pos,le):
#             if lis[pos]>lis[j]:
#                 swap(lis,pos,j)
# selection(list)
# print(list)




# insertion
# def insertionsort(arr):
#     le=len(arr)
#     for start in range(1,le):
#         for i in range(start,0,-1):
#             if arr[i]<arr[i-1]:
#                 swap(arr,i,i-1)
#             else:
#                 break
# insertionsort(list)
# print(list)



# 2D arrays

# arr = [1,2,3]
# mat =[[1,2,3],
#        [4,5,6],
#        [7,8,9],]

# print(arr1)
#
# print(arr1[0])
# print(arr1[1][1])
#
# print(len(arr1[0]))
# for i in range(len(arr1)):
#     for j in arr1[i]:
#         print(j)

# numrows=len(mat)
# numcols=len(mat[0])
# for r in range(numrows):
#     for c in range(numcols):
#         print(mat[r][c])

# for row in mat:
#     for col in row:
#         print(col)


# for row in range(numrows):
#     numcols=len(mat[row])
#     for col in range(numcols):
#         print(mat[col][row])

# def waveprinting(mat):
#     numrows = len(mat)
#     numcols = len(mat[0])
#     for c in range(numcols):
#         if c%2==0:
#             for r in range(numrows):
#                 print(mat[r][c])
#         else:
#             for r in range(numrows-1,-1,-1):
#                 print(mat[r][c])


# waveprinting(mat)

# cols=2
# rows=5
# mat2=[[0 for x in range(cols)] for y in range(rows)]
# print(mat2)
#
# mat3=[[0]*cols]*rows
# print(mat3)


