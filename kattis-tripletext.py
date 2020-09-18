s = input()
char = len(s) // 3
coll = []
for a in range(0, len(s)+1, char):
    word = s[a:a+char]
    coll.append(word)
if coll[1] == coll[0] or coll[0] == coll[2]:
    text = coll[0]
elif coll[1] == coll[2]:
    text = coll[1]

print(text)
