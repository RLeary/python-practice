def is_int(val):
    if int(val):
        return True
    else:
        return False

line = input("input an int: ")
if is_int(line):
    print("yes")
else:
    print("no")