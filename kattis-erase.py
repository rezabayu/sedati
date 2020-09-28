N = int(input())
line_1 = input()
line_2 = input()

def klik(kode, N):
    if N % 2 == 1:
        kode_2 = []
        for a in kode:
            if a == '1':
                kode_2.append('0')
            else:
                kode_2.append('1')
        return "".join(kode_2)
    elif N % 2 == 0:
        kode_2 = kode
        return kode_2

line_true = klik(line_1, N)
if line_true == line_2:
    print("Deletion succeeded")
else:
    print("Deletion failed")
