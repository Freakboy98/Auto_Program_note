
start_date_text = ""
end_date_text = ""
notional_text = ""
start_date_list = []
end_date_list = []
notional_list = []

csv = '''
 2024-12-14 2025-03-14 904.0 0 36,532,346.08 2025-03-14-365,323.46 INT 105EUR
 0 0 2025-03-14-864,379.96XNL 105EUR
 2025-03-14 2025-06-14 904.0 0 35,667,966.12 2025-06-16-356,679.66 INT 199EUR
 0 0 2025-06-16-873,023.76XNL 199EUR
 2025-06-14 2025-09-14 904.0 0 34,794,942.36 2025-09-15-347,949.42 INT 290EUR
 0 0 2025-09-15-881,754.00XNL 290EUR
 2025-09-14 2025-12-14 904.0 0 33,913,188.36 2025-12-15-339,131.88 INT 381EUR
 0 0 2025-12-15-890,571.54XNL 381EUR
 2025-12-14 2026-03-14 904.0 0 33,022,616.82 2026-03-16-330,226.16 INT 472EUR
 0 0 2026-03-16-899,477.26XNL 472EUR
 2026-03-14 2026-06-14 904.0 0 32,123,139.56 2026-06-15-321,231.39 INT 563EUR
 0 0 2026-06-15-908,472.03XNL 563EUR
 2026-06-14 2026-09-14 904.0 0 31,214,667.53 2026-09-14-312,146.67 INT 654EUR
 0 0 2026-09-14-917,556.75XNL 654EUR
 2026-09-14 2026-12-14 904.0 0 30,297,110.78 2026-12-14-302,971.11 INT 745EUR
 0 0 2026-12-14-926,732.31XNL 745EUR
 2026-12-14 2027-03-14 904.0 0 29,370,378.47 2027-03-15-293,703.78 INT 836EUR
 0 0 2027-03-15-935,999.64XNL 836EUR
 2027-03-14 2027-06-14 904.0 0 28,434,378.83 2027-06-14-284,343.78 INT 927EUR
 0 0 2027-06-14-945,359.64XNL 927EUR
 2027-06-14 2027-09-14 904.0 0 27,489,019.19 2027-09-17-274,890.19 INT 1022EUR
 0 0 2027-09-17-954,813.23XNL 1022EUR
 2027-09-14 2027-12-14 904.0 0 26,534,205.96 2027-12-14-265,342.06 INT 1110EUR
 0 0 2027-12-14-26,534,205.96XNL 1110EUR
'''
# 전처리 과정 추가하기


csv = csv.strip()
data = csv.split("\n") 
valid_data = []

for idx in range(len(data)) :
    # 길이가 40 under이면 해당row 제거
    if len(data[idx]) > 40 :
        data[idx] = data[idx].strip()
        valid_data.append(data[idx])
# valid_data 추출완료

for itr in valid_data :
    each_data = itr.split(" ")
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

print(start_date_text)
print(end_date_text)
print(notional_text)
