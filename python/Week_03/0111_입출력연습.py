# 문제 1
# 공백으로 구분된 정수
# 5 19 2901 2039 41 2 23 40 
numbers = list(map(int,input().split()))
print(numbers)

# 문제 2
# 공백으로 구분된 문자열
# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
string = input().split()
print(string)

# 문제 3
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스 수가 주어집니다.
# 각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.
T = int(input()) # 테스트 케이스 수

for t in range(1, T+1):
    N = int(input()) # 입력 줄 수
    
    for i in range(1,1+N):
        print(i)

# 문제 4
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스 수가 주어집니다.
# 각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.
# T = int(input()) # 테스트 케이스 수

for t in range(1, T+1):
    N = int(input()) # 입력 줄 수
    
    for i in range(1,1+N):
        print(i,i)

# 문제 5
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력
# 첫 줄에 테스트 케이스 수가 주어집니
# 각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.
# 각 문장에 포함된 단어를 공백을 기준으로 출력하세요.
# input.txt 파일을 생성하고,입력을 작성해주세요.
# 코드를 알고리즘 사이트에 제출할 때 아래 두 줄은 주석처리 해주세요.

