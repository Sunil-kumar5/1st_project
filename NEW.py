# method to print non repeating character in given string
# str_ = 'hello python'
# def non_repeat(str_):
# 	res =''
# 	for i in str_:
# 		if str_.count(i) > 1:
# 			pass
# 		else:
# 			res += i
# 	return res
# print(non_repeat(str_))

######################
## To check anagrome
# s = "sunil"
# u = "unisl"
# if (sorted(s) == sorted(u)):
# 	print("anagrome")
# else:
# 	print("not anagrome")
###### OR ######
# a = 'sunil'
# b = 'ilsun'
# if set(a) == set(b):
#     print('anagram')
# else:
#     print('not anagram')
#############
## To extract mail id

import re
# mail = "sunil uninuo sunilrd56_.@gmail.-.com@-_. gdhfy gjhyu hjgyuyuj"
# reg = r'\b[A-Za-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Z|a-z]{2,}\b'
#
# a = re.findall(reg, mail)
# print(a)
######## OR #######
# reg = r"[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[a-zA-Z0-9@]+[-_]+\."
# a = re.findall(reg, mail)
# print(a)
