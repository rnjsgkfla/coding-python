# 정렬 전: ["123", "12"]
# "12".startswith("123") → False
# 접두어 관계를 놓쳐서 True를 반환

# 정렬 후: ["12", "123"]
# "123".startswith("12") → True
# 접두어 관계를 발견해서 False를 반환
# 이중루프문으로 인해 시간초과
# def solution(phone_book):
    # phone_book.sort()
    # for i in range(len(phone_book)):
    #     check=phone_book[i]
    #     for j in range(i+1,len(phone_book)):
    #         if phone_book[j].startswith(check):
    #             return(False)
    # return(True)


# 문자열을 사전순으로 정렬하면 짧은 번호가 앞에 와서 뒤 번호가 앞 번호로 시작하는지만 확인하면 됨

def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True
