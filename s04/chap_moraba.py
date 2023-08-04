# n = int(input())
# i=0
# while i<n:
#     # print("*",end="")
#     j=0
#     while j<n:
#         if i==0 or i==n-1:
#             print("*",end="")
#         else:
#             if j==0 or j==n-1:
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#         j+=1
#     print()
#     i+=1
    
    
    
# i = 0
# while i<20:
#     print(i)
#     i+=1

# for i in range(10):  #[0,1,...,5,6,7,8,9]
#     print(i)
    
# for i in range(5,10):  #[5,6,7,8,9]
#     print(i)
    
# for i in range(5,10,2):  #[5,7,9]
#     print(i)
    
    


n = int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1:
            print("*",end="")
        else:
            if j==0 or j==n-1:
                print("*",end="")
            else:
                print(" ",end="")
    print()
