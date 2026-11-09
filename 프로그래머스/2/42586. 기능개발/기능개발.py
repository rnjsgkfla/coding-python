def solution(progresses, speeds):
    answer = []
    leftover=[]
    leftdays=[]
    count=1
    for i in range(len(progresses)):
        leftover.append(100-progresses[i])
    for i in range(len(leftover)):
        if (leftover[i]%speeds[i])==0:
            leftdays.append(leftover[i]//speeds[i])
        else:
            leftdays.append((leftover[i]//speeds[i])+1)
    i=0
    while i<len(leftdays):
        count=1
        while i+count < len(leftdays) and leftdays[i]>=leftdays[i+count]:
            count+=1
        answer.append(count)
        i +=count
    return answer
