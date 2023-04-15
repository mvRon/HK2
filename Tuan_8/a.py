class Product:
    def __init__(self, ID, name, cost, date, amount) -> None:
        self.ID = ID
        self.name = name
        self.cost = cost
        self.date = date
        self.amount = amount
        # self.total = total 
        
    def show_info_product(self):
        print(f"ID: {self.ID}")
        print(f"Product's name: {self.name}")
        print(f"Cost's {self.name}: {self.cost}")
        print(f"Date: {self.date}")
        print(f"amount: {self.amount}")
        self.total = self.cost * self.amount
        print(f"Total must pay: ${self.total}")




ID = input("Nhap ID:")
name = input("Product's name:")
cost = float(input(f"Cost's {name}: $"))
date = input("Date:")
amount = int(input("amount:"))
call = Product(ID, name, cost, date, amount)
print("======================")

call.show_info_product()

        
    