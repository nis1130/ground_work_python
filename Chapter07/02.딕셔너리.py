stock_a = {"삼성전자" : 82000, "LG전자" : 150000}

stock_b = {
    "삼성전자" : [81000, 81500, 82000, 81500, 82000],
    "LG전자" : (150000, 149000, 148000, 151000, 152000)
}

stock_c = {
    "삼성전자" : {
        "현재가" : 82000,
        "보유수량" : 5,
        "매수단가" : 81500
    }
}

stock_d = {
    "삼성전자" : 75100,
    "쿠팡" : 31000,
    "AWS" : 110000
}

print("stock_a : ",stock_a)
print("stock_b : ",stock_b)
print("stock_c : ",stock_c)
print("stock_d : ",stock_d)

# 딕셔너리 접근하기
print(stock_a["삼성전자"])
print(stock_c["삼성전자"]["보유수량"])

# 딕셔너리 할당하기
stock_a["삼성전자"] = 85000
print(stock_a)

# 딕셔너리 삭제하기
del stock_b["LG전자"]
print(stock_b)

# 딕셔너리 함수
# items() : 키와 데이터 쌍
for item in stock_d.items():
    print(item)

print("---------------------------")
# keys() : 키
for item in stock_d.keys():
    print(item)
    
print("---------------------------")

# values() : 데이터
for item in stock_d.values():
    print(item)