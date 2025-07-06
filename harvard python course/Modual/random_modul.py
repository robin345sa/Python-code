# import random
# while True:
#     coin = random.choice(["heads:you win","tails:computer win"])
#     print(coin)
# """ randint """
# from python.main import chart

# import random
#
# numbers = random.randint(1,10)
# print(numbers)
# """shuffle"""
# import random

# bikes = ["M15","R15","4v","Royel infenitep"]

# random.shuffle(bikes)

# for bike in bikes:
    # print(bike)

# import random
#
# charter = "!@#@#$%^&*()akljfaionnaopwarfncerwteyruioupi[okbn"
#
# lenth = int(input("Enter your Password lenth"))
#
# password ='This is your password:'
#
# for i in range(lenth):
#    password+=random.choice(charter)
# print(password)
# import random
# choese = ["bike","Home","Money"]
# random.shuffle(choese)

# for choeses in choese:
#     print(f"You choese is {choese}")

import random

while True:
    
    coin =input([random.choices(["heads:you win","tails:computer win"])])
    
    print(coin)