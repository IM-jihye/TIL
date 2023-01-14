# 문제 1
#정수 한 개를 입력 받고, 해당 숫자가 0보다 큰 숫자라면 True 아니면 False를 출력하세요.
num = int(input('정수를 입력하세요 >'))
if num > 0:
    print(True)
else:
    print(False)

# 문제 2
# 정수 두 개를 입력 받고, 크기가 더 큰 정수를 출력하세요.
# 두 정수가 같으면 False를 출력하세요.

num1 = int(input('첫 번째 정수를 입력하세요 >'))
num2 = int(input('두 번째 정수를 입력하세요 >'))

if num1 > num2 :
    print(num1)
elif num1 < num2 :
    print(num2)
elif num1 == num2 :
    print(False)

# 문제 3
# 정수 한 개를 입력 받고, 해당 정수가 1 보다 크고, 10보다 작다면 True 아니면 False를 출력하세요.
num = int(input('정수를 입력하세요 >'))
if 1 < num < 10 :
    print(True)
else:
    print(False)

# 문제 4
# 정수 한 개를 입력 받고 0 보다 크고, 짝수라면 True 아니면 False를 출력하세요.

num = int(input('정수를 입력하세요 >'))
if num > 0:
    if num % 2 == 0:
        print(True)
    else :
        print(False)
else:
    print(False)

# 문제 5
# 정수 한 개를 입력 받고, 아래 조건에 따라 출력하세요.
# 값이 100 초과 / 0 미만이면 "에러" 출력
# 값이 60 이상이면 "합격" 출력
# 값이 60 미만이면 "불합격" 출력

num = int(input('정수를 입력하세요 >'))

if num > 100 :
    print('에러')
elif num < 0:
    print('에러')
elif num >= 60 :
    print('합격')
else:
    print('불합격')

"""""""""""
# num = int(input('정수를 입력하세요 >'))

# if num > 100 or num < 0:
#     print('에러')
# else:
    if num >= 60 :
#     print('합격')
#   else:
#     print('불합격')

"""""""""""
# # 문제 6
# # 문자열을 입력 받고, 입력 받은 문자열을 반대로 한 글자씩 출력하세요.
# # 힌트 : 문자열 역슬라이싱

# str = input('문자열을 입력하세요 >')
# print(str[::-1])

"""""""""""
string = input("문자열을 입력하세요 > ")

for element in string[::-1]:
    print(element)

"""""""""""
# 문제 7
# 정수 두 개를 입력 받고, 두 수 사이의 정수를 오름차순으로 출력하세요.
# 두 값이 같으면 False를 출력하세요

num1 = int(input('첫 번째 정수를 입력하세요 > '))
num2 = int(input('두 번째 정수를 입력하세요 > '))

if num1 < num2 :
    for i in range(num1+1,num2):
        print(i)

elif num1 > num2 :
    for i in range(num2+1,num1):
        print(i)

else :
    print(False)

# 문제 8
# 정수 두 개를 입력 받고, 두 수 사이의 정수를 내림차순으로 한 줄에 모두 출력하세요.
# 두 값이 같으면 False를 출력하세요

num1 = int(input('첫 번째 정수를 입력하세요 > ')) #5  4 3 2 #1 
num2 = int(input('두 번째 정수를 입력하세요 > ')) #1        #5 4 3 1 

if num1 > num2 :
    for i in range(num1-1,num2,-1):
        print(i)

elif num1 < num2 :
    for i in range(num2-1, num1,-1): 
        print(i)
else :
    print(False)

# 문제 9
# 정수 한 개를 입력 받고, 1 부터 입력 값 사이의 정수 중 홀수만 출력하세요.
# 입력 값이 1보다 작으면 False를 출력하세요.

num = int(input('정수를 입력하세요 >'))

for i in range(1,num):
    if i % 2 ==1 :
        print(i)
    elif num < 1:
         print(False)

"""""""""""
number = int(input("정수를 입력하세요 > "))

if number < 1:
    print(False)
else:
    for element in range(1, number):
        if element % 2 == 1:
            print(element)

"""""""""""

# 문제 10
# 구구단을 출력하세요.

for i in range(2, 10):
    for j in range(2, 10):
        print(i,"*",j, "=",i*j)
"""""""""""
for i in range(2, 10):
    for j in range(2, 10):
        print(f"{i} X {j} = {i*j}")

"""""""""""
