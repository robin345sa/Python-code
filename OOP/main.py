class student :
    def __init__(self,name,house):
        self.name = name
        self.house = house
def main():
    name = input()
    house =input()
    print(f"{name} form {house}")
main()