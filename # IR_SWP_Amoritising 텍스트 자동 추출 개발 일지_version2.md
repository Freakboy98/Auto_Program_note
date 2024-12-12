## date : 2024-12-04
## made for nicepni
*** 
# IR_SWP_Amoritising  텍스트 자동 추출 개발 일지
***

# 1. Code


```python
    # global_var declear 
    start_date_text = ""
    end_date_text = ""
    notional_text = ""
    start_date_list = []
    end_date_list = []
    notional_list = []
```


## global 변수와 local 변수의 스코프 충돌로 인해 에러 발생!!
    따라서 global 변수를 사용하는 로컬 함수 안에 키워드 global을 추가하여 스코프 충돌을 피해야 한다.

### def Print()
``` python

    def Print(notional_data, start_date_data,end_date_data) :
        res = f'기간별 명목금액 : {notional_data} \n기간별 명목금액 시작일 : {start_date_data} \n기간별 명목금액 종료일 : {end_date_data}'
        print(res)
        return None
```

### def Samsung_IR_SWP_Amortised()
```python
    # Samsung IR_SWP_Amortised part
    def Samsung_IR_SWP_Amortised(data) :
        global start_date_text,end_date_text,notional_text # global 과 local 충돌을 피하기 위함
        global start_date_list,end_date_list,notional_list

        # global 변수 초기화
        start_date_text,end_date_text,notional_text = "","",""
        start_date_list,end_date_list,notional_list = [],[],[]

        #data read and data_set initialized
        row = data.strip()
        row = data.split("\n")
        row_list = row[1:]

        # data sliceing
        for item in row_list :
            each_price = item.split() # white space로 구분
            start_date_list.append(each_price[6])
            end_date_list.append(each_price[7])
            notional_list.append(each_price[0])

        # creat notional_price, initial_date,final_date to Text form
        for each_date in start_date_list :
            start_date_text = start_date_text + each_date + ";"
        for each_date in end_date_list :
            end_date_text = end_date_text + each_date + ";"
        for each_price in notional_list:
            notional_text = notional_text + each_price + ";"

        start_date_res = start_date_text.replace("-","")
        end_date_res = end_date_text.replace("-","")
        notional_res = notional_text.replace(",","")

        #print result
        Print(notional_res,start_date_res,end_date_res)
        return None
```

### def NH_Investment()
```python
    def NH_Investment(data) :
        global start_date_text,end_date_text,notional_text # global 과 local 충돌을 피하기 위함
        global start_date_list,end_date_list,notional_list

        # global 변수 초기화
        start_date_text,end_date_text,notional_text = "","",""
        valid_data,start_date_list,end_date_list,notional_list = [],[],[],[]
        

        ### == 변경 == ###
        data = data.strip()
        data = data.split("\n")
            
        for idx in range(len(data)) :
            # 길이가 40 under이면 해당row 제거
            if len(data[idx]) > 45 :
                data[idx] = data[idx].strip()
                valid_data.append(data[idx])
        # valid_data 추출완료

        for itr in valid_data :
            each_data = itr.split(" ")
            print(each_data,len(each_data))
            start_date_list.append(each_data[0])
            end_date_list.append(each_data[1])
            notional_list.append(each_data[4])


        for each_date in start_date_list :
            start_date_text = start_date_text + each_date + ";"
        start_date_text = start_date_text.replace("-","")
        for each_date in end_date_list :
            end_date_text = end_date_text + each_date + ";"
        end_date_text = end_date_text.replace("-","")
        for each_proce in notional_list :
            notional_text = notional_text + each_proce + ";"
        notional_text = notional_text.replace(",","")

        #print result
        Print(notional_text,start_date_text,end_date_text)

        return None
```
### def main() 

```python
    def main() :
        data = '''표기 불가'''

        Samsung_IR_SWP_Amortised(data)

        data = '''표기불가'''

        NH_Investment(data)
        return None

    if __name__ == "__main__" :
        main()

```
***
# 2. output

<img src="./IR_SWP output.png" width="50%" height="50%">    


***

# 3. Analysis and Future Work
1. 글로벌 변수 사용 최소화
글로벌 변수를 다수 사용하는 것은 유지보수에 불리합니다. 함수 호출 시 매개변수를 사용하고 필요한 데이터를 반환하는 방식으로 수정하는 것이 좋습니다.
글로벌 변수를 하나의 데이터 구조로 캡슐화하는 것도 방법입니다. 예를 들어, context 객체로 만들어 전달할 수 있습니다.
***

2. 함수 이름 및 변수명 개선
함수와 변수 이름은 Python의 명명 규칙인 스네이크 케이스를 따르는 것이 좋습니다.
***

3. 중복 코드 제거
Text_Switch 함수는 데이터를 리스트에서 문자열로 변환합니다. 그러나 동일한 기능을 ";".join(a_list)로 더 효율적으로 구현할 수 있습니다.
***

4. 입력 데이터 처리 개선
현재 NH_Investment 함수에서 데이터를 검증할 때 if each_data[0] == "2" 조건은 다소 불명확합니다.
조건을 명확히 하고 잘못된 데이터가 있을 경우 예외를 처리하도록 개선하세요.
***

5. 에러 처리
입력 데이터의 형식이 예상과 다를 경우 프로그램이 멈추지 않도록 try-except로 오류를 처리합니다.
***

6. 코드 구조 개선
중복된 초기화 코드를 제거하고 reset_globals 함수 또는 데이터 클래스를 사용하는 것이 좋습니다.
데이터 처리를 위한 별도 클래스를 만들면 더 간결하고 명확해집니다.
***
7. main 함수 개선
type 변수는 Python의 내장 함수 type()과 이름이 충돌하므로, input_type 등 다른 이름으로 바꾸세요.
잘못된 입력에 대해 명확히 처리합니다:

