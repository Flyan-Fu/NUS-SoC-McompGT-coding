ll = int(input())
l = input().split()
tmax = int(l[0])
tmin = int(l[0])
for i in range(ll):
    if int(l[i]) > tmax:
        tmax = int(l[i])
    if int(l[i]) < tmin:
        tmin = int(l[i])
print(f"{tmax} {tmin}")
