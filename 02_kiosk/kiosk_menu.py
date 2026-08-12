class Menu:


    def __init__(self):
        self.basic_menu = {
    "아메리카노": 3000,
    "카페라떼": 4000,
    "바닐라라떼": 4500,
    "디카페인 아메리카노" : 3500,
    "녹차라떼" : 3500,
    "카푸치노" : 3500,
    "카라멜마끼야또" : 3500,
    "매실애플티" : 3500,
    "플랫화이트" : 3500,
    "밀크티" : 3500
}


    def show_menu(self): # 메뉴 출력 함수
        print('==== 메뉴판 =======')
        for i in self.basic_menu:
            print(f'{i} : {self.basic_menu[i]}원')
        print('=================')



    def insert_menu(self): # 메뉴 추가 (파일 입출력)

        try:
            with open ("02_kiosk/kiosk_data/menu.txt", "r", encoding="utf-8") as file:
                for i in file:

                    new_menu, new_menu_price = i.strip().split(',')

                    if new_menu not in self.basic_menu:
                        self.basic_menu[new_menu] = int(new_menu_price)

                print('신메뉴 등록 완료 🥄')


        except FileNotFoundError :
           print('파일이 존재하지 않습니다 ! ! ! \n')