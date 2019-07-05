import sys

if len(sys.argv) > 2:
    print("Error: run as: python delete_last_line_in_file.py <filename>")
    exit()
elif len(sys.argv) < 2:
    print("Error: run as: python delete_last_line_in_file.py <filename>")
    exit()

FILE = sys.argv[-1]

try:
    read_file = open(FILE, 'r')
except FileExistsError:
    print("Input does not exist")

lines = read_file.readlines()

read_file.close()

del lines[-3:]

try:
    write_file = open(FILE, 'w')
    try:
        write_file.writelines(lines)
    finally:
        write_file.close()
except IOError:
    print("Error in writing to file")