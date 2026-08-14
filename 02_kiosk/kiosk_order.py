class Order:

    def __init__(self):
        self.cart = []


    def show_cart(self): # 장바구니 출력
        total = 0
        print("\n ╔═══════ MY 장바구니 ═══════╗ \n")
        if not self.cart :
            print("장바구니 텅텅 ~ :( \n")
        else:
            
            for i in self.cart:
                print (f'{i["name"]} :  {i["price"]}  x  {i["cnt"]} = {i["price"] * i["cnt"]}\n')
                total += i["price"] * i["cnt"]
                if total == 0 :
                    self.cart = []
            
            print(f'TOTAL 금액: {total}')
            print(" ╚═══════════════════════════╝ \n")
        return total

            


    def add_cart(self, menu_name, menu_price, menu_cnt): # 장바구니 메뉴 추가

        add_menu = {"name": menu_name, "price": menu_price, "cnt": menu_cnt}
        self.cart.append(add_menu)
        return "추가 완료"

        


    def payment(self, total_pay): # 총 금액 계산 + 결제
        total = 0
        if  total_pay == 0:
            print("장바구니가 비워져있어요 . . :( \n")
            while True:
                try:
                    payment_chk = int(input("1. 종료 \n2. 계속 담기 \n >>"))
                    match payment_chk:
                        case 1:
                            return "종료" # 종료
                        case 2:
                            return "계속 담기" # 계속 담기
                        case _:
                            print("1 ~ 2만 입력하세요 !! ")
                except ValueError:
                    print("1 ~ 2 만 입력하세요 !! ")
                    continue
                
        
        for i in self.cart:
                total += i["price"] * i["cnt"]

        while True:

            print(f"총 금액 : {total}\n")
            yn = input("결제를 원하시면 y를 눌러주세요 ! \n >> ")

            if yn.lower() == 'y':
                print("결제 완료 ! 키오스크 종료됩니다 <3 ")
                self.cart =[]
                return "결제 완료"
            else:
                try:
                    chk = int(input("다시 장바구니 담기: 1 \n 결제 계속 진행: 2 \n 결제 취소: 3 \n >> "))
                    match chk:
                        case 1:
                            return "다시 장바구니 담기" # 다시 장바구니 담기
                        case 2:
                            continue
                        case 3:
                            return "결제 취소" # 결제 취소
                        case _:
                            print("1 ~ 3만 입력하세요 !!")
                except ValueError:
                    print("1 ~ 3 만 입력하세요 !!")