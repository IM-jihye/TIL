t = int(input())
num = []
for i in range(t):
    num.append(int(input()))   
cnt = 0
max = 0
for j in reversed(num):
	if max < j:
		max = j
		cnt += 1
print(cnt)

      
