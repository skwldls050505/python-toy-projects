

# 좌석 예매 함수
def seat_booking(reserved_seat):
    print("좌석 예매를 시작합니다 *_* \n ")
    seat_num = input('예약할 좌석을 입력하세요 (예: A10, B12) : ').strip()
    seat_num = seat_num.upper()

    try:
        if seat_num[0] not in ('A', 'B', 'C', 'D', 'E', 'F') or int(seat_num[1:]) not in range(1,21):
            print("좌석은 A ~ F 행, 1 ~ 20 번까지 선택 가능합니다. ")

        elif seat_num in reserved_seat:
            print("해당 좌석은 이미 예약 중입니다. 다른 좌석을 입력해주세요.")
            

        else:
            reserved_seat.append(seat_num)
            print(f"{seat_num} 좌석 : 예약 성공 !")

    except (ValueError, IndexError):
        print('잘못된 좌석 번호 입니다 ..')




# 좌석 예매 취소 함수
def seat_cancellation(reserved_seat):
    seat_num = input("예약 취소할 좌석을 입력해주세요 (예: A10, B12) :  ").strip()
    seat_num = seat_num.upper()

    if seat_num in reserved_seat:
        reserved_seat.remove(seat_num)
        print(f"{seat_num} 취소 완료 !")

    else :
        yn = input('해당 좌석은 예약되어있지 않습니다. 예약을 원하십니까? (y/n): ')
        yn = yn.lower()
        if yn == 'y':
            seat_booking(reserved_seat)
        

        



# 좌석 조회 함수
def seat_check(seats, reserved_seat):

    print("\n 현재 예약된 좌석들 : ", reserved_seat)

    print("\n                     SCREEN")
    print("------------------------------------------------- \n")
    print("  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20")

    for i in range(len(seats)):
        print(seats[i][0][0], end = ' ')
        
        for j in range(len(seats[i])):
            
            if j == 10:
                print(" ", end = ' ')

            if seats[i][j] in reserved_seat:
                print('■', end = " ")
                
            else:
                print('□', end = " ")
                
        print()


