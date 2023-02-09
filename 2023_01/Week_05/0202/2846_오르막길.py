n = int(input())
p = list(map(int,input().split()))
up = 0
ans = []

for i in range(n-1):
    if p[i]<p[i+1]:
        up += p[i+1]-p[i]  
    else:       
        ans.append(up)
        up = 0
ans.append(up)
print(max(ans))


