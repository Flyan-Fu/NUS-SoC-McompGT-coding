A = 0
H = 0
a = 0
h = 0
Round = int(input())
Game = input()
for i in range(len(Game)):
    if Game[i] == "A":
        a += 1
        if a == 3 :
            A += 1
            a = 0
            h = 0
            if A == Round:
                print("Hannes")
    else:
        h += 1
        if h == 3 :
            H += 1
            a = 0
            h = 0
            if H == Round:
                print("Arnar")
