p, q, s = map(int, input().split(" "))
i = 1
r = p * i
while r % q != 0:
    r = p*i
    i += 1
if r <= s:
    print("yes")
else:
    print("no")
