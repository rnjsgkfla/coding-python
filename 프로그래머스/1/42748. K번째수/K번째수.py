def solution(array, commands):
    answer = []
    # i에서 commands배열의 크기만큼 루프(내부 배열 순차적 처리)
    for i in range(len(commands)):
        # array 배열 슬라이싱 (a[p:q]는 a[p]~a[q-1]까지 슬라이싱)
        # => 그래서 시작 숫자는 p-1, 끝은 그냥 q
        tmp1=array[commands[i][0]-1:commands[i][1]]
        # tmp1 정렬 후 tmp2에 저장. 굳이 정렬 알고리즘 구현안함.
        # 데이터 입력 크기도 작아서 그냥 기본 정렬 사용해도 ㄱㅊ
        # tmp1.sort()는 none을 반환하기 때문에 밑에처럼 대입하면 안됨. 쓰려면
        # tmp1.sort()
        # answer.append(tmp[commands[i][2]-1])
        tmp2=sorted(tmp1)
        # answer에다가 append
        answer.append(tmp2[commands[i][2]-1])
        
    return answer
