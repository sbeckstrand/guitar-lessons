import random

notes = 'abcdefg'
sharps = 'acdfg'
key = ['minor', 'major']

# Key orders based on pentatonic scales
order = {
    "major": [0, 2, 4, 7, 9, 12],
    "minor": [0, 3, 5, 7, 10, 12]
}

# Where a note is on each string. Does not acount for onctaves (fret + 12). 
# Octaves are checked for in validity loop
roots = {
    "a": [5, 10, 2, 7, 0, 5],
    "b": [7, 0, 4, 9, 2, 7],
    "c": [8, 1, 5, 10, 3, 8],
    "d": [10, 3, 7, 0, 5, 10],
    "e": [0, 5, 9, 2, 7, 0],
    "f": [1, 6, 10, 3, 8, 1],
    "g": [3, 8, 0, 5, 10, 3]
}



# Pick fret/position
position = random.randint(1, 15)

# Pick key
valid = False
while not valid:

    key_note = random.choice(notes)
    key_type = random.choice(key)
    sharp = random.choice([True, False])

    # Check if valid
    for root in roots[key_note]:
        for difference in order[key_type]:
            if sharp:
                difference -= 1
            if (root + difference or (root - 12) + difference) == (position or position - 12):
                valid = True

# Print key and position
if sharp:
    key_note = key_note + "#"
print("%s %s at position %s" % (key_note.upper(), key_type.capitalize(), position))


