'''
Maximally Unfair Fair IKEA Trip
'''
k = int(input())
n = int(input())
stuffs = []
for _ in range(n):
    stuffs.append(int,tuple(input().split()))
for _ in range(n-1):
    if int(stuffs[_][1]) >  int(stuffs[_+1][1]):
        stuffs[_][1],stuffs[_+1][1] = stuffs[_+1][1],stuffs[_][1]
        
print(stuffs)

    