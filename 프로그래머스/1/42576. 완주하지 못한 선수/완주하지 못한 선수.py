def solution(participant, completion):
    answer = ''
    runners = {}

    for name in participant:
        runners[name] = runners.get(name, 0) + 1

    for name in completion:
        runners[name] -= 1

    for name, count in runners.items():
        if count > 0:
            answer = name
            break

    return answer