# 문제 3
#입력과 같은 딕셔너리 변수가 있을 때, 해당 인물의 나이를 출력하세요.
# dict_variable = {
#     "이름": "정우영",
#     "생년": "2000",
#     "회사": "하이퍼그로스",
# }
# ### 이하 문제 해결 코드 작성
# if "나이" not in dict_variable:
#     dict_variable["나이"] = "24세"
#     print(dict_variable["나이"])

#나이 : 24세

#문제 4
#이름, 전화번호, 거주지 정보를 입력받아 딕셔너리 구조로 저장하고, 해당 딕셔너리와 딕셔너리의 정보를 구분해서 출력하세요.
# 이름을 입력하세요 > 정우영 # 사용자 입력
# 전화번호를 입력하세요 > 010-1234-5678 # 사용자 입력
# 거주지를 입력하세요 > 서울시 # 사용자 입력

# {'이름': '정우영', '전화번호': '010-1234-5678', '거주지': '서울시'}
# 이름 : 정우영
# 전화번호 : 010-1234-5678
# 거주지 : 서울시

# name = input("이름을 입력하세요 > ")
# number = input("전화번호를 입력하세요 >")
# live = input("거주지를 입력하세요 >")

# dict_variable = {
#     "이름": name,
#     "전화번호": number,
#     "거주지": live,
# }
# print(dict_variable)
# for i in dict_variable:
#     print(i,dict_variable[i])


# 문제5
# 이름, 전화번호, 이메일, 거주지 정보를 입력받아 출력 예시와 동일한 딕셔너리 구조를 출력하세요.
#Hint : 딕셔너리 안에 딕셔너리를 넣을 수 있습니다.

# 이름을 입력하세요 > 정우영 # 사용자 입력
# 전화번호를 입력하세요 > 010-1234-5678 # 사용자 입력
# 이메일을 입력하세요 > beemo@hphk.kr # 사용자 입력
# 거주지를 입력하세요 > 서울시 # 사용자 입력
# {'정우영': {'전화번호': '010-1234-5678', '이메일': 'beemo@hphk.kr', '거주지': '서울시'}}

# name = input("이름을 입력하세요 > ")
# number = input("전화번호를 입력하세요 >")
# email = input("이메일을 입력하세요 >")
# live = input("거주지를 입력하세요 >")

# dict_variable = {
#     name :
#     {"전화번호": number,
#     "이메일": email,
#     "거주지" : live}
# }
# print(dict_variable)