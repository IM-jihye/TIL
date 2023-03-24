# 세탁소 사장 동혁
# 쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)

# 3

# 124
# 25
# 194

# 4 2 0 4
# 1 0 0 0
# 7 1 1 4
num = int(input())
a = int(num/25) 
b = int((num-(25*a))/10)
c = int((num -((a*25)+(b*10)))/5)
d = int((num -((a*25)+(b*10)))) # 124 (100+20)
print(a,b,c,d)

# t = int(input())
# for i in t:
#     money = int(input())
#     if money >= 100:
#         num = (money/25)
# print(194/25)
# print(194*7)
# n = int(input())

