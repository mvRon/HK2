Ron = open("RoN_Melvin.txt", "x")
a = input("Input new text:")
Ron.write(f"Test ~~ ABC!!!\n{a}")
Ron.close()
