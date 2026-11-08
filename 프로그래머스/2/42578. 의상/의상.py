def solution(clothes):
    counts={}
    for cloth in clothes:
        counts[cloth[1]]= counts.get(cloth[1],0)+1
    answer = 1
    for count in counts.values():
        answer*=count+1
    return answer-1
# 각 종류에서 하나를 입거나 안 입을 수 있으므로 (의상 개수 + 1)
# 종류별 선택지 수를 모두 곱하면 전체 조합의 수
# 아무것도 안 입는 조합 1개를 제외하기 위해 마지막에 -1