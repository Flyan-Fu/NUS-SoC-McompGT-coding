l1 = input().split()

n = int(l1[0])
m = int(l1[1])
k = int(l1[2])
l2 = input().split()
s = []
for i in range(n):
    s.append(int(l2[i]))

if m > k:
    print(":(")
else:
    t = k // m
    print((sum(s)+t-1) // t)
