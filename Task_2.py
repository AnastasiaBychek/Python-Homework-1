for x in range(2):
    for y in range(2):
        for z in range (2):
            if not(x or y or z) == (not(x) and not(y) and not(z)):
                print (f'when x = {x}, y = {y}, z = {z} equation is TRUE ')
            else:
                print (f'when x = {x}, y = {y}, z = {z} equation is FALSE ')
