import random

lunch_data = {
    "한식": ["국밥", "냉면", "제육", "오징어볶음","시레기국","닭볶음탕"],
    "양식": ["버거","서브웨이"],
    "일식": ["모밀", "돈까스", "덮밥"],
    "중식": ["짜장면", "볶음밥", "짬뽕", "마라탕","우육면"]
}

def get_random_lunch():
    # 대분류 메뉴 선택
    category_key = random.choice(list(lunch_data.keys()))
    # 세부 메뉴 선택
    menu = random.choice(lunch_data[category_key])
    return menu

def main():
    while True:
        print("점심 메뉴 결정에 도움 드리겠습니다.")
        result = get_random_lunch()
        print("오늘 점심으로", result, "어떠세요?")
        
        continue_choice = input("계속 하시겠습니까? (yes/no): ").strip().lower()
        if continue_choice == "no":
            break

if __name__ == "__main__":
    main()
