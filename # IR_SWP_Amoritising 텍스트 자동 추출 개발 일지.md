*** 
# IR_SWP_Amoritising  텍스트 자동 추출 개발 일지 _date : 2024-12-04
***





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
'''

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

