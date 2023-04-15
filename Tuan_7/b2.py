import shutil
import os

file_1 = input("Nhap ten file muon sao chep:")
file_2 = input("Nhap ten file can sao chep:")
if os.path.exists(file_1):
    shutil.copy(file_1, file_2)
    print("Copied completed!")
else:
    print(f"{file_1} is not exists!")
    
