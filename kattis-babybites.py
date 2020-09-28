bites = int(input())
word = input().split(" ")
truth = [x for x in range(1, bites+1)]
for i in range(bites):
    if word[i] != 'mumble' and int(word[i]) != truth[i]:
        status = 0
        break
    else:
        status = 1
if status == 1:
    print("makes sense")
else:
    print("something is fishy")
