# 문제1
n = int(input("정수를 입력하세요 >"))
if n > 0 :
    print('True')
else :
    print('False')

# 문제2
#정수 두 개를 입력 받고, 크기가 더 큰 정수를 출력하세요.두 정수가 같으면 False를 출력하세요.

num1 = int(input("첫 번째 정수를 입력하세요 > "))
num2 = int(input("두 번째 정수를 입력하세요 > "))

if num1>num2 :
    print(num1)
elif num2>num1 :
    print(num2)
elif num1 == num2 :
    print(False)

# 문제3
# 정수 한 개를 입력 받고, 해당 정수가 1 보다 크고, 10보다 작다면 True 아니면 False를 출력하세요.
num3 = int(input("정수를 입력하세요 >"))

if 1<num3<10 :
    print(True)
else :
    print(False)

# 문제4
#정수 한 개를 입력 받고 0 보다 크고, 짝수라면 True 아니면 False를 출력하세요.
num4 = int(input("정수를 입력하세요 >"))

if num4 > 0 :
    if num4 % 2 == 0 :
        print(True)
    else :
        print(False)
elif num4 < 0 :
    print(False)

# 문제5
# 정수 한 개를 입력 받고, 아래 조건에 따라 출력하세요.
# 값이 100 초과 / 0 미만이면 "에러" 출력
# 값이 60 이상이면 "합격" 출력
# 값이 60 미만이면 "불합격" 출력

num5 = int(input("정수를 입력하세요 >"))

if num5 > 100 :
    print('에러')
elif num5 <0 :
     print('에러')
elif num5 >= 60 :
    print('합격')
else :
    print('불합격')

# 문제6
#문자열을 입력 받고, 입력 받은 문자열을 반대로 한 글자씩 출력하세요.
#힌트 : 문자열 역슬라이싱

# char = input("문자열을 입력하세요 > ")
# print(char[::-1])

# 문제 7
#정수 두 개를 입력 받고, 두 수 사이의 정수를 오름차순으로 출력하세요.
#두 값이 같으면 False를 출력하세요

# a = int(input("첫 번째 정수를 입력하세요 > "))
# b = int(input("두 번째 정수를 입력하세요 > "))
# if a > b :
#     for i in range(a,b) [::-1]:
#         print(i)
# elif a < b:
#     for i in range(b,a) [::-1]:
#         print(i)

# 문제 8
#정수 두 개를 입력 받고, 두 수 사이의 정수를 내림차순으로 한 줄에 모두 출력하세요.
#두 값이 같으면 False를 출력하세요

# a1 = int(input("첫 번째 정수를 입력하세요 > "))
# a2 = int(input("두 번째 정수를 입력하세요 > "))

#문제 9
#정수 한 개를 입력 받고, 1 부터 입력 값 사이의 정수 중 홀수만 출력하세요.
#입력 값이 1보다 작으면 False를 출력하세요.

# i = int(input("정수를 입력하세요 > "))

# if d > 0 :
#     if d % 2 == 1:
#         continue
#     print(d)
# else:
#     print(False)

# for i in range(i):
#     if i > 1:
#      if i % 2 ==1:
#         continue
#         print(i)
#     else:
#         print(False)

# 문제 10
# 구구단을 출력하세요.
for x in range(2, 10):
    for y in range(1, 10):
        print(x, "X", y, "=", x*y)
