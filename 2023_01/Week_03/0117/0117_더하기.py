# 10보다 작거나 같은 자연수 N개를 주면 합을 구하는 프로그램을 작성하시오.
# 각 테스트 케이스에 대해서 주어진 자연수의 합을 한 줄에 하나씩 출력한다.

t = int(input()) # 테스트케이스 개수

for i in range(t):
    nums = [] # 한 줄에 있는 자연수를 담을 리스트
    n = int(input()) # 한 줄에 있는 자연수의 개수
    nums = sum(list(map(int, input().split()))) # 한 줄에 있는 자연수를 리스트에 넣고 sum 함수로 합을 구한다.
    print(nums)

