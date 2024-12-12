# 2024년 6월 24일

## __main()__ method
```python
def main():
    save_time = str(datetime.datetime.now().date()).replace("-","")
    print( "거래 날짜를 입력하세요 : " , end = '' )
    n_date          =   input()
    mail_downpath   = r'C:\Users\user\Desktop\NHAR\Mail/'
    fx_read_path    =   r"C:\Users\user\Desktop\NHAR\Layout\신규 선물 데일리.xlsx"
    eq_read_path    =   r"C:\Users\user\Desktop\NHAR\Layout\신규 주식 데일리.xlsx"
    vl_read_path    =   r"C:\Users\user\Desktop\NHAR\Layout\Valuation Daily.xlsx"
    fx_return_path  =   r"C:\Users\user\Desktop\NHAR\Output\신규 선물 데일리{}.xlsx".format(str(save_time))
    eq_return_path  =   r"C:\Users\user\Desktop\NHAR\Output\신규 주식 데일리{}.xlsx".format(str(save_time))
    vl_return_path  =   r"C:\Users\user\Desktop\NHAR\Output\Valuation Daily{}.xlsx".format(str(save_time))
    
```
## 01. _comment_

1. import datetime을 사용하여 현재 시간에 대한 정보를 불러언 후, '-'로 구분된 문자열의 형식을 '-'대신 ''로 대체한다    
2. 거래 날짜를 input()으로 받아 온다.   
3. main_downpath를 통해 경로를 지정 한 후. 경로를 통해 각각의 파일에 접근한다.   
4. 접근한 파일에 대해 다음을 반환한다. 날짜의 형식을 첫 줄에 있는 형식으로 파일의 read 결과를 반환   

```python
    #OutLook 다운로드
    att_down("NHAR", mail_downpath,n_date)
    print("\n############Mail Load Complete#############\n\n")

    
    ##주식
    clear_sheet(eq_read_path,'신규주식','A3','AP10000',eq_return_path)
    clear_sheet(eq_return_path,'잔고주식','A3','CV10000',eq_return_path)
    clear_sheet(eq_return_path,'청산주식','A3','BB10000',eq_return_path)

        #해외
    copy_data(r'C:\Users\user\Desktop\NHAR\Mail\해외신규거래_주식_NHAR_{}.xlsx'.format(str(n_date)),'New_Equity',eq_return_path,'신규주식',write_start=3,location=1)
    copy_data(r'C:\Users\user\Desktop\NHAR\Mail\해외청산거래_주식_NHAR_{}.xlsx'.format(str(n_date)),'Unwind_Equity',eq_return_path,'청산주식',write_start=3,location=1)
    copy_data(r'C:\Users\user\Desktop\NHAR\Mail\해외잔고보고서_손익_NHAR_{}_해외.xlsx'.format(str(n_date)),'Position',eq_return_path,'잔고주식',write_start=3,location=1)
    print("\n############Equity Complete#############\n\n")
    #평가
    clear_sheet(vl_read_path,'잔고','A2','CV10000',vl_return_path)
        #해외
    copy_data(r'C:\Users\user\Desktop\NHAR\Mail\해외잔고보고서_손익_NHAR_{}_해외.xlsx'.format(str(n_date)),'Position',vl_return_path,'잔고',2,1)
    pr
```
## 02. _comment_
att_down함수에 arguments로 "NHAR", main_downpath, n_date를 넣는다.   
att_down에 대해 살펴보자   

## __att_down()__ method
```python
#####Get Mail's attachment from outlook
def att_down(foldername, downpath,today): 
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI") 
    inbox = outlook.GetDefaultFolder(6).Folders['NHAR']
    messages = inbox.Items
    
    for ms in messages:
        print(ms.Subject)
        if ("NHAR_해외" in ms.Subject) and (str(ms.ReceivedTime)[0:10].replace("-","") > today):
            attachments = ms.Attachments 
            r = attachments.count
            print("해외 메일 첨부파일 개수 : ",str(r)+"개") 
            for i in range(1, r + 1): 
                attachment = attachments.Item(i) 
                attachment.SaveASFile(downpath +"해외"+str(attachment)) 
            pass
            
```
## _comment_
parameter로 폴더의 이름, 다운 경로, 오늘 날짜를 입력한다.   

outlook open API를 사용하여 정보를 불러오나.   

정보를 받아온 것 중에, 오늘 날짜보다 이후에 온 메일에 대해 연산 처리.   

## __scan_row()__ method

```python
######Scan Last row of mail#############
def scan_row(read_path,read_sheet):
    xl_path             =   xl.load_workbook(read_path)
    target_sheet        =   xl_path['{}'.format(read_sheet)]
    max_row             =   len(target_sheet['A'])
    return int(max_row)

```

## _comment_

parameter로 경로와 sheet을 입력 받는다.   

import xl로 xl 파일을 처리하도록 한다.    

입력 받은 경로에 대해  대상 sheet를 target으로 할당한 후,  "A" sheet에 있는 마지막 row의 수를 return 한다.    

## __clear()__ method
