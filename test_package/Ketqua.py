import Pheptinh
def tinh_tong(a,b):
    Sum = Pheptinh.tong(a,b)
    print(f"Tong la:{Sum}")

def tinh_nhan(a,b):
    Mul = Pheptinh.nhan(a,b)
    print(f"Tich la: {Mul}")


if __name__ == "__main__":
    a = float(input("Nhap so A:"))
    b = float(input("Nhap so B:"))
    tinh_tong(a,b)
    tinh_nhan(a,b)

