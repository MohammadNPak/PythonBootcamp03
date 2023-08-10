# m = "shanbe seperator 1shanbeseperator 2shanbe,seperator3shanfgfrbe"

# def split_str(s,char):
#     start,end = 0,0
#     while end<len(s):
#         if s[end]==char or end==len(s)-1:
#             print(s[start:end])
#             start=end+1            
#         end+=1
        
# split_str(m,"seperator")

# s = "salam sep bye sep goodnight"
# a = s.split("sep")
# print(a)


m = "seperatorshanbe seperator 1shanbeseperator 2shanbe seperator3shanfgfrbe"

# def split_arian(s, char):
#     start = 0
#     end = 0
#     while end < len(s):
#         if s[end:end+len(char)] == char or end == len(s)-1:
#             print(s[start:end])
#             start = end + len(char)
#         end += 1

# split_str(m, "seperator")


name = "mohmmad"
a = name[1:4]

# names = ["mohmmad","reza","arian",1,3.14,True,]
# # index    0          1       2   3 4    5
# print(len(names))
# print(names[5])
# names[5] = 10
# print(names)
# names.append("lksdjhfkl")
# print(names)
# names.pop(2)
# print(names)
# names.remove("reza")
# print(names)


names = ["mohmmad","reza","arian",1,3.14,True]

i = 0
while i<len(names):
    print(names[i])
    i+=1
    
for i in range(len(names)):
    print(names[i])
    
for x in names:
    print(x)