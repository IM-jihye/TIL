# 2029. 몫과 나머지 출력하기
# 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.

T = int(input()) # 테스트 케이스 수

for t in range(1, T+1):
    a,b = list(map(int,input().split()))
    quotiend = a // b
    remainder = a % b
    print(f"#{t} {quotiend} {remainder}")

# 2071. 평균값 구하기
#10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
#(소수점 첫째 자리에서 반올림한 정수를 출력한다.)

T = int(input())
for t in range(1, T+1):
     numbers = list(map(int,input().split()))
     avg = round(sum(numbers)/len(numbers))
     print(f"#{t} {avg}")


# 1938. 아주 간단한 계산기 
# 두 개의 자연수를 입력받아 사칙연산을 수행하는 프로그램을 작성하라.

a,b = list(map(int,input().split()))
print(a + b)
print(a - b)
print(a * b)
print(int(a / b))

# 2046. 스탬프 찍기
# 주어진 숫자만큼 # 을 출력해보세요.
number = int(input())
for i in range (0,number):
    print('#',end="")

# 2068. 최대수 구하기
# 10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.
T = int(input())
for t in range(1, T+1):
     numbers = list(map(int,input().split()))
     numbers = max(numbers)
     print(f"#{t} {numbers}")

