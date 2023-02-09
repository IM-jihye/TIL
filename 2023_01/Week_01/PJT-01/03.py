# 3. 텍스트 파일 데이터 활용 - 특정 단어 추출
#과일 데이터 fruits.txt를 활용하여 이름이 berry로 끝나는 과일의 개수와 목록을 03.txt 에 기록하세요.

with open('data/fruits.txt','r', encoding='UTF8') as file:
    data = file.read()
    #print(data)

    cnt = 0
    for i in data:
        if 'berry' in data:
            cnt += 1
    print(i)
         
    


