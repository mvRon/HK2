from Pheptinh import *
def tinh(a,b):
    Sum = tong(a,b)
    Mul = nhan(a,b)
    print(f"Tong la: {Sum}")
    print(f"Tich la: {Mul}")

if __name__ == "__main__":
    a = float(input("Nhap so A:"))
    b = float(input("Nhap so B:"))
    tinh(a,b)

