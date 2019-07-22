# x=int(input("Enter the vslue of x"))
# n= int(input("enter the value of n"))
# def pow(x,n):
#     ans=x
#     for i in range(1,n):
#         ans=ans*x
#     return ans
# print(pow(x,n))
# a=int(input())
# b=int(input())
# def hcf(a,b):
#     if a==0 or b==0:
#         return max(a,b)
#     elif a>=b:
#         return hcf(a%b,b)
#     else:
#         return hcf(a,b%a)
#print(hcf(a,b))
# def hcf(a,b):
#     while a!=0 and b!=0:
#         if a>b:
#             a=a%b
#         else:
#             b=b%a
#     return max(a,b)
# # print(hcf(a,b))
# def lcm(a,b):
#     return (a*b)/hcf(a,b)
# print(lcm(a,b))
# N=int(input())
# X=int(input())
# count=0
# while X!=1:
#     X//= N
#     count+=1
# print(count)
# def log(base ,x):
#     hi=x
#     lo=0
#     y=(hi+lo)/2
#     pow=base**y
#     while abs(pow-x)>.000001:
#         if pow>x:
#             hi=y
#         else:
#             lo=y
#         y=(hi+lo)/2
#         pow=base**y
#     return y
# print(log(N,X))



# STRINGS
# s = "Hello world"
# # print(len(s))
# # print(s[1:5])
# # print(s[1:10:2])
# # print(s[9:1:-1])
# print(s.index("o"))
# print(s.index("o",5))
# print(s.count("o"))
# print(s.upper())
# print(s.lower())
# print(s.startswith("Hello"))
# print(s.endswith("d"))
# print(s.split("l"))
# print(s.split())
# for i in range(0,len(s)):
#     if s[i]!=" ":
#         print(s[i])
# for v in s:
#     print(v)
# a="abcba"
# def ispalen(s):
#     flag=True
#     for i in range(len(s)//2-1):
#         if s[i]==s[i+(len(s)/2)+1]:
#             flag=True
#         else:
#             flag=false
#             break
#     return flag
# if ispalen(a):
#     print("Yes")
# else:
#     print("No")

s="abcdef"
print(s[0:3])