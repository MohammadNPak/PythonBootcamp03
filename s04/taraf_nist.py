# a1 = int(input())
# a2 = input()
# b1 = int(input())
# b2 = input()
# c1 = int(input())
# c2 = input()


# m =     "shanbe 1shanbe 2shanbe 3shanfgfrbe"
# # index  0123456789
# print(len(m))
# print(m[1])
# print(m[2:6]) # slicing
# print(m[2:6:2]) # slicing

"shanbe"
"1shanbe"
"2shanbe"
"3shanfgfrbe"


m = "shanbe seperator 1shanbeseperator 2shanbe,seperator3shanfgfrbe"

def split_str(s,char):
    start,end = 0,0
    while end<len(s):
        if m[end]==char or end==len(s)-1:
            print(s[start:end])
            start=end+1            
        end+=1
        
split_str(m,"seperator")