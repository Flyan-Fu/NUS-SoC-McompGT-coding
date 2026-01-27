in1= input().split()
row = int(in1[0])
col = int(in1[1])
mines = 0
record = []
for i in range(row):
    line = input()
    for j in range(col):
        if line[j] == "*":
            mines += 1
            record.append(i+1)
            record.append(j+1)
print(mines)
for i in range(0,len(record),2):
    print(f"{record[i]} {record[i+1]}")
        
