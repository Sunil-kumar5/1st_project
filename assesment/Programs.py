## 1) Positive or Negative number:
# l = [-1,-8,4,5,-6,5,4,0]
# pos = []
# neg = []
# for i in l:
#     if i < 0:
#         neg.append(i)
#     else:
#         pos.append(i)
# print([pos,neg])
# # print(neg)
######################

# 2) Even or Odd number
# l = [1,2,3,4,5,6,43,33,6,55]
# even = []
# odd = []
# for i in l:
#     if isinstance(i,int):
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
# print(even,odd)
#####################

# 3) Sum of First N Natural numbers:
# n = 5
# sum = 0
# for i in range(1,n):
#     sum += i
# print(sum)
###################

# 4) program  to check armstrong number
# num = 153
# sum = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** 3
#     temp //= 10
# if num == sum:
#     print(num, "is an Armstrong number")
# else:
#     print(num, "is not an Armstrong number")
#################

# 5) Prime number within a given range:
# for num in range(0,10):
#     if num >1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)
################

# 6) Sum of digits of a number:
# num = 123
# a = str(num)
# sum = 0
# for i in a:
#     sum += int(i)
# print(sum)
###############

# 7) Reverse of a number :
# num = 56
# a = str(num)
# for i in a[::-1]:
#     print(i,end="")
##############

# 8) Palindrome number:
# str_ = "dad"
# res = ""
# for i in str_[::-1]:
#     res += i
# if res == str_:
#     print("palindrome")
# else:
#     print("not a palindrome")
###############

# Armstrong number in a given range :
# for num in range(1,50000+1):
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** 6
#         temp //= 10
#         if num == sum:
#             print(num)

####### OR #######
# a = 153
# b = str(a)
# c = 0
# for i in b:
#     c += int(i)**len(b)
# if a==c:
#     print(f"amstrong is {c}")
# else:
#     print("not")


# Fibonacci Series upto nth term :

# Factorial of a number :
# Power of a number :
# Factor of a number :

# row = 4
# for i in range(row, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     print("\r")

###########
## out_put = [1,2,3,4,5,6,7,8,9]
# l = [1,3,5,7,9]
# res = []
# for i in l:
#     res += [i, i+1]
# print(res[:(len(res)-1)])

########

# reverse a string
# s = "sunil"
# res = ""
# for i in s[::-1]:
#     res += i
# print(res)
#### OR ####
# s = "SUNIL"
# res = ""
# for i in s:
#     res = i + res
# print(res)

############

## count upper and lower

# s = "SUNIl kumar"
# upp = 0
# low = 0
# for i in s:
#     if 'a' <= i <= 'z':
#         low += 1
#     elif 'A' <= i <= 'Z':
#         upp += 1
#     else:
#         pass
# print(f'lower= {low} and upper= {upp}')




