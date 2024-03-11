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
    def __init__(self, name, hp, damage):
        self.name = name 
        self.hp = hp
        self.damage = damage
        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

soldier1 = Unit("보병", 40, 5)
soldier2 = Unit("보병", 40, 5)
tank = Unit("탱크",150, 35)

stealth1 = Unit("전투기", 80, 5)
print("유닛 이름: {0}, 공격력 : {1}".format(stealth1.name, stealth1.damage))

stealth2 = Unit("업그레이드한 전투기", 80, 5)
stealth2.cloacking = True

if stealth2.cloacking == True:
    print("{0}는 현재 은폐 상태입니다.".format(stealth2.name))

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴됐습니다.".format(self.name))

flamethrower1 =AttackUnit("화염방사병", 50, 16)
flamethrower1.attack("5시")

flamethrower1.damaged(25)
flamethrower1.damaged(25)
