def solution(s):
    left = 0
    right = 0
    i = 0

    while i < len(s):
        if s[i] == '(':
            left += 1
        else:
            right += 1

        # 지금까지 열린 괄호보다 닫힌 괄호가 많으면 실패
        if right > left:
            return False

        i += 1

    # 끝까지 확인한 뒤, 열린 괄호가 모두 닫혔는지 검사
    return left == right