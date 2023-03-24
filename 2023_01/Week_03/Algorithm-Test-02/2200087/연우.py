# num1=10
# num2=num1+10
# print(num1,num2) # ?

# number1 = 10
# number2 = 5
# number3 = str(number1) + str(number2)
# number4 = number1 + number2

# print(number1, number2, number3, number4) # ? 10 5 105 15

# string1 = "Hello"
# string2 = string1
# string3 = "World" + "!"

# print(string2, "?", string3) #

# number1 = 5
# number2 = 10.0 + number1
# number1 - 5
# number3 = number1 * (number2 + 10)

# print(number1, number2, number3) # ? 5 15 125

# list_variable = [1, 2, 3, [1, 2, 3]]
# sub_list = list_variable[3][-1]

# print(sub_list) # ?

# list_variable = []
# list_variable.append(4)
# list_variable.append("b")
# list_variable[1] = 2

# print(list_variable) # ?

# name = input("너의 이름은?")

# print(name) # ?

# name = input("너의 이름은?")

# print(name) # ?

# a = int(input('정수형 숫자를 입력해주세요 >'))

# num=a+10

# print(num)

# a = input("좋아하는 음식을 입력해주세요 >")


# print("좋아하는 음식 :",a)

# a = (input("이름을 입력해주세요 >"))
# b = int(input("태어난 년도를 입력해주세요 >"))


# print(f'저의 이름은 {a}이고, 올해 나이는 ,{2024-b}세 입니다.')




# a=int(input("첫 번째 정수형 숫자를 입력해주세요 >"))

# print(a)

# b=int(input("두 번째 정수형 숫자를 입력해주세요 >"))

# print(a+b)

# c=int(input("세 번째 정수형 숫자를 입력해주세요 >"))

# print(a+b+c)

# d=int(input("네 번째 정수형 숫자를 입력해주세요 >"))

# print(a+b+c+d)

# e=int(input("다섯 번째 정수형 숫자를 입력해주세요 >"))

# print(a+b+c+d+e)

# a=str(input("문자열을 입력해주세요 >"))
# b=int(input("정수형 숫자를 입력해주세요 >"))

# print(a*b)

# a = 1
# b = 1
# print(a < b) # ? f

# a = bool("")
# print(a)
# b = False
# print(a == b) # ?

# a = input("d >")
# result = ""

# if a == "1":
#     result = True
# else:
#     result = False
    
# print(result) # ?

# a = 90

# if a == 90:
#     a = a + 10
    
# elif a == 100:
#     a = a + 10
    
# elif a == 110:
#     a = a + 10

# else:
#     a = a + 10

# a = a + 10
    
# print(a) # ?

# string = "hello world!"

# for element in string:
#     print(element)
    
# ? 세로로 하나씩

# list_variable = [0, 1, 2, 3, 4, 5, 6]

# for element in list_variable:
#     print(element, end=" ")
#     # 0 1 2 3 4 5 6

# n = 10

# for element in range(-n, n):
#     print(element, end=" ")
# # ? -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 


# n = 10

# for element in range(1, n + 1, 3):
#     print(element, end=" ")
#     #  1 4 7 10 1번부터 2번 이하까지 3번만큼 등차수열



# list_variable = [6, 5, 4, 3, 2, 1, 0] 

# # enumerate가 무엇인지 검색해보세요!
# for index, element in enumerate(list_variable):
#     print(index,element)

n = 10

for element in range(n, -n, -1):
    print(element, end=" ")
    if n < 0:
        break