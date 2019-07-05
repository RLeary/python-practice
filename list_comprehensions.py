# Suppose we want to separate the letters of the word "Hello" and add the letters as items of a list.
# using a for loop:
#    hello_letters = []
#    for letter in 'hello':
#       hello_letters.append(letter)
#    print(hello_letters)

# This can also be done with list comprehensions
# eg:
hello_letters = [ letter for letter in 'hello' ]
print(hello_letters)

# Syntax - [ expression for item in list ]
# list comprehensions can recieve a string or tuple and treat it as a list, as seen above

# Lambda funtions can work the same way, but are less readable
world_letters = list(map(lambda x: x, 'world'))
print(world_letters)

# Conditionsals can be used in list comprehensions
even_list = [ x for x in range(20) if x % 2 == 0 ]
print(even_list)

# Nested IF statements
div_by_4_and_6_list = [ x for x in range(100) if x % 4 == 0 if x %6 == 0]
print(div_by_4_and_6_list)

# Transpose matrix using nested loops
transposed_matrix = []
matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed_matrix.append(transposed_row)

print(transposed_matrix)

# Transpose matrix using list comprehension
# not nested loops in comprehensions dont work the same as normal nested loops, 
# in the below code, for i in range(2) is executed before row[i] for row in matrix
# so a value is assigned to i, then item directed by row[i] is appended to the transposed lsit
matrix = [[1, 5], [2, 6], [3, 7], [4, 8]]
transposed_matrix_comprehension = [[row[i] for row in matrix] for i in range(2)]
print(transposed_matrix_comprehension)

# List comprehensions;
# define and create lists using exisiting lists
# generally more compact and faster than noormal functions and loops
# long comprehensions can be hard to read
# every list comprehension can be written as a for loop, but not vice versa


# From python tutorials:
# List comprehensions provide a concise way to create lists. Common 
# applications are to make new lists where each element is the result
#  of some operations applied to each member of another sequence or iterable, 
# or to create a subsequence of those elements that satisfy a certain condition.

# more examples:
# print squares:
# squares = []
# for x in range(10):
#   sqaures.append(x**2)
# print(squares)

# squares = list(map(lambda x: x**2, range(20)))
# print(squares)

squares = [x**2 for x in range(10)]
print(squares)

# combine elements of 2 lists that are not equal

# not_equal_combination = []
# for x in [1,2,3]:
#   for y in [3,1,4]:
#       if x != y:
#           not_equal_combination.append((x, y))
not_equal_list = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(not_equal_list)