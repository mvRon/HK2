from hinh_hoc import *

def tinh_toan(a,b,c,r):
    cvht = cvHT(r)
    dtht = dtHT(r)
    cvhcn = cvHCN(a,b)
    dthcn = dtHCN(a,b)
    cvtg = cvTG(a,b,c)
    dttg = dtTG(a,b,c)
    print(f"CV hinh tron: {cvht}")
    print(f"DT hinh tron: {dtht}")
    print(f"CV hinh chu nhat: {cvhcn}")
    print(f"DT hinh chu nhat: {dthcn}")
    if dttg:
        print(f"CV hinh tam giac: {cvtg}")
        print(f"DT hinh tam giac: {dttg}")
    else:
        pass

if __name__ == "__main__":
    a = int(input("Nhap so A:"))
    b = int(input("Nhap so B:"))
    c = int(input("Nhap so C:"))
    r = float(input("Nhap ban kinh r:"))
    tinh_toan(a,b,c,r)
    
