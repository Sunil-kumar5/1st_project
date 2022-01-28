# # '''wap to check if the given input is even'''
# # a = int(input("enter the string: "))
# # if a % 2 == 0:
# #     print("number is even")
# # else:
# #     # print("number not even")
#
# # """check for lowercase"""
# # char = input("enter a character")
# # if "a" <= char <= "z":
# #     print(f"{char} is lowercase character")
# char = input("enter a character")
# if char.islower():
#     print(f"{char} is lowercase character")

#check for lowercase if is lowercase print its assci value
# char = "a"
# d = {}
# if char.lower() in "aeiou":
#     d[char] = ord(char)
#     print(d)

# s = "shd@#$%"
# count = 0
# chr = 0
# for i in range(len(s)):
#     if 'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z' or '0' <= s[i] <= '9':
#         continue
#     else:
#         count += 1
# print(count)


# string = "sunil@#$%"
# a = 0
# d = 0
# sp = 0
# for i in range(len(string)):
#     if(string[i].isalpha()):
#         a += 1
#     elif(string[i].isdigit()):
#         d += 1
#     else:
#         sp += 1
# print(sp)

"""wap to count number of capital letter and small letter in a string"""
s1 = "SuniL"
countc = 0
counts = 0
for i in range(len(s1)):
    if 'a' <=s1[i] <= 'z':
        counts += 1
    else:
        countc += 1
print(countc)
print(counts)