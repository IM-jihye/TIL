
N = int(input())  #입력받은 값을 int로 바꿈
num = N           #변하는 값
count = 0         #몇 번 사이클인지
 
while True:
    a = num//10
    b = num %10
    c = (a+b)%10
    num = (b*10) + c
    count += 1
    if(num == N):
        break
 
print(count)

# 26 2+6=8 6+8=14 8+4=12 4+2=6 2+6=8

N = "26"
# N을 복사한 변수 
given_n = N

cnt = 0
while True:
    # 먼저 주어진 수가 10보다 작으면 앞에 0을 붙여 두 자리 수로 만든다.
    if int(given_n) < 10:
        N = "0" + given_n # 옆에 0붙여서 두 자리수로 만들다
# 각 자리의 숫자를 더한다.   
    first = given_n[-1] # 1의 자리수
    second = given_n[0] # 10의 자리수
    sum_number = int(first) + int(second)

# 주어진 수가 가장 오른쪽 자리 수와
# 옆에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수가 만들 수 있다.
    new_number = given_n[-1] + str(sum_number)[-1]
    # print(new_number)
# 연산 횟수 증가
    cnt += 1

    if int(new_number) == int(N):
        break
# new_number를 다시 N 에 넣어줘요
# N의 값을 새로운 수를 저장하면?
    given_n = new_number
print(cnt)