# # 문제1
number = int(input("숫자를 입력해주세요 >"))
print(number + 10)

# 문제2
food = input("좋아하는 음식을 입력해주세요 > ")
print("좋아하는 음식 : ", food)

# 문제3
name = input("이름을 입력해주세요 >")
year = int(input("태어난 년도를 입력해주세요 >"))
print("저의 이름은",name,"이고, 올해 나이는",2023 - year + 1,"세 입니다.")

# 문제4
input1 = input("첫 번째 문장을 입력해주세요 >")
input2 = input("두 번째 문장을 입력해주세요 >")
print(input1 + input2)

# 문제5
num = int(input("숫자를 입력해주세요 >"))
print(-num)

# 문제6
number1 = int(input("첫 번째 숫자를 입력해주세요 > ") )
number2 = int(input("두 번째 숫자를 입력해주세요 >"))
print("더하기 연산 :", number1 + number2)
print("뺴기 연산 :", number1 - number2)
print("곱하기 연산 :", number1 * number2)
print("몫 연산 :", int(number1 / number2))
print("나머지 연산 :", number1 % number2)

# 문제7
num1 = int(input("첫 번째 숫자를 입력해주세요 >")) 
num2 = int(input("두 번째 숫자를 입력해주세요 >")) 
num3 = int(input("세 번째 숫자를 입력해주세요 >")) 
print(int((num1 + num2 + num3)/3))

# 문제 8
number3 = int(input("첫 번째 숫자를 입력해주세요 >"))
number4 = int(input("두 번째 숫자를 입력해주세요 >")) 
number5 = int(input("세 번째 숫자를 입력해주세요 >")) 
number6 = int(input("네 번째 숫자를 입력해주세요 >")) 
number7 = int(input("다섯 번째 숫자를 입력해주세요 >")) 
B = [number3, number4,number5,number6,number7]
print(B)

# 문제9
A = input("문자열을 입력해주세요 >")
num4 = int(input("숫자를 입력해주세요 >"))
print(A * num4)

# 문제10
a = int(input("첫 번째 숫자를 입력해주세요 >"))
print(a)
b = int(input("두 번째 숫자를 입력해주세요 >"))
print(a + b)
c = int(input("세 번째 숫자를 입력해주세요 >"))
print(a + b + c)
d = int(input("네 번째 숫자를 입력해주세요 >"))
print(a + b + c + d)
e = int(input("다섯 번째 숫자를 입력해주세요 >"))
print(a + b + c + d + e)

# 문제10 풀이
result = 0
a = int(input("첫 번째 숫자를 입력해주세요 >"))
result += a
print(result)
b = int(input("두 번째 숫자를 입력해주세요 >"))
result += b
print(result)
c = int(input("세 번째 숫자를 입력해주세요 >"))
result += c
print(result)
d = int(input("네 번째 숫자를 입력해주세요 >"))
result += d
print(result)
e = int(input("다섯 번째 숫자를 입력해주세요 >"))
result += d
print(result)

result = 0
result += int(input("첫 번째 숫자를 입력해주세요 >"))
print(result)
result += int(input("두 번째 숫자를 입력해주세요 >"))
print(result)
result +=int(input("세 번째 숫자를 입력해주세요 >"))
print(result)
result += int(input("네 번째 숫자를 입력해주세요 >"))
print(result)
result += int(input("다섯 번째 숫자를 입력해주세요 >"))
print(result)