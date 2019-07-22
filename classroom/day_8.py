# l1=[1,0,0]
# l2=[9,9,9,9]
# x=len(l1)
# y=len(l2)
# n=max(x,y)+1
# result=[]
# carry=0
# for i in range(1,n+1):
#     a=l1[x-i]  if x-i>=0 else 0
#     b= l2[i]   if y-i>=0 else 0
#     c=a+b+carry
#     carry=c//10
#     result.insert(0,c%10)
# print(result)

# Tuples
tup3=(1,2,3)
# print(tup3)
# print(tup3[0])
# tup3[0]=11
# tup0=()
tup5=(1,2,3,4,5)
# print(tup5[1:4])
# tup6=tup3+tup5
# print(tup6)
# a=3,4,5,6,7
# print(a)


# def foo():
#     return 1,2
# print(foo())
# x,y=foo()
# print(x)
# tup1=(55)
# print(tup1)

# tup1=tuple([55])
# print(tup1)
#
# arr=[1,2,3,4]
# tuple(arr)
#
# print(tuple(arr))
#
# for v in tup5:
#     print(v)
# print(3 in tup5)
# print(30 in tup5)
#
# print((1,2,3)*2)






# Dictonary

# person={
#     "name":'john',
#     "age":20,
#     "address":{
#         "city": "Delhi",
#         "zip": 110001
#     }
#     ,"friends": ["Anne","Bill"]
# }
# print(person)
# print(person["name"])
# phonbook={
#     "John":13213123123,
#     "Bill":231213123123,
#     "Anne":23123123123321
# }
# phonbook["Cathy"]=32434324234
# print(phonbook)

# print(person["friends"][0])

# print(phonbook.get("Matt"))
# person={}
# person["name"]=input("Enter ")
# person["age"]=int(input("Enter"))
# person["address"]={}
# person["address"]["city"]=input()
# print(person)

# for i in person:
#     print(i,person[i])

# for k,v in person.items():
#     print(k,v)
# print(person.item())
# print(person())

# SETS

s1=set()
s1.add(1)
s1.add(2)
s1.add(3)
s1.add(3)
s1.add(4)
print(s1)
#
# s2=set([10,20,30])
# print(s2)


# for i in s1:
#     print(i)
# s="The tallest tree is also the oldest"
# words=set(s.split())
# print(words)
# print(words[2])

# a=set([1,2,3])
# b=set([2,3])
# c=set([2,3,4])
# print(b.issubset(a))
# print(c.issubset(a))
# print(a==b)
# print(b.intersection(a))
# print(b.union(a))
# print(b.difference(a))
# print(a.difference(b))
# print(a.symmetric_difference(b))
#
# d={}
# tup=(1,2)
# arr=[1,2]
# d["coordinates"]=tup
# d["coord-arr"]=arr
# d[tup]="hello"
# print(d)
# d[tup]="hello"
# print(d)



