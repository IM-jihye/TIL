# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# print(num1*num2*num3)

a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))
for i in range(10):
    print(result.count(str(i)))