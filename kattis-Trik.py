order = input()
pos = ['Ball', None, None]
for letter in order:
    if letter == 'A':
        pos[0], pos[1] = pos[1], pos[0]
    elif letter == 'B':
        pos[1], pos[2] = pos[2], pos[1]
    else:
        pos[0], pos[2] = pos[2], pos[0]

print(pos.index('Ball') + 1)
