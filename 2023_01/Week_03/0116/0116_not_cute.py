# 첫 번째 줄에 설문조사를 한 사람의 수 N (1 ≤ N ≤ 101, N은 홀수)가 주어진다.
# 다음 N개의 줄에는 각 줄마다 각 사람이 설문 조사에 어떤 의견을 표명했는지를 나타내는 정수가 주어진다. 0은 준희가 귀엽지 않다고 했다는 뜻이고, 1은 준희가 귀엽다고 했다는 뜻이다.

N = int(input())
cut = 0
not_cute = 0
for i in range(N):
    if int(input())==1:
        cut +=1
    else:
        not_cute +=1
    
if cut > not_cute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")