# 1. program to find out maximum of two numbers
a=34
b=56
if a>b:
    print(a)
else:
    print(b)
# 2. Write a program to find the maximum of three numbers stored in variables.
a=2
b=3
c=4
big=a
if b>=big:
    big=b
if c>=big:
    big=c
print(big)

# 3. Write a program to check whether a number is negative, positive or zero. Print out “negative”, “positive”, or “zero”.
a= 34
if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")

# 4. Write a program that prints “YES” if a number is divisible by both 5 and 11, and prints “NO” otherwise.
a=55
if ((a%5==0) and (a%11==0)):
    print("YES")
else:
    print("NO")

# 5.Write a program to check whether a year is leap year or not.
a=2100
if a%100==0:
    if a%400==0:
        print("Leap year")
    else:
        print("Not a leap year")
else:
    if(a%4==0):
        print("Leap year")
    else:
        print("Not a leap year")

# 6.Write a program to check whether a character is uppercase or lowercase alphabet. Print “U” for uppercase and “L” for lowercase.
a = 'z'
print(ord(a))
if ord(a)>=65 and ord(a)<=90:
    print("U")
if ord(a)>=97 and ord(a)<=122:
    print("L")

# 7.  Write a program which takes month number and print number of days in that month. For example:
# For month=1 print “31 days”
# For month=2 print “28 days”

month=8
if month<=7:
    if month==2:
        print("28 days")
    elif month%2==0:
        print("30 days")
    else:
        print("31 days")
else:
    if month%2==0:
        print("31 days")
    else:
        print("30 days")
# 8.  Write a program to print the minimum number of Rupee notes needed to match a given amount. Available denominations of notes are 2000, 500, 100, 50.
# For example, if the amount is 28,550, then you need 14 notes of 2000, 1 note of 500, and 1 note of 50. So total number of notes is 14+1+1 = 16.
a=2350
count2000=a//2000
remaining=a%2000
count500=remaining//500
remaining=remaining%500
count100=remaining//100
remaining=remaining%100
count50=remaining//50
print(count2000,count500,count100,count50)
# 9. Write a program to print the profit or loss, given cost price and selling price.
costprice=2000
sellingprice=2500
if costprice>sellingprice:
    print("Loss")
elif sellingprice>costprice:
    print ("profit")
else:
    print("No profit or loss")

# 10. Write a program to check if a triangle can be formed using the given lengths of 3 sides
side1=3
side2=4
side3=6
if (side1+side2)>side3 and (side2+side3)>side1 and (side1+side3)>side2:
    print("valid triangle")
else:
    print("Not a a valid triangle")
#11. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle. (Equilateral triangle has all 3 sides equal. Isosceles triangle has 2 sides equal. Scalene triangle has no side equal).
side1=3
side2=4
side3=6
if (side1==side2) and (side2==side3):
    print("Equilateral triangle")
elif (side1==side2) or (side2==side3) or (side3==side1):
    print("Isoceles triangle")
else:
    print("scalene triangle")
