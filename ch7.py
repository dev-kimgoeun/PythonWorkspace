def open_account():
    print("새로운 계좌를 개설합니다.")

open_account()

def deposit(balance, money): #입금처리함수
    print("{0}원을 입금했습니다. 잔액은 {1}원 입니다.".format(money,balance+money))
    return balance + money #입금 후 잔액 변화

# def withdraw(balance, money): #출금처리함수
#     if balance >= money:
#         print("{0}원을 출금했습니다. 잔액은 {1}원입니다.".format(money, balance-money))
#         return balance-money
#     else :
#         print("잔액이 부족합니다. 잔액은 {0}원입니다.".format(balance))

def withdraw_night (balance, money):
    commission = 100
    print("업무 시간 외에 {}원을 출금했습니다.".format(money))
    return commission,balance -money- commission

balance = 0 #초기잔액
balance = deposit(balance, 1000)

#출금
# balance = withdraw(balance,2000)
# balance = withdraw(balance,500)

#업무 외 출금 시도
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))



def profile(name, age=20, main_lang="파이썬"): #일반 전달값과 기본값이 있는 전달값을 함께 사용할때는 반드시 일반 전달값 먼저
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}".format(name, age, main_lang))

profile("찰리")
profile("찰리",22)
profile("찰리",24, "자바")
profile("루시")

def language(name, age, *code) :
    print("이름: {0}\t나이 : {1}\t".format(name, age), end=" ")
    #print(language, type(language))
    for lang in code :
        print(code, end=" ")
        print()

language("찰리", 20, "파이썬", "자바","c","c++","c#", "자바스크립트")
language("루시", 25, "코틀린","스위프트","","","")


#함수안에 함수 호출

def add(item):
    print(item, "붓기")

def americano():
    add("뜨거운 물")
    add("에스프레소")

print("아메리카노 만드는 법")
americano()

#3d안경

glasses = 10

def rent(people):
    global glasses
    glasses = glasses - people
    print("[함수 내부] 남은 3D 안경 개수 : {0}".format(glasses))

print("전체 3D 안경 개수 : {0}".format(glasses))
rent(2)
print("남은 3D 안경 개수: {0}".format(glasses))

def rent_return(glasses, people) :
    glasses = glasses-people
    print("[함수 내부] 남은 3D 안경 개수: {0}".format(glasses))
    return glasses

print("전체 3D 안경 개수 : {0}".format(glasses))
glasses = rent_return(glasses, 2)
print("남은 3D 안경 개수 :{0}".format(glasses))

#표준체중 
def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else :
        return height * height * 21
    
height = 175
gender = "남자"

weight = round(std_weight(height/ 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))

#미세먼지

def get_air_quality (condition) :
    if (condition <= 30) :
        return "좋음"
    elif (condition <= 80):
        return "보통"
    elif(condition <= 150):
        return "나쁨"
    else :
        return "매우나쁨"
    
print(get_air_quality(15))
print(get_air_quality(85))
