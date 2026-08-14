def solution(n):
    strn = str(n)
    answer = []
    tmp = []
    for i in strn:
        tmp.append(int(i))
    answer = tmp[::-1]
    #print(answer)
    return answer