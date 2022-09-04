X = int (input("Input X coordinate"))
Y = int (input("Input Y coordinate"))
if X > 0 and Y > 0:
    q = "1st"
elif X >0 and Y < 0:
    q = "2d"
elif X < 0 and Y < 0:
    q = "3d"
else:
    q = "4th"
print(f"It's a {q} quarter" )