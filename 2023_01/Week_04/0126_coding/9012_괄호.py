# 괄호

string = "(()())((()))"

# 왼쪽 괄호를 저장하고 제거할 스택(파이썬 리스트)
left_bracket = []

for bracket in string:
    # 괄호가 왼쪽 괄호일 떄
    if bracket == '(':
        left_bracket.append(bracket)
    
    # 괄호가 오른쪽 괄호일 때
    if bracket == ")":
        
        """
        조건 1. 남은 왼쪽 괄호가 없을 때 -> left bracket 길이가  0
        조건 2. 남은 왼쪽 괄호가 있을 때 '(' 만나는 경우
        """
        if len(left_bracket) == 0:
            #올바른 괄호 문자열 x
            print('올바른 괄호 문자열이 아닙니다.')
            break
        else :
            left_bracket.pop()
else:
    if len(left_bracket) > 0:
        print('올바른 괄호 문자열이 아닙니다.')
    else:
        print('올바른 괄호 문자열 입니다.')   
    print(left_bracket)