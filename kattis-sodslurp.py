e, f, c = input().split(" ")
e, f, c = int(e), int(f), int(c)
bot = e + f
sod = 0
while bot / c >= 1:
    cot = bot // c
    bot = cot + (bot % c)
    sod += cot
print(int(sod))
