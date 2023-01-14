# 문제1
#정수형 숫자를 입력 받고, 10을 더해서 출력하세요.
num = int(input('정수형 숫자를 입력해주세요 > '))
print(num + 10)

# 문제2
food = input('좋아하는 음식을 입력해주세요 >') 
print('좋아하는 음식 :' + food)

# 문제3
# 이름과 태어난 년도를 입력 받고, 출력하세요.(단, 태어난 년도를 나이로 변환해서 출력하세요.)
name = input('이름을 입력해주세요 >')
year = int(input('태어난 년도를 입력해주세요 >'))
print('저의 이름은 ',name,'이고, 올해 나이는 ',2023- year+1 ,'세 입니다.')

# 문제4
#문장 두 개를 입력 받고, 두 문장을 연결해서 출력하세요.
a = input('첫 번째 문장을 입력해주세요 >')
b = input('두 번째 문장을 입력해주세요 >') 
print( a + b)

# 문제5
#정수형 숫자 한 개를 입력 받고, 정수형 숫자의 부호를 바꿔서 출력하세요.
num = int(input('정수형 숫자를 입력해주세요 >')) 
print(num * -1)

# 문제6
num1 = int(input('첫 번째 정수형 숫자를 입력해주세요 >')) 
num2 = int(input('두 번째 정수형 숫자를 입력해주세요 >')) 
print('더하기 연산 :', num1 + num2)
print('뺴기 연산 :',num1 - num2)
print('곱하기 연산 :', num1 * num2)
print('몫 연산 :', int(num1/num2)) 
print('나머지 연산 :',num1 % num2) 

# 문제7
#정수형 숫자 세 개를 입력 받고, 세 정수형 숫자의 평균을 출력하세요.
num1 = int(input('첫 번째 정수형 숫자를 입력해주세요 > '))
num2 = int(input('두 번째 정수형 숫자를 입력해주세요 > '))
num3 = int(input('세 번째 정수형 숫자를 입력해주세요 > '))

print(int((num1+num2+num3)/3))

# 문제8
#정수형 숫자 다섯 개를 입력 받고, 다섯 개의 정수형 숫자를 리스트 객체에 저장해서 출력하세요.
numbers = list(map(int,input().split()))
print(numbers)

# 문제9
# 문자열 하나와 정수형 숫자 한 개를 입력 받고, 문자열을 정수형 숫자만큼 반복해서 출력하세요.
str = input('문자열을 입력해주세요 >') 
num = int(input('정수형 숫자를 입력해주세요 >'))
print(str * num)

# 문제10
#정수형 숫자 다섯 개를 입력 받고, 입력할 때 마다 입력한 정수형 숫자들의 합을 출력하세요.
num = 0
num1 = int(input('첫 번째 정수형 숫자를 입력해주세요 >'))
print(nume= num1)
num2 = int(input('두 번째 정수형 숫자를 입력해주세요 >'))
print(num=num1+num2)
num3 = int(input('세 번째 정수형 숫자를 입력해주세요 >'))
print(num1+num2+num3)
num4 = int(input('네 번째 정수형 숫자를 입력해주세요 >'))
print(num1+num2+num3+num4)
num5 = int(input('다섯 번째 정수형 숫자를 입력해주세요 >'))
print(num1+num2+num3+num4+num5)



