colours = {'blue', 'red', 'orange', 'purple', 'green', 'pink'}
print(colours)
# quick membership testing
if 'blue' in colours:
    print('True')
if 'yellow' in colours:
    print('false')

# set operations

set_a = set('abracadabra')
set_b = set('alacazam')
# unique letters in set_a, call set_a
print(set_a)
# letters in a, not b
print(set_a - set_b)
#letters in a or b
print(set_a | set_b)
# letters in both a and b
print(set_a & set_b)
# letters in a exclusive or b
print(set_a ^ set_b)

# compehensions can also be used for sets
set_c = {x for x in 'abracadabra' if x not in 'abc'}
print(set_c)