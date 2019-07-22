# sum=0
# for i in range(10,21):
#     sum=sum+i
# print(sum)
#
# inp=input()
# while inp!="Quit" and inp!="exit":
#     print(inp)
#     inp=input()
# for i in range(1,6):
#     print("*"*i)
#
# counter=1
# for i in range(1,5):
#     s=""
#     for j in range(1,i+1):
#         s= s + str(counter)
#         counter=counter+1
#     print(s)
# ch =input()
# if ch>="A" and ch<="Z":
#     print("upper")
# elif ch>="a" and ch<="z":
#     pprint("lower")
# else:
#     print("independent")
# ans=0
# num =int(input())
# while num!=-0:
#     ans=ans*10 +num%10
#     num=num//10
# print(ans)
# x=int(input())
# a=0
# b=1
# while True:
#     c=a+b
#     a=b
#     b=c
#     if c<x:
#         print(c)
#     else:
#         break
# def f(x):
#     y=2*x
#     print(y)
# f(2)
# f(5)
# def area(a,b):
#     ar=a*b
#     return ar
# a1=area(4,6)
# a2=area(2,4)
# print(a2)
# def isprime(x):
#     flag=True
#     for i in range(2,int(x**0.5)+1):
#         if x%i==0:
#             return False
#     return True
# x=int(input())
# c=isprime(x)
# if c:
#     print("prime")
# else:
#     print("not a prime")
# def isupper(x):
#     return x>="A" and x<="Z"
# if isupper("U"):
#     print("Upper case")
# else:
#     print("Lower case")

# def getoccur(x,y):
#     count=0
#     while x!=0:
#         if x%10==y:
#             count=count+1
#         x = x//10
#     return count
# y=getoccur(11211,1)
# print(y)
# l=int(input())
# def isarm(x):
#     cube=0
#     orignal=x
#     while x!=0:
#         cube= cube + (x%10)**3
#         x=x//10
#     return orignal==cube
# # p=isarm(l)
# # if l==p:
# #     print("armstrong")
# # else:
# #     print("not an armstrong")
# for i in range(1,10010):
#     if isarm(i):
#         print(i)
# for i in range(1,1001):
#     if isprime(i):
#         print(i)
