from hinhhoc import hinhchunhat,hinhtron,tamgiac

def tinh_toan(a,b,c,r):
    cv_hcn = hinhchunhat.cvHCN(a,b)
    dt_hcn = hinhchunhat.dtHCN(a,b)
    cv_tg = tamgiac.cvTG(a,b,c)
    dt_tg = tamgiac.dtTG(a,b,c)
    cv_ht = hinhtron.cvHT(r)
    dt_ht = hinhtron.dtHT(r)
    print(f"CV hinh chu nhat: {cv_hcn}")
    print(f"DT hinh chu nhat: {dt_hcn}")
    print(f"CV hinh tron: {cv_ht}")
    print(f"DT hinh tron: {dt_ht}")
    if dt_tg:
        print(f"CV hinh tam giac: {cv_tg}")
        print(f"DT hinh tam giac: {dt_tg}")
    else:
        pass


if __name__ == "__main__":
    a = float(input("Nhap so A:"))
    b = float(input("Nhap so B:"))
    c = float(input("Nhap so C:"))
    r = float(input("Nhap ban kinh r cua hinh tron:"))
    tinh_toan(a,b,c,r)







