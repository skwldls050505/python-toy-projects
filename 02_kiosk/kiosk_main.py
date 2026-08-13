# 키오스크 메인 구현
import kiosk_order
import kiosk_menu


def main():
    menu = kiosk_menu.Menu()
    order = kiosk_order.Order()

    menu.insert_menu()

    while True:
        print("• 카페 키오스크 주문하기 start • \n ")

        menu.show_menu()

        input_menu = input("주문할 메뉴를 입력해주세요: ").strip()
        input_cnt = int(input(f"{input_menu}의 수량 입력해주세요: "))
        input_price = menu.basic_menu[input_menu]
        order.add_cart(input_menu, input_price, input_cnt)
        order.show_cart()
        print("추가 주문: 1번, 결제: 2번, 장바구니 초기화: 3번 키오스크 종료: 4번 \n")
        num = int(input())
        if num == 1:
            continue
        elif num == 2:
            order.payment()
        elif num ==3:
            order.cart = []
        else:
            return "프로그램 종료"
            

if __name__ == "__main__":
    main()