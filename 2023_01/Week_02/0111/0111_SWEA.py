# 2047. 신문 헤드라인 
# 문자열의 소문자를 모두 대문자로 변경한 결과를 출력한다.
a = 'The_headline_is_the_text_indicating_the_nature_of_the_article_below_it.'
print(a.upper())

# 2025. N줄덧셈 
# 주어진 숫자가 10 일 경우 출력해야 할 정답은,
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
number = int(input())
sum = 0
for i in range(1,number+1):
    sum += i
print(sum)

# 1936. 1대1 가위바위보
#A가 이기면 A, B가 이기면 B를 출력한다.
a,b = map(int,input().split())
if a == 1:
    if b == 2:
        print('B')
    elif b == 3 :
        print('A')
elif a == 2 :
    if b == 1 :
        print('A')
    elif b == 3 :
        print('B')
elif a == 3 :
        if b == 1 :
            print('B')
        elif b == 2 :
            print('A')

# 2027. 대각선 출력하기 
for i in range(5) :
    for j in range(5) :
        if i == j :
            print('#', end='')
        else :
            print('+',end ='')
    print()
 
# 2058. 자릿수 더하기
# 각 자릿수의 합을 출력한다.
n = int(input())
result = 0
while n > 0 :
    result += n%10
    n //= 10
print(result)

# 2019. 더블더블
# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
#주어질 숫자는 30을 넘지 않는다.
n = int(input())
for i in range(n+1):
    print(2**i,end=' ')

