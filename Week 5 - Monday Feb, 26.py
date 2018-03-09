# SEARCHING (Chapter 15 from programming arcade games)

file = open('data/villains.txt', 'r') # open file to read (creates object named file
print(file)

'''
for line in file:
    print(line.strip()) # .strip() method removes spaces and \t \n from beginning and end
'''

for line in file:
    print("Hello", line.strip())


file.close()

# you can also open a file to write (overwrites all previous)
#file = open('data/villains.txt', 'w')
#file.write('Lee the Merciless')
#file.close()

# open a file to append (adds to the bottom of the file)
#file = open('data/villains.txt', 'a')
#file.write("Lee The Merciless\n")
#file.close()

# Read the file into an array (list)
file = open('data/villains.txt', 'r')

villains = [x.strip() for x in file]

'''
villains = []

for line in file:
    villains.append(line.strip())
'''

print(villains)

# Linear search
key = "The Vindictive Fury" # What we are searching for
i = 0 # index for my loop

while i < len(villains) - 1 and key != villains[i]:
    i += 1

if i < len(villains):
    print("Found", key, "at position", i)


# Binary Search

key = "The Barbarous Harlot"
lower_bound = 0
upper_bound = len(villains) - 1
found = False

# loop until we find it
while lower_bound <= upper_bound and not found:
    middle_pos = (upper_bound + lower_bound) // 2
    if villains[middle_pos] < key:
        lower_bound = middle_pos + 1
    elif villains[middle_pos] > key:
        upper_bound = middle_pos - 1
    else:
        found = True


if found:
    print(key, "was found at position", middle_pos)
else:
    print(key, "was not found in the list")


import re

# This function takes in a line of text and returns a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file = open('data/villains.txt', "r")
all_words = []

for line in file:
    words = split_line(line)
    for words in words:
        all_words.append(words)

print(all_words)

