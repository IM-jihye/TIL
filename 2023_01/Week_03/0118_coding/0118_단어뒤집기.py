# 각 테스트 케이스에 대해서, 입력으로 주어진 문장의 단어를 모두 뒤집어 출력한다.
T = int(input())

for i in range(T):
    string = list(input().split())
    for j in string:
        print(j[::-1],end=' ')