'''
Maximally Unfair Fair IKEA Trip
'''
k = int(input())
n = int(input())
index = 0
stuffs = []
sum_weight = 0
part1_weight = 0
part2_weight = 0
carry = []
for _ in range(n):
    stuff = input().split()
    stuff[1] = int(stuff[1])
    stuff.append(index)
    index += 1
    stuffs.append(stuff)
# Sort priority: Weight > Index
stuffs.sort(key=lambda x: (x[1], x[2]))
if n % k:
    for i in range(n//k+1):
        part1_weight +=  stuffs[i][1]
    for j in range(n//k+1,2*(n//k)+1):
        part2_weight +=  stuffs[j][1]
    if part1_weight < part2_weight:
        sum_weight = part1_weight
        print(sum_weight)
        carry = stuffs[0: n//k+1]
        carry.sort(key=lambda x: x[0])
# Print priority: Name
        for i in range(len(carry)):
            print(carry[i][0])
    else:
        sum_weight = part1_weight - stuffs[n//k][1]
        print(sum_weight)
        carry = stuffs[0: n//k]
        carry.sort(key=lambda x: x[0])
        for i in range(len(carry)):
            print(carry[i][0])
else:
    for _ in range(n//k):
        sum_weight +=  stuffs[_][1]  
    print(sum_weight)
    carry = stuffs[0: n//k]
    carry.sort(key=lambda x: x[0])
    for i in range(len(carry)):
        print(carry[i][0])
    