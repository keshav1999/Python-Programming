# 1. Take as input N, a number. Print odd numbers in decreasing sequence (up until 0) and even numbers in increasing sequence (up until N). E.g. for N = 6 print 5, 3, 1, 2, 4.
# N= int(input())
#
# def func(n):
#     def oddsequence(n):
#         if n == 0:
#             return
#         if n % 2 != 0:
#             print(n)
#         oddsequence(n - 1)
#
#     def evensequence(n):
#         if n == 0:
#             return
#         evensequence(n - 1)
#         if n % 2 == 0:
#             print(n)
#
#     oddsequence(n)
#     evensequence(n)
# func(N)


#2. Take as input N, a number. Print the following pattern (for N = 5)

# *
# * *
# * * *
# * * * *
# * * * * *

# N=int(input())
# def pattern(n):
#     if n==0:
#         return
#     pattern(n-1)
#     s=""
#     for i in range(n):
#         s+='* '
#     print(s)
# pattern(N)


# 3 3. Take as input N, a number. Print the following pattern (for N = 5)
#
# * * * * *
# * * * *
# * * *
# * *
# *
# N=int(input())
# def pattern(n):
#     if n==0:
#         return
#     s=""
#     for i in range(n):
#        s+= '* '
#     print(s)
#     pattern(n-1)
# pattern(N)


# 5 5. Take as input N, a number. Write a recursive function to find Nth triangle where
# 1st triangle is 1, 2nd triangle is 1 + 2 = 3, 3rd triangle is 1 + 2 + 3 = 6, so on and so forth. Print the value returned.

# N=int(input())
# def nthtriangle(n,sum):
#     if n==0:
#         return 0
#     return n + nthtriangle(n-1,sum)
# print(nthtriangle(N,0))


#
# 6. Take as input N, the size of array. Take N more inputs and store that in an array. Write a recursive function which returns true if the array is sorted and false otherwise. Print the value returned.
# N=int(input())
# arr=[]
# for i in range(N):
#     n=int(input())
#     arr.append(n)
# def issorted(lis,i):
#     if i == (len(lis)-1):
#         return True
#     return (lis[i]<=lis[i+1]) and issorted(lis,i+1)
#
# print(issorted(arr,0))

# 7. 7. Take as input N, the size of array. Take N more inputs and store that in an array. Take as input M, a number. Write a recursive function which returns true if M is contained in the array and false otherwise. Print the value returned.


# N= int (input("Enter the length of the array"))
# arr=[]
# for i in range(N):
#     arr.append(int(input()))
# M= int(input("Enter no to be searched"))
# def isnum(arr1,n,m):
#     if n<0:
#         return False
#     return arr[n]==m or isnum(arr1,n-1,m)
# print(isnum(arr,N-1,M))

#8. Take as input N, the size of array. Take N more inputs and store that in an array. Take as input M, a number. Write a recursive function which returns the first index at which M is found in the array and -1 if M is not found anywhere. Print the value returned.

# def isnum2(arr2,n,m,i):
#     if i==n:
#         return -1
#     if arr2[i]==m:
#         return i
#     else:
#          return isnum2(arr2,n,m,i+1)
# print(isnum2(arr,N,M,0))

# 9. Take as input N, the size of array. Take N more inputs and store that in an array. Take as input M, a number. Write a recursive function which returns the last index at which M is found in the array and -1 if M is not found anywhere. Print the value returned.


# def isnum3(arr2,n,m,i):
#     if i<0:
#         return -1
#     if arr2[i]==m:
#         return i
#     else:
#          return isnum3(arr2,n,m,i-1)
# print(isnum3(arr,N,M,N-1))



#  10. Take as input N, the size of array. Take N more inputs and store that in an array. Take as input M, a number. Write a recursive function which returns an array containing indices of all items in the array which have value equal to M. Print all the values in the returned array.
# res=[]
# def isnum4(arr2,n,m,i,result):
#     if i==n:
#         return result
#     if arr2[i]==m:
#         result.append(i)
#         return isnum4(arr2,n,m,i+1,result)
#     else :return isnum4(arr2,n,m,i+1,result)
# print(isnum4(arr,N,M,0,res))


# 11 ake as input N, a number. Take N more inputs and store that in an array. Write a recursive function which tests if the array is a palindrome and returns a Boolean value. Print the value returned.
# N= int (input("Enter the length of the array"))
# arr=[]
# for i in range(N):
#     arr.append(int(input()))
# def ispalindrome(arr,n,i):
#     if i==n//2:
#         return True
#     return  arr[i]==arr[n-i-1]   and ispalindrome(arr,n,i+1)
# print(ispalindrome(arr,N,0))

#12 Take as input N, a number. Take N more inputs and store that in an array. Write a recursive function which reverses the array. Print the values of reversed array.
# def swap (a,i,j):
#     a[i],a[j]=a[j],a[i]
# def reverse(arr,n,i):
#     if i>=n//2:
#         return
#     swap(arr,i,n-i-1)
#     reverse(arr,n,i+1)
# reverse(arr,N,0)
# print(arr)

# 13 Take as input N, a number. Take N more inputs and store that in an array. Write a recursive function which inverses the array. Print the values of inverted array.

# arr1=[-1]*N
# def invert(ar,ar1,n,i):
#     if i==n:
#         return
#     ar1[ar[i]-1]=i+1
#     invert(ar,ar1,n,i+1)
# invert(arr,arr1,N,0)
# print(arr1)

# 14 Take as input N, the size of array. Take N more inputs and store that in an array. Write a recursive function which bubble sorts the given array. Print all the values in the sorted array.

# def bubblesort(ar,n,i):
#     if i==n :
#         return
#     bubblesort(ar,n,i+1)
#     if ar[i]<ar[i-1]:
#         swap(ar,i,i-1)
#     bubblesort(ar,n,i+1)
# bubblesort(arr,N,1)
# print(arr)