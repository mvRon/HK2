from MyPackage import baitap

def tinh_chu_vi(a,b,c):
    hcn = baitap.cvHCN(a,b)
    tg = baitap.cvTG(a,b,c)
    print(f"CV HCN = {hcn}")
    print(f"CV TG = {tg}")

if __name__ == "__main__":
    a = int(input("Nhap so A:"))
    b = int(input("Nhap so B:"))
    c = int(input("Nhap so C:"))
    tinh_chu_vi(a,b,c)