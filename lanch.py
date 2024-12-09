import random

lunch_data = {
    "한식": ["계림","순남시래기","향토식당","향토칼국수","순대국","미스터초우","오봉집","소공동","오징어","진순대","독토"],
    "양식": ["바스버거","폴트버거","부리토 & 퀘사디아","홈","버거킹"],
    "일식": ["무공","저스트텐동"],
    "중식": ["가양", "팔당반점", "마라탕","우육면"]
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
