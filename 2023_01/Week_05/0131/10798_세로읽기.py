
words = []

for i in range(5):
    word = input()
    words.append(word)

for i in range(max(len(w) for w in words)):
    for j in range(5):
        if i < len(words[j]):
            print(words[j][i],end='')
