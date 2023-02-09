word = str(input())

for i in range(len(word)):
    for j in range(i+1,len(word)-1):
        a = word[:i]
        b = word[i:j]
        c = word[j:]

    print(a)
    print('#',b)
    print(c)


# sort
# prin(index[0])