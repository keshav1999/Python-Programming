# 1. Take as input str, a number in form of a string. Write a recursive function to find the sum of digits in the string. Print the value returned.
# S=input()
# l=len(S)
# def sumdigits(s,n,i):
#     if i==n:
#         return 0
#     return int(s[i])+sumdigits(s,n,i+1)
# print(sumdigits(S,l,0))

# 2 Take as input str, a number in form of a string. Write a recursive function to convert the number in string form to number in integer form. E.g. for “1234” return 1234. Print the value returned.

# def strtonum(s,i,num):
#     if i<0:
#         return 0
#     return int(s[i])*num + strtonum(s,i-1,num*10)
# print(strtonum(S,l-1,1))

#3. Take as input str1 and str2, both strings. Write a function which tests if str2 is reverse of str1 or not and returns a Boolean value. Print the value returned.

# str1=input("Enter the string 1")
# str2=input("Enter the string 2")
# l1=len(str1)
# l2=len(str2)
# def isreverse(s1,s2,a,b,i,j):
#     if a!=b:
#         return False
#     if i>a and j<0:
#         return True
#     return s1[i]==s2[j] and isreverse(s1,s2,a,b,i+1,j-1)
# print(isreverse(str1,str2,l1-1,l2-1,0,l2-1))

#4 Take as input str, a string. Write a function which tests if the string is a palindrome or not and returns a Boolean value. Print the value returned.
# S=input()
# m=len(S)//2
# def ispalindrome(s,i,mid):
#     if i==mid:
#         return True
#     return s[i]==s[len(s)-1-i] and ispalindrome(s,i+1,mid)
# print(ispalindrome(S,0,m))

#5. Take as input str, a string. Write a recursive function which returns a new string in which all duplicate consecutive characters are separated by a ‘*’. E.g. for “hello” return “hel*lo”. Print the value returned.
S=input()
le=len(S)
s=""
def duplicate(ss,i,l,ns):
    if i==l:
         ns.append(ss[l])
    if i>l:
        return
    elif ss[i]==ss[i+1]:
       ns.append(ss[i])
       ns.append("*")
    elif ss[i]!=ss[i+1]:
        ns.append(ss[i])
    duplicate(ss,i+1,l,ns)

r=duplicate(S,0,le-1,s)
print(r)



