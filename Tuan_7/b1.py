import os

file_name = input("Nhap ten tap tin:")
if os.path.exists(file_name):
    f = open(file_name, "r")
    print(f.read())
    f.close()
else:
    print(f"{file_name} is not exists!")
