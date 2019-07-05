input_string = input("Enter an integer: ")

try:
    val = int(input_string)
    print("Input string is an integer\n",
            "Input number is: ", val)
except ValueError:
    print("Input string is not an int")

# Using isdigit() - only works for positive

input_string2 = input("Enter another string: ")
if(input_string2.isdigit()):
    print("inpput string is an int")
else:
    print("input is a string")

#float input
input_string3 = input("yet another input string(float this time): ")

try:
    if "." in input_string3:
        float_val = float(input_string3)
        print(float_val, "this is a float")
    else:
        int_val = int(input_string3)
        print(int_val, "this in an int")
except ValueError:
    print("NAN")

#isinstance()
input_string4 = isinstance(int(input("Enter another int:")), int)
if input_string4:
    print("this is another int: ", val)
else:
    print("not an int")