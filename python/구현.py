# 문제 1
# 문자열을 입력받고, e 가 처음 나오는 위치(index)를 출력하세요.
# 만약, 문자열에서 e 가 없으면 -1 을 출력하세요.
# 단, index() / find() 메서드는 사용하지마세요.

a = input("문자열을 입력하세요 >")
cnt = 0
for i in a:
    if 'e' not in a:
        print(-1)
        break
    elif 'e' not in i:
        cnt += 1
    elif 'e' in i:
        print(cnt)

# 문제 2
# 문자열을 입력받고, 각 단어의 등장 횟수를 출력하세요.
# 단, count() 메서드는 사용하지마세요.

b = input("문자열을 입력하세요 >").split()
print(len(b))

#문제 3
# 문자열을 입력받고, e 를 제거한 결과를 출력하세요.
# 단, replace() 메서드는 사용하지 마세요.

x = input('문자열을 입력하세요 >')
num = x.index('e') 
y = x[:num] + x[num+1:]
print(y) 

# 문제4
# 문자열과 알파벳을 공백으로 구분해서 입력받고,문자열에서 입력한 알파벳의 개수를 출력하세요.
# 단, count() 메서드는 사용하지마세요.
# a, b = input('문자열을 입력하세요 >').split()
cnt = 0
for i in a:
    if b in i :
        cnt += 1
    elif b in i:
        cnt = 0
print(cnt)

# 문제5
# 단어 3개를 입력받고, 3개의 단어를 - 로 연결해서 출력하세요.
# 단, join() 메서드는 사용하지마세요.

a = input('문자열을 입력하세요 >').split()

# 문제 6
# 양의 정수를 입력받고, 자리수의 합을 출력하세요.
# 만약, 입력 받은 값이 0보다 작으면 -1을 출력하세요.
# 단, 양의 정수를 문자열로 변경하지마세요. str() 함수를 사용하지마세요.

num = input("양의 정수를 입력하시오> ")

lst = []
for i in range(len(num)):
    lst.append(int(num[i]))
print(sum(lst))

# 문제6 풀이
n = int(input())

if n < 0:
    print(-1)
else:
    reseult = 0
    while n > 0:
        reseult =+ n%10
        n //= 10
    print(reseult)



    
