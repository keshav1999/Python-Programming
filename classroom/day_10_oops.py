# tup=1,2,3
# print(tup)
# arr=list(tup)
#
#
# elem=tup[0]*2
# tup1=(elem,)
# print(tup1+tup[1:])


# oops
# class Student:
#     counter=1
#     def __init__(self,name):
#         self.name=name
#         self.rollnum=Student.counter
#         Student.counter+=1
#     def __str__(self):
#         return "Roll: {} Name: {}".format(self.rollnum,self.name)
# s1=Student("Deepak")
# print(s1)
#
# s2=Student("Manish")
# print(s2)
# # s1.counter=30
# print(Student.counter)
# print(s1.counter)
# print(s2.counter)


# length=5
# breadth=3
# print("The length of rect id "+str(length)+" and breadth is "+str(breadth))
# print("The length of rect is {0} and breadth is {1}. Length is {0}".format(length,breadth))

# class Account:
#     counter=1
#     def __init__(self,openingbalance=0):
#         self.__bankbalance= openingbalance
#         self.id=Account.counter
#         Account.counter+=1
#         self.trans=0
#         self.maxtrans=3
#     def deposite(self,amount):
#         if self.__bankbalance+amount>=0 and self.trans<self.maxtrans:
#             self.__bankbalance+=amount
#             self.trans+=1
#     def withdraw(self,amount):
#         if amount<=self.__bankbalance and amount>=0 and self.trans<self.maxtrans:
#             self.__bankbalance-=amount
#             self.trans+=1
#     def __str__(self):
#         return "bankbalance is {} and id is {}".format(self.__bankbalance,self.id)
#     def getbalance(self):
#         return self.__bankbalance
# class SavingAccounts(Account):
#     def getinterest(self):
#         return self.getbalance()*0.05
# class CurrenAccount(Account):
#     def __init__(self):
#         super().__init__()
#         self.maxtrans=5
#
#
# sa1=SavingAccounts()
# sa1.deposite(100)
# sa1.withdraw(10)
# sa1.withdraw(10)
# sa1.withdraw(10)
# print(sa1)
#
# ca1=CurrenAccount()
# ca1.deposite(100)
# ca1.withdraw(10)
# ca1.withdraw(10)
# ca1.withdraw(10)
# ca1.withdraw(10)
# ca1.withdraw(10)
# print(ca1)

# a1=Account()
# a1.deposite(1000)
# a1.withdraw(100)
# a1.__bankbalance=9999999
# print(a1)
# a2=Account(100)
# a2.deposite(20)
# a2.withdraw(1)
# print(a2)




























