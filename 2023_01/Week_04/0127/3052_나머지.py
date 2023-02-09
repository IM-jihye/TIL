# arr = [] 
# for i in range(10):
#     num = int(input())
#     arr.append(num % 42)
# arr = set(arr) # set 중복제거
# print(len(arr))

arr = []

for i in range(10):
    a = int(input())
    arr.append(a % 42)

arr = set(arr)
print(len(arr))