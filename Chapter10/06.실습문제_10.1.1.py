import csv

# data = [
#     ["종목","매입가","수량","목표가"],
#     ["삼성전자",85000,10,9000],
#     ["Naver",38000,5,400000]
# ]

# file = open("./myvenv/Chapter10/student.csv","w",newline="",encoding="utf-8-sig")
# writer = csv.writer(file)

# for d in data:
#     writer.writerow(d)
# file.close()

def show_profit(data):
    name = data[0]
    profit = (int(data[3])- int(data[1])) * int(data[2])
    profit_percent = (int(data[3]) / int(data[1])-1)* 100 
    print(f"{name},{profit},{profit_percent:.2f}%")

file = open("./myvenv/Chapter10/student.csv","r",encoding="utf-8-sig")
reader = list(csv.reader(file))

for data in reader[1:]:
    show_profit(data)
file.close()