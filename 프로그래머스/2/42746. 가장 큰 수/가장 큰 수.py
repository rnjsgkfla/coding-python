# def solution(numbers):
#     answer = ''
#     arr=[]
#     for i in range(len(numbers)):
#         arr.append(str(numbers[i]))
#     # 버블정렬
#     for i in range(len(arr) - 1):
#         for j in range(len(arr) - 1 - i):
#             a = arr[j]
#             b = arr[j + 1]

#             if a + b < b + a:
#                 arr[j], arr[j + 1] = b, a

#     for num in arr:
#         answer += num

#     return answer

def solution(numbers):
    answer=''
    # 이어 붙이기와 문자열 비교를 위해 변환
    arr = [str(num) for num in numbers]

    # 원소 범위가 0~1000인 조건을 활용한 내림차순 정렬
    arr.sort(key=lambda x: x * 3, reverse=True)

    # 정렬 후 첫 원소가 "0"이면 모든 원소가 0
    if arr[0] == "0":
        return "0"

    # 정렬된 문자열을 공백 없이 연결
    answer=''.join(arr)
    return answer