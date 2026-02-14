'''
【经典贪心问题】函数只能增不能减
求最长锻炼时间
【核心思路】倒序遍历列表
'''
days = int(input())
input_stay = input().split()
stay = [int(i) for i in input_stay]
work = 10**5
time = 0
for i in range(days-1,-1,-1):
    work = min(work,stay[i])
    time += work
print(time)

    
            
        
            
            
