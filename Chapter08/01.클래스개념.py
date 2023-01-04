# 클래스를 사용하는 이유

champion1_name="이즈리얼"
champion1_health=700
champion1_attack = 90

print(f"{champion1_name}님 소환사의 협곡에 오신것을 환영합니다.")

champion2_name= "리신"
champion2_health= 800
champion2_attack = 95

print(f"{champion2_name}님 소환사의 협곡에 오신것을 환영합니다.")

def basic_attack(name, attack):
    print(f"{name} 기본공격 {attack}")

basic_attack("리신", 80)

print("==========클래스를 사용한 경우===========")