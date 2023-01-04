

print("국어, 수학, 영어 성적이 입력")
std_input_kor=int(input("kor >>>"))
std_input_math=int(input("math >>>"))
std_input_eng=int(input("eng >>>"))
total=std_input_kor+std_input_math+std_input_eng
avg=total//3

if 0 < std_input_kor <= 100 and  0 < std_input_math <= 100 and 0 < std_input_eng <= 100:
    if avg >= 80:
        print("불합격")
    else:
        print("합격")
else:
    print("잘못입력하였습니다.")

# 방법 2
if std_input_kor < 0 or std_input_kor > 100 or std_input_math < 0 or std_input_math > 100 or std_input_eng < 0 or std_input_eng > 100:
    if avg >= 80:
        print("불합격")

