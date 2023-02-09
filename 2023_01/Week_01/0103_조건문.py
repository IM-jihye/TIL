# 실습
num = int(input("숫자를 입력하세요"))
if num % 2 == 0 :
    print('짝수')
else :
    print('홀수')

# 실습
dust = 80

if dust > 150 :
    print('매우나쁨')
elif dust > 80 :
    print('나쁨')
elif dust > 30 :
    print('보통')
else :
    print('좋음')
print('미세먼지 확인 완료')

# 실습 for

num = int(input('정수를 입력하세요>'))
sum = 0

for i in range (1,num+1):
    sum += i

print(sum)

# 실습 while

n=0
num1 = 10
result = 0

while num1 >= n:
    result += n
    n+=1
print(result)



