l = input()
s=l[0]
for i in range(1,len(l)):
    if l[i] != l[i-1]:
        s += l[i]
print(s)
