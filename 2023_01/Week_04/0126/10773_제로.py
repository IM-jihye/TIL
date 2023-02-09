# 제로
T = int(input())
stack = []
for i in range(T):
    N = int(input())
    if N != 0:
        stack.append(N)
    elif N == 0:
        stack.pop()
print(sum(stack))