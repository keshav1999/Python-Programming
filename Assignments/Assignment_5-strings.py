# 1. Take as input S, a string. Write a function that returns true if the string is palindrome and false otherwise. Print the value returned.
# S= input()
# le=len(S)
# def  palindrome(s,len):
#     if len%2!=0:
#         return s[0:( len//2)]== s[len:len//2:-1]
#     else:
#         return s[0:(len//2)]==s[len:(len//2)-1:-1]
#print(le)
#print(palindrome(S,le))

# 2. Take as input S, a string. Write a function that returns the count of substrings of this string which are palindromes. Print the value returned.

# def  countpalin(s):
#     count = 0
#     leng = len(s)
#     for i in range(1,leng+1):
#         a = ""
#         for j in range(i, leng+1):
#             a =  s[i:j+1]
#             ln = len(a)
#             if palindrome(a, ln):
#                 count = count + 1
#     return count
# print ( countpalin ( S ) -1)

# 3. 3. Take as input S, a string. Write a function that toggles the case of all characters in the string. Print the value returned.
# S=input()
# def strtoggle(s):
#     le=len(s)
#     for i in range(le):
#         if s[i]>='a' and s[i]<='z':
#             print(s[i]+" : "+"l")
#         elif s[i]>='A' and s[i]<='Z':
#             print(s[i]+" : U")
#         else:
#             print(s[i]+" : other character")
# strtoggle(s)

# 4. Take as input S, a string. Write a function that replaces every odd character with the character having just higher ascii code and every even character with the character having just lower ascii code. Print the value returned.
# def oddeven(s):
#     le=len(s)
#     b=""
#     for i in range(le):
#         if i%2==0:
#             b+= chr(ord(s[i]) + 1)
#         else:
#             b+= chr(ord(s[i]) - 1)
#     return b
# a = oddeven(S)
# print(a)

# 5. 5. Take as input S, a string. Write a function that inserts between each pair of characters the difference between their ascii codes. Print the value returned.
s=input()
def diffascii(b):
    l=len(b)

