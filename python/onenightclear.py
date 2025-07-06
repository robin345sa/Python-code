# # for i in range (1,100):
# #     print(i,"Hello World ")
# #
# # name = input()
# # age =input()
# # print(f"My name is {name} and my age is {age}")
#
# list = [1,11,111,1,1,111,1,1,1,]
# for list in list:
#     print(list)
#
# print(2**4)
# print(2//2)
# print(100%10)

pic =[
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[0,0,1,1,1,0,0],
[0,0,1,1,1,0,0],
[0,0,0,1,0,0,0]
]
for row in pic:
    for pixel in row:
        if(pixel==1):
            print("*",end="")
        else:
            print("",end="")
    print("")