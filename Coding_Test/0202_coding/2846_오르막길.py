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


# n = int(input())
# li = list(map(int, input().split()))
# a = 0
# re = []

# for i in range(n-1):
#     if li[i] < li[i+1]:
#         a += li[i+1] - li[i]
#     else:
#         re.append(a)
#         a = 0
# re.append(a)
# print(max(re))