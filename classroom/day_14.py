
# import re
# pattern = re.compile(r"[a-zA-Z0-9]+@gmail.com")
# result= re.search(pattern,"My email is coding@gmail.com")
# print(result)
# print(result.start())
# print(result.end())
# print(result.group(0))
# web ="(http[s]?:\/\/)?www.[a-zA-Z0-9]+.com" # can be checked in pattern


# import random
# random.seed()
# print(5 + random.random()*5)

# import time
# ticks= time.time()
# print(ticks)
#
#
# localtime= time.localtime(ticks)
# print(localtime)
# print(time.asctime(localtime))
#
# import calendar
# cal= calendar.month(2018,7)
# print(cal)
# name='John'
# s="""
# asdasda
#   asdasdasd
#   asdasd
#   {}
#   asdsdasdasdas
#   dasdasdasd
#   """.format(name)
# print(s)
#

'''

this is comment
'''

#  exception handling

# try:
#     a=float(input())
#     b=float(input())
#     print(a/b)
# except (ZeroDivisionError,ValueError) as e:
#     print("invalid input",e)
# except :
#     print("something is wrong")
# finally:
#     print("devision completed successfully")
#
# print("do this")



# expected = 6
# actual=6
# if expected!=actual:
#     raise ValueError("Actual was diff from expected")

# ()


# a=6
# def foo():
#     global a
#     a=5
#     print(a)
# foo()
# print(a)


# def outer(data):
#     def inner():
#         print(data)
#     inner()
# outer("Hello")
# outer(5)



def contain(data):
    def nested():
        print(data)
    return nested
inner= contain("Hello")
inner1=contain("World")
inner()
inner1()