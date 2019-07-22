# 1. Write a function that takes as input a Fahrenheit value and returns the corresponding Celsius value.
# N =float(input("Enter the temprature in fahrenheit "))
# def tempconv(x):
#     celcius= (5/9)*(x-32)
#     print(celcius)
# tempconv(N)
# 2. Write another function that takes as input 3 values:
# a. start - This represents the starting Fahrenheit value
# b. end - This represents the ending Fahrenheit value
# c. step - This represents the increment you need to make after each value
# Now run a loop from start to end, increasing the value by step each time. Each value in the loop represents a Fahrenheit value that you have to convert into Celsius. “Call” the function you had created in previous question to do the conversion from F to C.
# Print as output the following table, with Fahrenheit values in left column and Celsius values in the right column. e.g. for an input of 0 (start), 100 (end) and 20 (step) the output is:
#                                         
# 0 : -17
# 20 : -6
# 40 : 4
# 60 : 15
# 80 : 26
# 100 : 37
# start=int(input("Enter the starting value"))
# end=int(input("Enter the ending value"))
# step=int(input("Enter the step value"))
# for i in range(start,end+1,step):
#     tempconv(i)
# 3. Take as input a character ch (eg: ‘g’, ‘h’, ‘A’, ‘5’, ‘+’). Write a function that returns ‘U’ if the character is uppercase, ‘L’ if it is lowercase, and ‘I’ otherwise. Print the value returned.
# chr=input()
# def getchar(chr):
#     if chr>="A" and chr<="Z":
#         return ("U")
#     elif chr>="a" and chr<="z":
#         return("L")
#     else:
#         return ("I")
# print(getchar(chr))

# 4. Take as input a number. Write a functions which returns true if the number is Armstrong number and false otherwise. Print the value returned.
# An Armstrong number is defined as follows
# E.g. 371 is an Armstrong number as 371 = 33 + 73 + 13
# N= int(input())
# def isarmstrong(x):
#     orignal=x
#     num=0
#     while(x!=0):
#         num+=(x%10)**3
#         x=x//10
#     return num==orignal
# if isarmstrong(N):
#     print(str(N) +" is an armstrong number")
# else:
#     print("Not an armstrong number")

# 5. Take as input two numbers N1 and N2. Write a function to print all Armstrong numbers between N1 and N2. HINT: “Call” the function from previous question inside this function.
# N1=int(input())
# N2 = int(input())
# for i in range(N1,N2+1):
#     if isarmstrong(i):
#         print(i)

# 6. Take as input the following
# a. A number (eg: 31416)
# b. A digit (eg: 1)
# Write a function that returns the number of times digit is found in the number. Eg: 1 is found 2 times in 31416 Print the value returned.
# N=int(input("Enter a number "))
# a=int(input("enter the digit "))
# def countdigit(x,y,count):
#     while x!=0:
#         if (x%10)==y:
#             count+=1
#         x=x//10
#     return count
# print(countdigit(N,a,0))

# 7. Take as input two numbers N1 and N2. Write a function which calculates and returns the GCD ( = HCF ) of two numbers. Print the value returned.
# N1=int(input("enter the 1st number "))
# N2=int(input("enter the second number and greaterone "))
# def GCD(N1,N2):
#     for i in range(1,N1+1):
#         if N1%i==0 and N2%i==0:
#             max=i
#     return max
# print(GCD(N1,N2))

# 8. 8. Take as input two numbers N1 and N2. Write a function which calculates and returns the LCM of two numbers. Print the value returned. HINT: N1 x N2 = GCD x LCM
# N1=int(input("Enter the first number "))
# N2=int(input("Enter the second number "))
# def LCM(N1,N2):
#     lcm=(N1*N2)/GCD(N1,N2)
#     return lcm
# print(LCM(N1,N2))

# 9. Take as input two numbers x and n. Write a function which calculates and returns the xn. Print the value returned.
# x=int(input("Enter the vslue of x"))
# n= int(input("enter the value of n"))
# def pow(x,n):
#     ans=x
#     for i in range(1,n):
#         ans=ans*x
#     return ans
# print(pow(x,n))

# 10. Take as input two numbers x and n. Write a function which calculates and returns the Logn(x) of two numbers. Print the value returned. Assume that values of x and n are such that the result is going to be a whole number.
# x=int(input())
# base=int(input())
# def lognX(a,b):
#     count=0
#     while a!=0:
#         a=a//b
#         count+=1
#     return count-1
# print(lognX(x,base))
# 11. Take as input two numbers N1 and N2. Write a function which prints first N1 terms of the series 3n + 2 which are not multiples of N2.
# N1=int(input("Enter a number "))
# N2=int(input("Enter second number "))
# def series(N1,N2):
#     for i in range(N1+1):
#         if (3*i+2)%N2!=0:1
#             print(i)
# series(N)
#

# 12.
# 13. 13. Write a program that works as a simple calculator. It reads two integers and a character.
# If the character is +, the sum is printed.
# If it is -, the difference is printed.
# If it is *, the product is printed.
# If it is /, the quotient is printed.
# If it is %, the remainder is printed.
# If the user enters 'X' or 'x', the program exits, otherwise again asks for two numbers and a new operation.

# def calculatoer():
#     c=input()
#     while c!='x' and c!='X':
#         a = int(input())
#         b = int(input())
#
#         if c =='+':
#             print(a+b)
#         elif c =='-':
#             print(a-b)
#         elif c=='*':
#             print(a*b)
#         c=input()
# calculatoer()

# 14. Take as input a number. Assume that for a number of n digits, the value of each digit is from 1 to n and is unique. E.g. 54123 is a valid input number.
# Write a function that returns its inverse, where inverse is defined as follows
# Inverse of 54123 is 34521.
# In 54123, “5” is at 1st place, therefore in 34521, “1” is at 5th place.
# In 54123, “4” is at 2nd place, therefore in 34521, “2” is at 4th place.
# Print the value returned.

a=input()
l=len(a)
arr=[]
for i in range(l):
    arr.append(int(a[i]))
def inverse(lists):
    b=[]
