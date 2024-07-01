## Libraries ##
import numpy as np
import string
import random
##

#### Challenge 1 - Algorithms ####
##
# Create function to find patterns
def find_pattern(array1,array2,array3):
    size_min = min(len(array1),len(array2),len(array3))
    i = 0
    pattern = []
    while i < size_min:
        j = i
        while (j < size_min)and(array1[j] == array2[j] == array3[j]):
            j += 1
            if j > i:
                pattern.append(array1[i:j])
            i = j+1
    return pattern
# Create arrays
size = random.randint(0,100) # arbitray len of the array

array1 = np.random.choice(list(string.ascii_uppercase), size)
array2 = np.random.choice(list(string.ascii_uppercase), size)
array3 = np.random.choice(list(string.ascii_uppercase), size)
# Print arrays
print(array1)
print('\n')
print(array2)
print('\n')
print(array3)
print('\n')

patterns = find_pattern(array1, array2, array3)
if patterns:
    for x in patterns:
        print('Pattern found: {patterns}')
else:
    print('No patterns found')


#### Challenge 2 - Algorithms ####
##
size_colors = random.randint(0,10) # arbitrary len of the colors array
colors = ['r','g','b'] # list of the characters we need

colors_list = '-'.join(np.random.choice((colors), size_colors))
print(colors_list)

r = 0
g = 0
b = 0

for i in colors_list:
    if i == 'r':
        r += 1
    elif i == 'g':
        g += 1
    elif i == 'b':
        b += 1

print("Total count:\n")
print("Red: "+str(r)+"\n")
print("Green: "+str(g)+"\n")
print("Blue: "+str(b)+"\n")


# Next steps
# Create function to find patterns (similar to first challenge)
## to this function will be necessary to split when character '|' is found
## and be iterating till found a string of a pattern
