from random import randint


name = "보병"
hp = 40
damage = 5

print("{} 유닛을 생성했습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{}유닛을 생성했습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

def attack (name, location, damage):
    print("{0} :{1} 방향 적군을 공격합니다. [공격력 {2}] ".format(name,location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{} 유닛을 생성했습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

class Unit :
    def __init__(self, name, hp, speed):
        self.name = name 
        self.hp = hp
        self.speed = speed
        print("{0} 유닛을 생성했습니다.".format(name))

    def move(self, location):
        # print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴됐습니다.".format(self.name))


# soldier1 = Unit("보병", 40, 5)
# soldier2 = Unit("보병", 40, 5)
# tank = Unit("탱크",150, 35)

# stealth1 = Unit("전투기", 80, 5)
# # print("유닛 이름: {0}, 공격력 : {1}".format(stealth1.name, stealth1.damage))

# stealth2 = Unit("업그레이드한 전투기", 80, 5)
# stealth2.cloacking = True

# if stealth2.cloacking == True:
#     print("{0}는 현재 은폐 상태입니다.".format(stealth2.name))

class AttackUnit(Unit): #unit클래스 상속
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
class Soldier(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "보병", 40, 5, 1)

    def booster(self):
        if self.hp>10:
            self.hp -=10
            print("{0} : 강화제를 사용합니다. (hp 10 감소)".format(self.name))
        else :
            print("{0} : 체력이 부족해 기술을 사용할 수 없습니다.".format(self.name))
        
class Tank(AttackUnit):
    siege_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 35, 1)
        self.siege_mode = False

    def set_siege_mode(self):
        if Tank.siege_developed == False:
            return 
        if self.siege_mode == False:
            print("{0} : 시지모드로 전환합니다. ".format(self.name))
            self.damage *= 2
            self.siege_mode = True
        else :
            print("{0} : 시지모드를 해제합니다.".format(self.name))
            self.damage //= 2
            self.set_siege_mode = False


# flamethrower1 =AttackUnit("화염방사병", 50, 16)
# flamethrower1.attack("5시")

# flamethrower1.damaged(25)
# flamethrower1.damaged(25)

class Flyable :
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self,name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        # print("[공중유닛이동]")
        self.fly(self.name, location)

class Stealth(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "전투기", 80,20,5)
        self.cloaked = False

    def cloaking(self):
        if self.cloaked == True:
            print("{0} : 은폐모드를 해제합니다.".format(self.name))
            self.cloaked = False
        else :
            print("{0} : 은폐모드를 설정합니다.".format(self.name))
            self.cloaked = True


intercepter = FlyableAttackUnit("요격기",200,6,5)
intercepter.fly(intercepter.name, "3시")

hoverbike = AttackUnit("호버 바이크", 80,20,10)
spacecruiser = FlyableAttackUnit("우주 순양함", 500, 25, 3)

hoverbike.move("11시")
# spacecruiser.fly(spacecruiser.name, "9시")
spacecruiser.move("9시")

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0)
        self.location = location 

supply_deport = BuildingUnit("보급고", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : Good Game")
    print("[Player] 님이 게임에서 퇴장했습니다.")

game_start()

so1= Soldier()
so2= Soldier()
so3= Soldier()

ta1 = Tank()
ta2 = Tank()

st1 = Stealth()

#유닛관리
attack_units= []
attack_units.append(so1)
attack_units.append(so2)
attack_units.append(so3)
attack_units.append(ta1)
attack_units.append(ta2)
attack_units.append(st1)

#전군이동
for unit in attack_units:
    unit.move("1시")

Tank.siege_developed = True
print("[알림] 탱크의 시지 모드 개발이 완료됐습니다.")

#공격 모드 준비 ( 보병 : 강화제, 탱크 : 시지모드, 전투기 : 은폐모드)
for unit in attack_units:
    if isinstance(unit, Soldier):
        unit.booster()
    elif isinstance(unit, Tank):
        unit.set_siege_mode()
    elif isinstance(unit, Stealth):
        unit.cloaking()

#전군 공격
for unit in attack_units:
    unit.attack("1시")

#전군 피해
for unit in attack_units:
    unit.damaged(randint(5,20)) #피해는 무작위로
    
game_over()          