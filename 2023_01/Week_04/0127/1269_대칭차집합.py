a,b = map(int,input().split())
a_ = set(map(int,input().split()))
b_ = set(map(int,input().split()))
print(len(a_-b_) +len(b_-a_))




