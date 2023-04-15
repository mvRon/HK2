import os
import shutil

# shutil.rmtree("RON")
# os.mkdir("RON\\Test")
old = 'abc'
new = 'xyz'

if os.path.exists(old):
    os.rename(old, new)
else:
    print(f"{old} not exists!")
      


