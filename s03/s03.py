# 123
# 321
# 456789123
# 321987654

# a = 123
# d = a%10
# c = a//10
# c%10


# a = int(input()) # 123
# b=0
# while a!=0:
#     d = a%10
#     a = a//10
#     b = b*10+d

# print(b)




# a = int(input()) # 123
# b=0
# end_with_zero = False
# if a%10==0:
#     end_with_zero=True

# while a!=0:
#     d = a%10
#     a = a//10
#     b = b*10+d
# a = b
# b=0
# while a!=0:
#     d = a%10
#     a = a//10
#     # b = b*10+d
#     print(f"{d}: ",end="")
#     i = 0
#     while i<d:
#         print(d,end="")
#         i+=1 
#     print()

# if end_with_zero:
#     print(f"0: ")

    

n = int(input())
i = 2
p = True
while i<n:
    if n%i==0:
        p=False
    i+=1
print(p)
