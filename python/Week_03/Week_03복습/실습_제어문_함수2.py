# 문제 1
#정수 한 개를 입력 받고, 해당 정수의 절대값을 출력하세요.
#단, abs() 함수는 사용하지 마세요.
num = int(input('정수를 입력하세요 >'))
if num >= 0:
    print(num)
else:
    print(num*-1)

# 문제 2
# 정수만 저장한 리스트가 주어집니다.
# 리스트 요소의 개수를 출력하세요.
# 단, len() 함수는 사용하지 마세요

number_list = [1, 2, 3, 4, 5]
cnt = 0
for i in number_list:
    cnt = cnt +1  
print(cnt)

number_list = []
cnt = 0
for i in number_list:
    cnt = cnt+1
print(cnt)

# 문제 3
# 정수만 저장한 리스트가 주어집니다.
# 리스트에 저장된 정수들의 합을 출력하세요.
# 단, sum() 함수는 사용하지 마세요.
number_list = [1, 2, 3, 4, 5]
totla = 0
for i in number_list:
    totla = totla + i
print(totla)

# 문제 4
# 정수만 저장한 리스트가 주어집니다.
# 리스트에 저장된 정수들의 평균을 출력하세요.
# 단, len() / sum() 함수는 사용하지 마세요.
number_list = [2, 4, 6]
cnt = 0
total = 0
for i in number_list:
    cnt = cnt +1
    total = total + i
print(total/cnt)

# 문제 5
# 정수만 저장한 리스트가 주어집니다.
# 리스트에 저장된 정수들의 곱을 출력하세요.
number_list = [1, 2, 3, 4, 5]
gop = 1
for i in number_list:
    gop = gop * i
print(gop)
number_list = [-1, -2, 3]
gop = 1
for i in number_list:
    gop = gop * i
print(gop)

# 문제 6
# 양의 정수만 저장한 리스트가 주어집니다.
# 리스트에 저장된 정수 중 가장 큰 값을 출력하세요.
# 단, max() 함수는 사용하지 마세요.
number_list = [1, 2, 3, 4, 5]
biggest = 0
for i in number_list:
    biggest > i
    biggest = i
print(biggest)

# 문제 7
# 양의 정수만 저장한 리스트가 주어집니다.
# 리스트에 저장된 정수 중 가장 작은 값을 출력하세요.
# 단, min() 함수는 사용하지 마세요.
number_list = [5, 5, 5, 2]
small = 0
for i in number_list:
    small < i
    small = i
print(small)