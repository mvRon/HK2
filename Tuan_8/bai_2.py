class Personality:
    def __init__(self, name, age, address) -> None:
        self.name = name
        self.age = age
        self.address = address
    
    def show(self):
        print("Full name:",self.name)
        print("Age:",self.age)
        print("Address:",self.address)
        

if __name__ == "__main__":
    print("=====INPUT=====")
    name = input("Your name:")
    age = int(input("Your age:"))
    address = input("Your address:")
    print("=====OUTPUT=====")
    call = Personality(name, age, address)
    call.show()
    
    
    
    
    