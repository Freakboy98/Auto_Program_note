import pandas as pd
import numpy as np
import openpyxl as xl

# 엑셀 파일의 시트 이름을 가져오는 함수
def get_sheet_title(file_path):
    wb = xl.load_workbook(file_path)
    wb_names = wb.sheetnames
    print(wb_names)
    return wb_names

# 엑셀 파일을 읽어오는 함수
def file_read(file_name, sheet_name):
    df = pd.read_excel(file_name, sheet_name=sheet_name)
    print(df)
    return df

# 엑셀 파일에 데이터를 추가하고 저장하는 함수
def upload_excel(file_name, sheet_name, df):
    # 새로운 행 추가
    new_row = {"업체명": "민상그룹","담장자":"김민상", "주소": "서울 영등포구", "전화": "010-2499-9554", "비고": "-"}
    df = df._append(new_row, ignore_index=True)
    
    with pd.ExcelWriter(file_name, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)
    print("complete!!!")
    print(df)

def main():
    file_name = "test.xlsx"
    file_path = r"C:\Users\user\Desktop\업무 자동화 프로그램 개발 폴더\test.xlsx"
    
    # 시트 이름 출력
    sheet_names = get_sheet_title(file_path)
    
    sheet_name = input("원하는 시트 이름을 입력하세요: ")
    
    # 입력한 시트 이름이 유효한지 확인
    if sheet_name not in sheet_names:
        print("잘못된 시트 이름입니다.")
        return
    
    # 엑셀 파일 읽기
    df = file_read(file_name, sheet_name)
    
    # 전화번호 변경
    df.loc[1, "전화"] = "010-2499-9554"
    print(df)
    
    # 수정된 내용을 엑셀 파일에 저장
    upload_excel(file_name, sheet_name, df)

if __name__ == "__main__":
    main()
