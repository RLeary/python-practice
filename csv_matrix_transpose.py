import csv

INPUT_FILE = 'input.csv'
OUTPUT_FILE = 'output.csv'
OUTPUT_FILE2 = 'output2.csv'

# Using with open, nested opens
"""
with open('INPUT_FILE', 'r') as input_file:
    input_data = csv.reader(input_file)
    with open('output.csv', 'w') as output_file:
        writer = csv.writer(output_file)
        output_data = zip(*input_data)
        writer.writerows(output_data)
"""

# Without using with open

input_file = open(INPUT_FILE, 'r')
output_file = open(OUTPUT_FILE2, 'w')

input_data = csv.reader(input_file)
output_data = zip(*input_data)

output = csv.writer(output_file)
output.writerows(output_data)

input_file.close()
output_file.close()