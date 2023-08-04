m = "shanbe seperator 1shanbeseperator 2shanbe,seperator3shanfgfrbe"

def split_str(s,char):
    start,end = 0,0
    while end<len(s):
        if m[end]==char or end==len(s)-1:
            print(s[start:end])
            start=end+1            
        end+=1
        
split_str(m,"seperator")