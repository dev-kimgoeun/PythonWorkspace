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

def language(name, age, lang1, lang2, lang3, lang4, lang5) :
    print("이름: {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)

language("찰리", 20, "파이썬", "자바","c","c++","c#")
language("루시", 25, "코틀린","스위프트","","","")









