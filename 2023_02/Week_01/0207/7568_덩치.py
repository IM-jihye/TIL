
# n = int(input())
# li = []

# for i in range(n):
#     x,y = map(int, input().split())
#     li.append([x,y])

# for i in range(n):
#     rank = 1
#     for j in range(n):
#         if (li[i][0] < li[j][0] and li[i][1]< li[j][1]):
#             rank += 1

#     print(rank,end= ' ')

a,b = list(map(int,input().split()))
for i in range(2):

    print(a[::-1])