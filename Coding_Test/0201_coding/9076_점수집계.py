# t = int(input())
# for i in range(t):
#     numbers = list(map(int,input().split()))
#     numbers = sorted(numbers)
    
#     if numbers[3] - numbers[1] >= 4:
#         print('KIN')
#     else:
#         sum = numbers[1]+numbers[2]+numbers[3]
#         print(sum)

n = int(input())
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)