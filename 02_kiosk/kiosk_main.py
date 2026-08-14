# 키오스크 메인 구현
import kiosk_order
import kiosk_menu

def input_menu():
    while True:
        input_menu = input("주문할 메뉴를 입력해주세요: ").strip()
        if input_menu not in (menu.basic_menu):
            print("잘못된 메뉴입니다. 다시 입력하세요.")
            continue
        else:
            return input_menu
        
def input_menu_cnt(input_menu_result):
    while True:
            try:
                input_cnt = int(input(f"{input_menu_result}의 수량 입력해주세요: "))
            except ValueError :
                print('수량을 제대로 입력해주세요.')
                continue

            if input_cnt <= 0:
                print("수량은 1 이상 입력해주세요. ")
                continue

            return input_cnt

            
def main():

    menu.insert_menu()

    while True:

        print("• 카페 키오스크 주문하기 start • \n ")

        menu.show_menu()
        input_menu_result = input_menu()
        input_cnt = input_menu_cnt(input_menu_result)
        


        input_price = menu.basic_menu[input_menu_result]

        order.add_cart(input_menu_result, input_price, input_cnt)
        total_pay = order.show_cart()
        print("추가 주문 : 1 \n결제 : 2 \n장바구니 초기화 : 3 \n 그 외 : 키오스크 종료 \n")
        num = int(input('>>'))

        if num == 1:
            continue
        elif num == 2:
            payment_result = order.payment(total_pay)
            if payment_result == "종료" :
                return "키오스크 종료"
            elif payment_result == "계속 담기":
                continue
            elif payment_result == "다시 장바구니 담기" :
                continue
            elif payment_result == "결제 취소" :
                continue
            elif payment_result == "결제 완료" :
                break 
        elif num ==3:
            order.cart = []
        else:
            return "프로그램 종료"
            


if __name__ == "__main__":
    menu = kiosk_menu.Menu()
    order = kiosk_order.Order()
    main()