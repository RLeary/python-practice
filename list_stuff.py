colours = ['red', 'blue', 'yellow', 'grey', 'orange', 'blue']

# list.count(x), count how many times x is in list
print(colours.count('blue'))

#list.index(x), return index of 1st item equal to x
print(colours.index('yellow'))

#find next 'blue' starting from position 3
print(colours.index('blue',3))

# list.reverse(), reverse elements in list --returning none
print(colours.reverse())

#list.append(x), append x to end of list
colours.append('purple')
print(colours)

#list.sort(), sort list
colours.sort()
print(colours)

#list.pop([i]), remove item and givien position and return it
print(colours.pop(4))
print(colours)