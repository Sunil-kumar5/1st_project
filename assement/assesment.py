""" 1) wap to a tuple of character and its ascii value in a string = hello world"""
# string_ = "hello world"
# tuple_ = ()
# for item in string_:
#     tuple_ += ((item,ord(item)))
# print(tuple_)
#
""" 2) wap to check the given number is prime or not"""
# num = 2




""" 3) wap to print the sum of all the digits present in the string"""

# string_ = "whitr56 sperrow98"
# sum = 0
# for item in string_:
#     if item.isdigit():
#         sum += int(item)
# print(f"the sum pf digits in the string is {sum}")


""" 4) wap to print all the consonants present in the sting"""
# string_ = "sum of values present in the string"
# res = ""
# for item in string_:
#     if item not in "aeiou":
#         res += item
# print(res)


""" 3) count the number of digit and alphabets"""

# srt_ = "hai 1234 python23"
# num = 0
# alpha = 0
# for i in srt_:
#     if i.isdigit():
#         num += 1
#     elif i.isalpha():
#         alpha += 1
#     else:
#         pass
# print(f'number of digit{num}')
# print(f'number of alphabets{alpha}')

""" 4) swapping case"""
# str_ = "SuniL 58"
# res = ""
# for i in str_:
#     if "a" <= i <= "z":
#         res += chr(ord(i)-32)
#     elif "A" <= i <= "z":
#         res += chr(ord(i)+32)
#     else :
#         res += i
# print(res)

""" 5) search for character and returns its 1st occurance possion """
# str_ = "gubbi"
# for i in str_:


""" 6) wap character and its ascii value if character is vowel """
# str_ = "sunil kumar"
# for i in str_:
#     if i in "aeiou":
#         print(i,ord(i))

""" 7) wap word and its length"""
# str_ = "wap character and its ascii value if character is vowel"
# a = str_.split()
# for i in a:
#     print(i,len(a),end=" - ")

""" 8) wap print word strting with vowles"""
# str_ = "wap character and its ascii value if character is vowel"
# a = str_.split()
# for i in a:
#     if i[0] in "aeiou":
#         print(i,end="  ")

""" 9) count number of chracter with out inbuilt function"""
# str_ = "hello world"
# count = 0
# for i in str_:
#     if "a" <= i <= "z" or "A" <= i <= "Z":
#         count += 1
#     else:
#         count += 1
# print(count)

""" 10) reverse a string with out using slicing"""
#str_ = "hello world"
# res = ""
# for i in str_:
#     res = i + res
# print(res)

# for item in reversed(str_):
#      print(item,end="")


                           # DAY 2


""" 1) wap to remove all the duplicate element in the list"""
# names = ["apple", "google","apple","yahoo"]
#
# print(list(set(names)))
#
# #
# res = []
# for i in names:
#     if i not in res:
#         res += [i]
# print(res)

""" 2) wap to print all numerical values in a list"""

# items = ["apple",1.2,'google','12.6',26,'100']
# for item in items:
#     if isinstance(item,(int,float,complex)):
#         print(item)
#


""" 3) wap to print thr sum of all even numbers in the given string"""

#sentence = "hello 123 world 567 welcome to 9686 python"
#to print sum of all numbers

# sum = 0
# for i in sentence:
#     if i.isdigit():
#         sum += int(i)
# print(sum)

#  #to sum of even numbers

# evens = 0
# for char in sentence:
#     if "0" <= char <= "9": # and int(char) % 2 ==0
#         if int(char) % 2 == 0:
#             evens += int(char)
# print(evens)

""" 4) wap to create a set with all the languages which starts with 'P'"""
# l = ['Python','Java','Perl','PHP','Python','Js','C++','python','Ruby']
# res = set()
# for i in l:
#     if i[0] in 'P':
#         res.add(i)
# print(res)


""" 5) build a list with only even length string"""
# names = ['apple','google','yahoo','facebook','help','flipkart']
# res = []
# for i in names:
#     if len(i) % 2 == 0:
#         res += [i] # res.append(i)
# print(res)


""" 6) Reverse the item if the item is of odd length string otherwise keep the item as it is"""

# names = ['apple','google','yahoo','facebook','help','flipkart']
# res = []
# for i in names:
#     if len(i) % 2 != 0:
#         res.append(i[::-1])  #res += [i[::-1]]
#     else:
#         res.append(i)  #res += [i]
# print(res)

""" 7) wap to print the sum of entire list and sum of only internal list"""
# l = [[1,2,3],[4,5,6],[7,8,9]]
# entire_sum = 0
#
# for item in l:
#     internal_sum = 0
#     for i in item:
#         internal_sum += i
#         entire_sum += i
#     print(internal_sum)
# print(entire_sum)


# entire_sum = 0
#
# for item in l:      # [1, 2, 3], [4, 5, 6]
#     internal_sum = 0
#     for i in item:          # (1, 2, 3), (4, 5, 6)
#         internal_sum += i
#         entire_sum += i     # 0+1= 1, 1+2= 3, 3+3=6, 6+4=10, 10+5=15, 15+6= 21
#     print(internal_sum)
# print(entire_sum)   # 6

