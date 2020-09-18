R, C, Zr, Zc = input().split(" ")
results = []
for i in range(int(R)):
    line = input()
    new_char = []
    for char in line:
        new_char.append(char*int(Zc))
    new_line = "".join(new_char)
    for j in range(int(Zr)):
        results.append(new_line)

for baris in results:
    print(baris)
