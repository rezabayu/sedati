N = int(input())
tb = 0
lr = 0
for i in range(N):
    tblr = input() 
    if tblr[0] == '0':
        tb += 1
    if tblr[1] == '0':
        tb += 1
    if tblr[2] == '0':
        lr += 1
    if tblr[3] == '0':
        lr += 1

tb_pair = tb // 2
lr_pair = lr // 2
if tb_pair <= lr_pair:
    swords = tb_pair
elif tb_pair > lr_pair:
    swords = lr_pair

tb_remain = tb - (swords * 2)
lr_remain = lr - (swords * 2)

print(swords, tb_remain, lr_remain, sep=" ")
