# def numpaths(rows,cols):
#     return numpathshelper(rows,cols)
# def numpathshelper(r,c):
#     if r==1 and c==1:
#         return 1
#     if r==2 and c==2:
#         return 0
#     if r==2 and c==1:
#         return 0
#     if r==2 and c==3:
#         return 0
#     if r==0 or c==0:
#         return 0
#     pathsfromtop=numpathshelper(r-1,c)
#     pathsfromleft=numpathshelper(r,c-1)
#     return pathsfromtop +pathsfromleft
# print(numpaths(3,3))


# subsets

# def getsubsets(arr):
#     if len(arr)==1:
#         return [[],[arr[0]]]
#     elem=arr[0]
#     ss=getsubsets(arr[1:])
#     result=[]
#     for s in ss:
#         result.append(s)
#         s2=s[:]
#         s2.append(elem)
#         result.append(s2)
#     return result
#
# print(getsubsets([1,2,3]))



# def permute(arr):
#     if len(arr)==1:
#         return [[arr[0]]]
#     result=[]
#     for i in range(len(arr)):
#         elem=arr[i]
#         remain=arr[:i]+arr[i+1:]
#         p=permute(remain)
#         for v in p:
#             v.insert(0,elem)
#             result.append(v)
#     return result
#
# print(permute([1,2,3]))




