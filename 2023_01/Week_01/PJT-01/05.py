import json

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 영화 데이터 movie.json 을 활용하여 필요한 정보로만 구성된 딕셔너리를 출력하세오.
# 코드 작성 전 movie.json 의 데이터 구조를 파악하세요. 
print(type(movie))
# movie.json 파일에서 읽은 데이터는 변수 movie 에 저장됩니다.

# 0. 해당되는 key를 list에 담기
key_list = ['id','title','vote_average','overview','genre_ids']
# 1. 새로운 dictionary를 담을 변수 선언
movie_dict = {}
# 2. key_list 요소에 해당하는 정보만 추출 (for문 이용)
for key in key_list:
    movie_dict[key] = movie[key]
print(movie_dict)
print(type(movie))



