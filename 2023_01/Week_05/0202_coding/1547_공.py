m = int(input())
cup = [1,2,3]

for i in range(m):
    x,y = map(int,input().split())
    xi = cup.index(x)
    yi = cup.index(y)

    cup[xi] , cup[yi] = cup[yi], cup[xi]

print(cup[0])