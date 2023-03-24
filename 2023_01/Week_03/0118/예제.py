# 팰린드롬인지 확인하기
a = str(input())
if a == a[::-1]:
    print(1)
else:
    print(0)

# 문자열 반복
T = int(input())

for i in range(T):
    R,S = input().split()
    R = int(R) # 형변환
    S = str(S)
    for i in range(len(S)):
        print(R*S[i],end='')
    print()

# 유학금지
word = input()

for i in 'CAMBRIDGE':
    word = word.replace(i,"")
print(word)

# 태보태보 총난타
# 태보(TaeBo)란, 태권도와 복싱을 조합한 운동이다. 복싱의 공격 기술로는 민첩하게 앞주먹을 뻗으면서 가볍게 치는 잽, 옆으로 치는 펀치인 훅이 있다.
# 선풍적인 인기에 태보 강의를 들으며 태보를 마스터한 혜정이는 이제 펀치 속도가 워낙 빨라서 잽과 훅을 반복하다보면 잔상이 남는다.
# 얼굴의 왼편에 왼손의 잔상이, 오른편에는 오른손이 잔상이 남을 때 혜정이는 주먹을 몇 번 뻗었을까?
# 주먹의 잔상은 =로 시작하여 @로 끝나고, 잔상이 남지 않는 경우는 없다. 얼굴 형태가 (^0^) 꼴이고, 주먹의 잔상이 같은 곳에 위치하지 않는다.

# 알파벳찾기
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.
S = input()
abc ='abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in S:
        print(S.index(i), end= ' ')
    else:
        print( -1, end =' ')

# 크로아티아 알파벳
alp = ('c=','c-','dz=','d-','lj','nj','s=','z=')
word = input()
for i in alp:
    word = word.replace(i,"*")
print(len(word))