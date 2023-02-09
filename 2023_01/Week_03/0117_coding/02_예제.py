# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
# 5
# 20 10 35 30 7

T = int(input())
numbers = list(map(int,input().split()))
print(min(numbers),max(numbers))

# 숫자의 합
# 입력으로 주어진 숫자 N개의 합을 출력한다.

T = int(input())
totla = 0
numbers = list(input())
for i in numbers:
    totla += int(i)
print(totla)

# 수 정렬하기
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 최댓값
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.
num_list = []
for i in range(9):
    num_list.append(int(input()))
    
print(max(num_list))
print(num_list.index(max(num_list))+1)


