class DataProcessor:
    def __init__(self):
        self.start_date_list = []
        self.end_date_list = []
        self.notional_list = []

    def reset(self):
        self.start_date_list = []
        self.end_date_list = []
        self.notional_list = []

    def convert_list_to_text(self, a_list, remove_char=""):
        return ";".join(a_list).replace(remove_char, "")

    def Print_result(self, notional_data, start_date_data, end_date_data):
        res = (
            f"기간별 명목금액: {notional_data}\n"
            f"기간별 명목금액 시작일: {start_date_data}\n"
            f"기간별 명목금액 종료일: {end_date_data}"
        )
        print(res)

    def process_samsung_ir_swp_amortised(self, data):
        self.reset()
        rows = data.strip().split("%")[1:]

        for row in rows:
            try:
                items = row.split()
                self.start_date_list.append(items[6])
                self.end_date_list.append(items[7])
                self.notional_list.append(items[0])
            except IndexError:
                print(f"Error: 잘못된 데이터 형식 -> {row}")

        start_date_res = self.convert_list_to_text(self.start_date_list, "-")
        end_date_res = self.convert_list_to_text(self.end_date_list, "-")
        notional_res = self.convert_list_to_text(self.notional_list, ",")

        self.print_result(notional_res, start_date_res, end_date_res)

    def process_nh_investment(self, data):
        self.reset()
        rows = [line.strip() for line in data.strip().split("\n") if line.strip()]

        valid_data = [row for row in rows if row.startswith("2")]
        for row in valid_data:
            try:
                items = row.split()
                self.start_date_list.append(items[0])
                self.end_date_list.append(items[1])
                self.notional_list.append(items[4])
            except IndexError:
                print(f"Error: 잘못된 데이터 형식 -> {row}")

        start_date_res = self.convert_list_to_text(self.start_date_list, "-")
        end_date_res = self.convert_list_to_text(self.end_date_list, "-")
        notional_res = self.convert_list_to_text(self.notional_list, ",")

        self.print_result(notional_res, start_date_res, end_date_res)


def main():
    input_type = input(
        '''
        1. 삼성증권
        2. NH투자증권권
        데이터 송신처 번호를 입력해주세요: ''').strip()
    
    if input_type not in ["1", "2"]:
        print("잘못된 번호를 입력하셨습니다.")
        return

    print("\n데이터를 입력한 후 빈 줄을 입력하여 종료하세요:\n")
    user_input = []
    while True:
        try:
            line = input()
            if not line.strip():
                break
            user_input.append(line)
        except EOFError:  # Handle Ctrl+D
            break

    data = "\n".join(user_input)
    processor = DataProcessor()

    if input_type == "1":
        processor.process_samsung_ir_swp_amortised(data)
    elif input_type == "2":
        processor.process_nh_investment(data)

    input("종료하시려면 아무 버튼을 눌러주세요.")

if __name__ == "__main__":
    main()
