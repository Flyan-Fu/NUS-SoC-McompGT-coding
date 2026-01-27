l = input()
t = 0
h = 0
for i in l :
    if i == "T":
        t += 1
        if t >= 11 and t - h >= 2:
            t = 0
            h = 0
    elif i == "H":
        h += 1
        if h >= 11 and h - t >= 2:
            t = 0
            h = 0
print(f"{t}-{h}")
