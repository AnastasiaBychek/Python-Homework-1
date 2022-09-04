a = int (input("Input week day number"))
if a < 0 or a > 8:
    print ("Input correct week day number")
elif a == 6 or a ==7:
    print ("It's a weekend")
else:
    print("It's a working day")