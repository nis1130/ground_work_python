# 생성자
# : 인스턴스를 만들 떄 호출되는 메서드

class Monster:
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed
    def decrease_health(self, num):
        self.health -= num
    def get_health(self):
        return self.health

# 고블린 인스턴스 생성
goblin = Monster(800, 120, 300)
goblin.decrease_health(100)
print(goblin.get_health())

# 늑대 인스턴스 생성
wolf = Monster(1500, 200, 500)
wolf.decrease_health(1000)
now_health = wolf.get_health()

if now_health < 0:
    print("다시 부활하는데 10초가 걸립니다.")
else:
    print(f"now_health : {now_health}")