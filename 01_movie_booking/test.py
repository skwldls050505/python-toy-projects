

# def max_num(number_list):
#     max_number = number_list[0]
#     for num in number_list:
#         if num > max_number:
#             max_number = num

#     return max_number


# def min_num(number_list):
#     min_number = number_list[0]
#     for num in number_list:
#         if num < min_number:
#             min_number = num

#     return min_number

# def midd_num(number_list):
#     number_list.sort()
#     midd_num = number_list[len(number_list ) // 2] 
#     return midd_num



# midd = midd_num([8,6,2,8,5,1,2,5,4,9])
# print("중간값은 : ", midd)
# max = max_num([8,6,2,8,5,1,2,5,4,9])
# print("최댓값은 : ", max)
# min = min_num([8,6,2,8,5,1,2,5,4,9])
# print("최솟값은 : ", min)




# import random # 무작위에 대한 프로그램/모듈

# lst = [
#     random.randint(0,9) for _ in range(random.randint(5,9))
# ]

# def func(p_lst):
#     # 1. 리스트에 있는 데이터들을 정렬해야 함. => sort()
#     p_lst.sort() # 정렬

#     # 2. 가장 작은 수 찾기 => [0]
#     mininum = p_lst[0]

#     # 3. 가장 큰 수 찾기 => [-1]
#     maximum = p_lst[-1]

#     # 4. 중간값/중위값
#     if len(p_lst) % 2 != 0:
#         # 4-1. 만약 전체 데이터의 수가 홀 수 이면, 가운데 값 찾기 => %2 != 0
#         # print("홀수")
#         median = p_lst[len(p_lst)//2]
#     else:
#         # 4-2. 만약 전체 데이터의 수가 짝 수 이면, 가운데 2개의 값의 평균값 사용하기 
#         # print("짝수")
#         median = (p_lst[len(p_lst)//2-1] + p_lst[len(p_lst)//2])/2

#     # 5. 결과 확인 
#     # print(p_lst)
#     return f"{mininum} / {maximum} / {median}"


import random

def rsp(user, computer):
    rsp_win_list = {"바위": "가위", "가위": "보", "보": "바위"}

    if user == computer:
        return f'비겼습니다. 컴퓨터 : {computer} / 사용자 : {user}'
    
    elif rsp_win_list[user] == computer:
        return f'사용자가 이겼습니다. 컴퓨터 : {computer} / 사용자 : {user}'
    else:
        return f'컴퓨터가 이겼습니다. 컴퓨터 : {computer} / 사용자 : {user}'

    

computer = random.choice(["가위", "바위", "보"])

user = input("가위, 바위, 보 중 하나를 입력하세요 : ").strip()

rsp_result = rsp(user, computer)

print(rsp_result)


    

