# try:
#     f = open("Demofile.txt", "x")
#     try:
#         f.write("Lorem Ipsum")
#         print("Completed!")
#     except:
#         print("Something went wrong when writing to the file")
#     finally:
#         f.close()
# except:
#     print("Something went wrong when opening the file")

x = -1
if x<0:
    raise Exception("Something went wrong!")
    

