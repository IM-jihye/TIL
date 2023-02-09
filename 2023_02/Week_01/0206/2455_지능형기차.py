
train = []
result = 0

for i in range(4):
    a, b = map(int, input().split())   
    
    result = result - a + b 
    # 32
    # 32 - 3 + 13 = 42
    # 42 - 28 + 25 = 39
    train.append(result)
        
print(max(train))