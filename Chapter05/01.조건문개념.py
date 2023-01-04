# 조건문
# : 조건에 따라 실행할 명령이 달라 지는 것

orgin_pass = "1234"
input_pass = input("패스워드를 입력하세요 >>>")

if input_pass == orgin_pass:
    print("True")
elif input_pass == "":
    print("whatever you have to input any type")
else:
    print('False')