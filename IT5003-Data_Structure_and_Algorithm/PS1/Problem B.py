n =int(input())
l = input()
g, a, gm, am = 0, 0, 0, 0

for i in range(n-1,-1,-1):
    if l[i] == "A":
        a += 1
    elif l[i] == "G":
        g += 1
    else:
        continue
    if gm + am == 0:
        gm = g
        am = a
    if gm*(a+g) < g*(am+gm):
        gm = g
        am = a
print(f"{gm}-{am}")
