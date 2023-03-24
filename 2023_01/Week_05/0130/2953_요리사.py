
scores = []
for i in range(5):
    numbers = map(int,input().split())
    score = sum(numbers)
    scores.append(score)

print(scores.index(max(scores))+1,max(scores))
    