""" 8) wap to print list of prime numbers between 1-100"""
# prime_ = []
# for n in range(100):
#     if n > 1:
#         for i in range(2,n):
#             if n % i == 0:
#                 break
#         else:
#             prime_.append(n)
# print(prime_)

""" 9) wap to reverse the list as below"""
# words = ["hi","hello","python"]
# for i in reversed(words):
#     print(i[::-1],end=" ")
#
# res = []
# for i in words[::-1]:
#     res.append(i[::-1])
# print(res)


""" 10) wap to rotate items of the list"""

# l = ['apple',8,'google','12.6',678,'100']
# k = 2
# for i in range(k):
#     item = l.pop()
#     l.insert(0, item)
# print(l)



""" to print fibonaccs"""
# n = 10
# a = 0
# b = 1
# i = 0
# while i < n:
#     print(a)
#     c = a + b
#     a = b
#     b = c
#     i += 1
#
# print(i)

                                          # Day 3

                                         # Dictionary

""" 1) to get indexes of each item in the below list"""
# names = ["apple","google","apple","yahoo","google","gmail","gmail"]
# d ={}
# for index,item in enumerate(names):
#     if item not in d:
#         d[item] = [index]
#     else:
#         d[item] += [index]
# print(d)

""" 2) reverse the values in the dictionary if the value is of type string"""

# d ={"a":100,"b":"hello","c":"jhgkj"}
# # d1 = {}
# for key,value in d.items():
#     if isinstance(value,str):
#         d[key] =value[::-1]
# print(d)

""" 3) to get all the duplicate items and the number of times the item is repeated in the list"""

# names = ["apple","google","gmail","apple","google"]
# d ={}
# for i in names:
#     count = names.count(i)
#     if count > 1:
#         d[i] = count
# print(d)

""" 4) create dictionary of city and population pair using dict comprehension"""

# cities = ["Tokyo","Delhi"]
# population = ["3569845","54892698"]
#
# res = {a: b for a, b in zip(cities, population)}
# print(res)

""" 5) write a program to flip keys and values"""

# d = {"a":100,"b":"hello","c":"jhgkj"}
# res = {(key, value) for value, key in d.items()}
# print(res)

""" 6) L = [1,2,3,4,5,2,3,4,6,8,8,8,88,99,100
group even and odd index values with comprehension"""

# L = [1, 2, 3, 4, 5, 2, 3, 4, 6, 8, 8, 8, 88, 99, 100]
# res = {even: i if L[i] % 2 == 0 else odd: i for i in L}         #xx
# print(res)

""" 7) Group both the dictionary items in a single dictionary using comprehension"""

# D = {"names":"apple","id":35446}
# d = {"names":"apple","id":32352}
#
# res = {key:value for key,value in D.items() for key,value in d.items()}
# print(res)

""" 8) create a dictionary with the item in tuple as key and its unicode as value using comprehension"""

# T = (9,3,4,123,78,65)
#
# res = {i: chr(i) for i in T}
# print(res)

""" 9) create a dictionary taking keys and values using items in list take key before special character"""

# list_ = ["food@table","lilly@flower"]
# res = {i.split("@")[0]: i.split("@")[1] for i in list_}
# print(res)

""" 10) create dictionary with key as string item and value as integer"""
# s = [(4,56,78),("one","two","three")]
# res = {               #xx
# print(res)


a = filter(lambda x: x**2, [1,2,3,4])
# print(list(a))    #[1,2,3,4]
#
a = map(lambda x: x%2 == 0, a)
# print(a(10))         # a not defined


a = map(lambda x: x**2, [1,2,3,4])
# print(list(a))     #[1, 4, 9, 16]

# a = lambda x, y: x*2, y+3
# print(a(1,2))    # y is not defined


# a = lambda x: x*2
# print(a((1,2)))    #(1, 2, 1, 2)

# a, *z,b = (1,2,3,4)
# print(a,z,b)     #1 [2, 3] 4

"""to check fibo number"""
# def fibo_(num):
#     a = 0
#     b = 1
#     while a <= num:
#         if a == num:
#             return f"{num} is fibo"
#         c = a + b
#         a = b
#         b = c
#     return f"{num} is not fibo"
# print(fibo_(5))



"""to print n fibo numbers"""
# def rec_fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return(rec_fibo(n-1) + rec_fibo(n-2))
#
# print(rec_fibo(3))


#sorting

#
# s = ["asdf","python","hjjgjjhyu","java","c"]
# print(sorted(s,reverse=True))

# d = {"python":1,"java":2,"c":3}
# print(sorted(d))
# print(sorted(d.items()))

# s = ["python","java","c"]
# print(sorted(s,key=len))

# s = "asdf python hjjgjjhyu java c"
# word = s.split()
# short,*rest,long = sorted(word,key=len)
# print((short,len(short)),(long,len(long)))


# def last_(ele):
#     return ele[-1]
# print(sorted(s,key=last_))

# print(sorted(s,key=lambda item:item[-1]))
# print(sorted(s,key=lambda item:item[0]))

# d = {"python":15,"java":2,"c":3}
# print(sorted(d.items(),key=lambda item:item[-1]))

s = "create a dictionary with the item in a tuple as key the and its"
list_ = s.split()
d = {word:list_.count(word) for word in list_}
print(d)
res = sorted(d.items(), key=lambda item:item[-1])
print(res[-1])