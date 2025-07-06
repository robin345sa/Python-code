import random
char = "1234567890qqwertyuiopasdfghjkl;;'zxcvbnm,./"
length = int(input("Enter the length of charater :"))
passwd ='This is your password:'
for i in range(length):
    passwd+=random.choice(char)
print(passwd)