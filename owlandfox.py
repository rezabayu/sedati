T = int(input())
final = []

def numSum(num):
    n_sum = 0
    for i in str(num):
        n_sum += int(i)
    return n_sum

for i in range(T):
    N = int(input())
    a_sum = numSum(N)
    for j in range(N-1, -1, -1):
        if numSum(j) == a_sum-1:
            break
    final.append(j)
for r in final:
    print(r)
