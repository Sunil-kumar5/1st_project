# """wap to traversing through list"""
# l = ["python", 10,3.2, "java"]
# for item in l:
#     print(item, end=" ")
# print()
#
# for i in range(len(l)):
#     print(l[i],end=" ")
#
# """wap index and its corresponding item in the list"""
#l = ["python", 10,3.2, "java"]
# for i in range(len(l)):
#     print("index is:",i)
#     print("element is:",l[i])
#
# for index, item in enumerate(l):
#     print(index, item)

#"""wap to print elements in the list in reverse order"""
#l1 = [2,4,5,"python"]
# for item in l1:
#     print(l1[::-1])
#
# print()

# for i in range(-1,-len(l1)-1,-1):
#     print(l1[i],end="|")

# for i in reversed(l1):
#     print(i, end=" ")

""""wap to print alternative element in a list"""
#l = [2,3,4,5,6,7,7,8,6,9]
# for item in l[::2]:
#    print(item,end=",")

# for i in range(0,len(l),2):
#     print(l[i],end=" ")
""""even index element"""
# for i in range(len(l)):
#     if i % 2 == 0:
#         print(l[i])

# for i in range(len(l)):
#     if i % 2 != 0:
#         print(l[i])
"""wap integer in a list"""
#l = [2,3.4,5,3.,0,11,"sunil",2j,True,False]
# for item in l:
#     if isinstance(item,int):
#         print(item)
#

# for item in l:
#     if isinstance(item,(int,float,complex)):
#         print(item,end=",")

"""wap to print length of each string in the list"""
# l = ["name", "place","bike","age"]
# for i in l:
#     print((i,len(i)))

# l = ["name", "place","bike","age"]
# for i in l:
#     if len(i) % 2 == 0:
#         print(i,len(i))
"""wap to print even lenght of element in a string and store it a list"""
# l = ["name", "place","bike","age"]
# res =[ ]
# for i in l:
#     if len(i) % 2 == 0:
#         res += [i]
# print(res)
"""wap to prinnt the element in a list if the element even lenegth print as it is, if length is odd print it reverse"""
# l = ["name", "place","bike","age"]
# res = []
# for i in l:
#     if len(i) % 2 == 0:
#         res.append(i)
#     else:
#         res.append(i[::-1])
# print(res)

"""wap to reverse the element in the list if the element is of type string or else keep it as it is"""
# l = ['sunil', 'java', 10, True, 19.3, "howsff"]
# res =[]
# for i in l:
#     if isinstance(i,str):
#         res.append(i[::-1])
#     else:
#         res.append(i)
# print("reversed the string in a list",res)

"""wap the element which are starting with vowels"""
# file = ["Amazon", "flipkart", "walmat","gmail","yahoo"]
# for i in file:
#     if i[0] in "aeiouAEIOU":
#         print(i)
"""wap all the extension in the following list"""
# file = ["Amazon.txt", "flipkart.pdf", "walmat.eks","gmail.cgc","yahoo.in"]
# for i in file:
#     l = i.split(".")
#     print(l[1])

"""wap to print the file name if the file is of odd lenght"""
# file = ["Amazon.txt", "flipkart.pdf", "walmat.eks","gmail.cgc","yahoo.in"]
# for i in file:
#     a = i.split(".")
#     if len(a[0]) % 2 == 0:
#         pass
#     else:
#         print(a[0])

""""""
# numbers = [45,10,20,39,40,50,10]
# num = 10
# for index,item in enumerate(numbers):
#     if item == num:
#         print(item,index)
#         break
#using index()
#print(numbers.index(num))

"""prime number"""
# n = 5
# for i in range(2, n):
#     if n % i ==0:
#         print("not prime")
#         break
# else:
#     print("prime")
#

""" To print series of prime number"""
# for n in range(50):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 break
#         else:
#             print(n)
#
"""wap to print all the elements other then the given element"""
# numbers = [10,20,30,40,20,50,60]
# n = 20
# for num in numbers:
#     if n == num:
#         continue
#     print(num)
"""wap to prime numbers in a list"""
# l = [1,5,3,8,9,10,89]
# for n in l:
#     if n > 0:
#         for i in range(2,n):
#             if n % i == 0:
#                 break
#         else:
#             print(n)

"""wap to print the palindromes in the given list"""
l = ["python", "dad", " hai", "madam", "mom","malayalam"]
res = []
for ele in l:
    if ele == ele[::-1]:
        print(ele)
