# 카드
# 첫째 줄에 버리는 카드들을 순서대로 출력한다. 제일 마지막에는 남게 되는 카드의 번호를 출력한다.
# 카드
# 첫째 줄에 버리는 카드들을 순서대로 출력한다. 제일 마지막에는 남게 되는 카드의 번호를 출력한다.

n = int(input())
a = [i for i in range(1, n+1)]

while len(a) > 1:
    print(a.pop(0), end=' ')
    k = a.pop(0)
    a.append(k)
print(a[0])