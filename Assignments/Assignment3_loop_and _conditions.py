# 1. Take N as input. If the number is prime, print “Prime” otherwise print “Not Prime”.
# N = int(input())
# Flag= True
# for i in range(2,( int(N**0.5) + 1)):
#     if N%i==0:
#         Flag=False
#         break
# if Flag:
#     print("Prime")
# else:
#     print("Not a Prime")
# 2. Take N as input. Print all prime numbers from 2 to N.
# N = int(input())
# for i in range(2,N):
#     flag=True
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             flag=False
#             break
#     if flag:
#         print(i)
# 3. Take N as input. Calculate and print its reverse. Ex: 3247 will output 7423.
# num=int(input())
# ans=0
# while num!=0:
#     ans=ans*10 + num%10
#     num=num//10
# print(ans)
# 4. Take N as input. Print the sum of its odd placed digits and sum of its even placed digits.
# num = int(input())
# i=1
# oddsum=0
# evensum=0
# while num!=0:
#     if i%2!=0:
#         oddsum = oddsum + num%10
#     else:
#         evensum = evensum + num%10
#     i=i+1
#     num=num//10
# print(oddsum)
# print(evensum)
# 5. Take N as input. Print all Fibonacci numbers less than N.
# N= int(input())
# a=0
# b=1
# c=a+b
# while c<N:
#     print(c)
#     a=b
#     b=c
#     c=a+b

# 6. Take N as input. Print Nth Fibonacci number. 0 is the 0th Fibonacci number and 1 is 1st Fibonacci number.
# N=int(input())
# Num=N
# a=0
# b=1
# for i in range(1,N-1):
#     c=a+b
#     a=b
#     b=c
# if N==1:
#     print(0)
# elif N==2:
#     print(1)
# else:
#     print(c)
# 7. Take N (number of rows), print the following pattern (for N = 4)
#                            
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# N=int(input())
# counter=1
# for i in range(1,N+1):
#     s=""
#     for j in range(1,i+1):
#         s+=" "+str(counter)
#         counter+=1
#     print(s)

# 8. Take N (number of rows), print the following pattern (for N = 5)
#                            
# 1
# 2 2
# 3 0 3
# 4 0 0 4
# 5 0 0 0 5

# N=int(input())
# for i in range(1,N+1):
#     if i<=2:
#         s=""
#         for j in range(1,i+1):
#             s+=str(i)+" "
#         print(s)
#     else:
#         s=str(i)+" "
#         for k in range(1,i-1):
#             s+="0 "
#         s+=str(i)
#         print(s)
#