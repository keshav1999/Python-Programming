# spiral printing
# mat= [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [10,11,12]
# ]
#
# def spiralprint(mat):
#     numrows=len(mat)
#     numcols=len(mat[0])
#     top=0
#     bottom=numrows-1
#     left=0
#     right=numcols-1
#     while left<=right and top<=bottom:
#         for r in range(top,bottom+1):
#             print(mat[r][left])
#         left+=1
#         if not(left<=right and top<=right):
#             break
#
#         for c in range(left,right+1):
#             print(mat[bottom][c])
#         bottom-=1
#         if not (left <= right and top <= right):
#             break
#
#         for r in range(bottom,top-1,-1):
#             print(mat[r][right])
#         right-=1
#         if not (left <= right and top <= right):
#             break
#
#         for c in range(right,left-1,-1):
#             print(mat[top][c])
#         top+=1
#
# spiralprint(mat)

## recursion

# def factorial(num):
#     if num==1:
#         return 1
#     return num*factorial(num-1)
# print(factorial(5))


# def fabonacci(num):
#     if num==1 or num==0:
#         return num
#     return fabonacci(num-1)+fabonacci(num-2)
# print(fabonacci(7))

# def pow(a,b):
#     if b==0:
#         return 1
#     return a*pow(a,b-1)
# print(pow(2,3))




# def reverseprint(num):
#     if num==0:
#         return
#     print(num)
#     reverseprint(num-1)
# reverseprint(6)



# def straightprint(num):
#     if num==0:
#         return
#     straightprint(num-1)
#     print(num)
# straightprint(6)



# memory=[-1]*1000
# def fib(i):
#     if memory[i]!=-1:
#         return memory[i]
#     if i==0 or i==1:
#         return i
#     result=fib(i-1)+fib(i-2)
#     memory[i]=result
#     return result
# print(fib(990))

# def powerpositive(a,b):
#     if b==0:
#         return 1
#     p=b if b>=0 else -b
#     partial=pow(a,b//2)
#     result=partial*partial
#     if p%2!=0:
#         result*=a
#     return result if b>0 else 1/result
#
# print(power(-2,-3))



# def pow(a,b):
#     if b<0:
#         return 1/powerpositive(a,-b)
#     else:
#         return powerpositive(a,b)


# def hcf(a,b):
#     if a==0 or b==0:
#         return max(a,b)
#     if a>b:
#         return hcf(a%b,b)
#     else:
#         return hcf(a,b%a)
# print(hcf(12,60))





