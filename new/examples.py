# s = "python is a programming language"
# words = s.split()
# shortest, *rest, longest = sorted(words,key=len)
# print(shortest,longest)


# s = "python is a programming language"
# words = s.split()
# shortest, *rest, longest = sorted(words,key=len)
# print((shortest,len(shortest)),(longest,len(longest)))

# s = "python is a programming language"
#
# words = s.split()
# print(sorted(words,key=lambda))


# d = {"z": 2,"walmart": 3,"apple": 1}
# print(sorted(d.items(),key=lambda item: item[0][-1]))


# d = {"z": 2,"walmart": 3,"apple": 1}
# print(dict(sorted(d.items(),key=lambda item: item[-1])))


""" to get most repeated word"""
# sentence = "hi how are you how is your health"
# list_= sentence.split()
# d = {word:list_.count(word) for word in list_}
# res = sorted(d.items(),key=lambda item:item[-1])
# print(res[-1])


# list_ = sentence.split()
# d = {item:len(item) for item in list_}
# res = sorted(d.items(),key=lambda item: item[-1])
# print(res[-1])


# l = [{"name":"ram","class":6,"age":12},{"name":"shyam","class":12,"age":18},{"name":"john","class":8,"age":13}]
# #sort on names
# print(sorted(l,key=lambda item: item["name"]))
# print(sorted(l,key=lambda item: item["class"]))
# print(sorted(l,key=lambda item: item["age"]))
#
# s = ["python","c","java","pjj","pffff","ahjbhh","ekjk"]
# dict_ = {item:len(item) for item in s if item[0] in "Pp"}
# # print(dict_)
# res = sorted(dict_.items(),key = lambda item: item[-1])
# print(res)

# s ={"pjj","pffff","ahjbhh","ekjk",4,58,5,85,585,5855,5}
# dict_ = {item: index for index,item in enumerate(s) if isinstance(item,int)}
# print(dict_)
# res = sorted(dict_.items(),key = lambda item: item[-1])
# print(res)

""" to print even len key and (len,index)"""
# s = ["python","c","java","pjj","pffff","ahjbhh","ekjk"]
# dict_ = {item:(len(item),index)  for index,item in enumerate(s) if len(item) % 2 ==0}
# # print(dict_)
# res = sorted(dict_.items(),key = lambda item: item[-1],reverse=True)
# print(res)

