import csv
with open('input.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
                print (row)
                                                                     