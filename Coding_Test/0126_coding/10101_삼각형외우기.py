# 삼각형 외우기
# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error

a = int(input())
b = int(input())
c = int(input())

if a == b== c == 60 :
    print('Equilateral')
elif a + b + c == 180 and a == b :
    print('Isosceles')
elif a + b + c == 180 and a == c :
    print('Isosceles')
elif a + b + c == 180 and b == c :
    print('Isosceles')
elif a + b + c == 180 and a != b != c:
    print('Scalene')
else:
    print('Error')