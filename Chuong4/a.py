Ron = open("RoN.txt", "a")
a = input("Nhap chu muon them vao:")
Ron.write(f"Chu vua moi them vao: {a}")
Ron.close()

Ron = open("RoN.txt", "w")
Ron.write("RoN Melvin!! \n")
Ron.close()

Ron = open("RoN.txt", "r")
for line in Ron:
    print(line)