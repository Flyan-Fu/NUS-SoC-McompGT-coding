# participants: N
num = int(input())
go_list = []
for i in range(num):
    go_list.append(int(input()))
go_list.sort()
sum_wait_t = [go_list[0],]

for i in range(1,num):
    sum_wait_t.append(sum_wait_t[i-1] + go_list[i])

min_wait_t = float('inf')

for i in range(num-1):
    part1_t = (i+1) * go_list[i] - sum_wait_t[i]
    part2_t = (num - (i + 1)) * go_list[num-1] - (sum_wait_t[num-1] - sum_wait_t[i])
    total_wait_t = part1_t + part2_t
    if total_wait_t < min_wait_t:
        min_wait_t = total_wait_t

print(min_wait_t)