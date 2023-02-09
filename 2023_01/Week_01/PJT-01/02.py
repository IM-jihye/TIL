with open('data/fruits.txt','r', encoding='UTF8') as file:

    count = 0
    for i in file:
        count +=1
    print(count)
    
