
start_date_text = ""
end_date_text = ""
notional_text = ""

csv = '''
2024-12-14	2025-03-14	53775613429
2025-03-14	2025-06-14	52503246128
2025-06-14	2025-09-14	51218155153
2025-09-14	2025-12-14	49920213265
2025-12-14	2026-03-14	48609291959
2026-03-14	2026-06-14	47285261432
2026-06-14	2026-09-14	45947990604
2026-09-14	2026-12-14	44597347068
2026-12-14	2027-03-14	43233197107
2027-03-14	2027-06-14	41855405637
2027-06-14	2027-09-14	40463836247
2027-09-14	2027-12-14	39058351173
'''

csv = csv.strip()
data = csv.split("\n") 
start_date_list = []
end_date_list = []
notional_list = []

for each_line in data:
    each_data = each_line.split("\t")
    start_date_list.append(each_data[0])
    end_date_list.append(each_data[1])
    notional_list.append(each_data[2])
 

for each_date in start_date_list :
    start_date_text = start_date_text + each_date + ";"
start_date_text = start_date_text.replace("-","")
for each_date in end_date_list :
    end_date_text = end_date_text + each_date + ";"
end_date_text = end_date_text.replace("-","")
for each_proce in notional_list :
    notional_text = notional_text + each_proce + ";"
notional_text = notional_text.replace("-","")

print(start_date_text)
print(end_date_text)
print(notional_text)
