# 1. Write a program to print all natural numbers from 1 to 25.
# for i in range(1,26):
#     print(i)

# 2. Write a program to print all natural numbers in reverse (from 30 to 1).
# for i in range(30,0,-1):
#     print(i)

# 3. Write a program to print all odd numbers between 1 and 100 inclusive.
# for i in range(1,100):
#     if i%2!=0:
#         print(i)
# 4.  Write a program to find the sum of all natural numbers between 1 and 50 inclusive.
# sum=0
# for i in range(1,61):
#     sum=sum+i
# print(sum)
# 5 . Write a program to find the sum of all even numbers between 1 to 50 inclusive.
# sum=0
# for i in range(1,51):
#     if i%2==0:
#         sum=sum+i
# print(sum)
# 6 . Given a number ‘num’, find its factorial. (Factorial of 7 = 7! = 7 x 6 x 5 x 4 x 3 x 2 x 1)
# num=7
# prod=1
# for i in range(1,num+1):
#     prod*=i
# print(prod)
# 7. Given two integers a and b, find the value of a raised to power b. Ex: a=2, b=3 will give 8.
# a = 2
# b = 3
# result=1
# for i in range(b):
#     result*=2
# print(result)
# 8. Write a program to print multiplication table (upto 10) of any number saved in variable ‘num’.
# num=4
# for i in range(1,11):
#     print(num*i)
# 9.  Write a program to check whether a number is Prime number or not.
# num=67
# rang=int(num**0.5)
# flag=True
# for i in range(2,rang+1):
#     if num%i==0:
#         flag=False
#         break
# if flag:
#     print("Prime")
# else:
#     print("not a prime")
#10.Write a program to print all Prime numbers between 1 and 100.
# for i in range(1,101):
#     rang = int(i ** 0.5)
#     flag = True
#     for j in range(2, rang + 1):
#         if i % j == 0:
#             flag = False
#             break
#     if flag:
#         print(i)
# 11. Ask user to enter a command. If the command is not “x” print the command and ask for the next command. Keep repeating, until the user enters “x”.
# a=input()
# while(a!="x"):
#     print(a)
#     a=input()
# 12. 12. Write a program to print the following triangle using for-loop.
# HINT: First figure out how to print multiple stars on the same line.
# In Java, use System.out.print instead of System.out.println
# In JS and Python, keep adding stars into an empty string. Then print the entire string at once.
# In C++, this is not an issue because endl is used explicitly.
#
# *
# **
# ***
# ****
# *****
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*"*i)
#         break
# 13. Write a program to print the following triangle using for-loop.
#
#
#     *
#    ***
#   *****
#  *******
# *********
# numspaces=4
# numstars=1
# for row in range(1,6):
#     s=""
#     for col1 in range(numspaces):
#         s+=" "
#     for col1 in range(numstars):
#         s+="*"
#     print(s)
#     numspaces-=1
#     numstars+=2

