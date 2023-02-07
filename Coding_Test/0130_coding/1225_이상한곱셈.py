# a,b = input().split()
# a = list(map(int,a))
# b = list(map(int,b))

# print(sum(a)*sum(b))

# t = int(input())
# cnt = 0

# for i in range(t):
#     word = str(input())
    
#     print('#',word)

alp = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = str(input())

for i in alp:
    word = word.replace(i,'*')

print(len(word))
