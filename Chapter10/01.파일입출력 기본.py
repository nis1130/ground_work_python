# file= open("./myvenv/Chapter10/data1.txt","w", encoding="utf8")
# file.write("1.스타트코딩과 함께 파이썬 공부")
# file.close()

file = open("./myvenv/Chapter10/data1.txt","a", encoding="utf8")
file.write("2.비전공자도 정말 쉽게 배울수 있습니다.")
file.close()

file = open("./myvenv/Chapter10/data1.txt","r",encoding="utf8")
# data = file.read()
# print(data)
# file.close()

while True:
    data = file.readline()
    print(data)
    if data  == "":
        break
file.close()


import pickle
file = open  