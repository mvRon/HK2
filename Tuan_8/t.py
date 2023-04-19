class QLCD:
    def __init__(self, cd_name, singer_name, amout, cost):
        self.cd_name = cd_name
        self.singer_name = singer_name
        self.amount = amout
        self.cost = cost

    def show(self):
        print(f"{cd_name} | {singer_name} | {amount} | {cost}")
    
    def Total(self):
        self.total += self.cost
        return self.total
    
    
if __name__ == "__main__":
    choice = 1
    CD_List = []
    while choice==1:
        cd_name = input("CD Name:")
        singer_name = input("Singer's Name:")
        amount = input("Amount:")
        cost = input("Cost:")
        print("-----CD List-----")
        CD = QLCD(cd_name,singer_name,amount,cost)
        CD_List.append(CD)
        CD.show()
        choice = int(input("Choices (1:continue/0:stop): "))
        
    print(CD_List[0])



