# if 상품군과 날짜를 입력
# then 입력 받은 상품군와 날짜의 파일을 읽는다. -> how? 한줄 씩 읽되 맨 뒤에 개행문자는 제거한다.
# thwn 위 과정을 file 맨 마지막까지 반복한다.
# then 2차원 데이터를 평탄화 한다.
# then 위 과정을 거친 데이터를 csv 형태로 변경한다.
# then local pc에 저장한다.

import pandas as pd
import json
import os
from IPython.display import display
# 상품군 입력 단순화
type,date = input("상품군 날짜:").split()
finance_type = ""
type = type.upper()

if type == "CO" :
    finance_type = "Commodities"
elif type == "CR" :
    finance_type = "Credit"
elif type == "EQ" :
    finance_type = "Equity"
elif type == "FX" :
    finance_type = "Foreign_Exchange"
elif type == "RA" :
    finance_type = "Rates"
else :
    finance_type = "Other"

# 상품군과 날짜를 입력
def convert_file_to_csv(type, date):

    # path 생성
    absolute_path = os.getcwd()
    file_path = f"{absolute_path}/{type}-{date}.records" # local에서 대상 파일의 절대 경로 넣기

    # 파일 내용 읽기
    try:
        data_of_json = []

        with open(file_path, "r") as file:
            for line in file:
                data_of_json.append(json.loads(line.strip())) # "\n"제거

        
        df = pd.json_normalize(data_of_json)
        display(df)
        # 기존 파일과 같은 이름의 csv로 저장
        csv_file_path = f"{type}-{date}.csv"
        df.to_csv(csv_file_path,index = False)
        print(f"csv file download complete!!! : {csv_file_path}")

    except Exception as e:
        print(f"error!!! {e}")



convert_file_to_csv(finance_type,date)


### 범위 설정을 하고 인덱스롷 만들거나

# 데이터의 헤더 별로 스플릿
## 헤더 부분의 제외하고 평탄화 
### 위 과정을 모든 해더에 대해 완료
#### 병합

