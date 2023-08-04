# m = "shanbe seperator 1shanbeseperator 2shanbe,seperator3shanfgfrbe"

# def split_str(s,char):
#     start,end = 0,0
#     while end<len(s):
#         if s[end]==char or end==len(s)-1:
#             print(s[start:end])
#             start=end+1            
#         end+=1
        
# split_str(m,"seperator")

s = "salam sep bye sep goodnight"
a = s.split("sep")
print(a)


m = "seperatorshanbe seperator 1shanbeseperator 2shanbe seperator3shanfgfrbe"

def split_arian(s, char):
    start = 0
    end = 0
    while end < len(s):
        if s[end:end+len(char)] == char or end == len(s)-1:
            print(s[start:end])
            start = end + len(char)
        end += 1

split_arian(m, "seperator")
