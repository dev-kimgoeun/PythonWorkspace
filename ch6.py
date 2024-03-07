from random import *

# weather = "비"
# if weather == "비":
#     print("우산을 챙기세요.")

# weather = "맑음"

# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" :
#     print("우산을 챙기세요.")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요.")
# else : print("맑습니다.")

temp = int(input("오늘 기온은 어때요? "))

if 30 <= temp:
    print("너무 더워요. 외출을 자제하세요.")
elif 10<= temp and temp <30 :
    print("활동하기 좋은 날씨예요.")
elif 0 <= temp and temp < 10 :
    print("외투를 챙기세요.")
else :
    print("너무 추워요. 나가지 마세요.")

for waiting_no in range(1,6,2) : #1부터 6직전 까지 2씩 간격주기
    print("대기번호 : {0}".format(waiting_no))

orders = ["아이언맨", "토르", "스파이더맨"]
for customer in orders :
    print ("{0} 님, 커피가 준비되었습니다. 픽업대로 와주세요.".format(customer))

customer = "토르"
index = 5

while index >=1:
    print("{} 님, 커피가 준비됐습니다.".format(customer))
    index -= 1
    print("{}번 남았어요.".format(index))
    if index ==0:
        print("커피를 폐기 처분합니다.")

customer = "아이언맨"
index = 1

while True : 
    print("{0}님, 커피가 준비됐습니다. 호출 {1}회".format(customer, index))
    index +=1

customer = "토르"
person = None

while person != customer:
    print("{0} 님, 커피가 준비됐습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")

absent = [2,5]
no_book = [7]

for student in range(1, 11) :
    if student in absent :
        continue
    elif student in no_book:
        print ("오늘 수업은 여기까지, {0}번 학생은 교무실로 따라와요.".format(student))
        break    
    print("{0}번 학생, 책을 읽어 보세요.".format(student))


#ex 1 
cnt = 0
for i in range (1,51):
    time = randrange(5,51)
    if 5 <= time <= 15:
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
        cnt += 1
    else :
        print("[] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

        print("총 탑승객 수 : {0}명".format(cnt))


# ex selfcheck

price = 1000
goods = 3
total = 0

for i in range (1, goods +1):
    print ("2+1 상품입니다.")
    if i % 3 == 0:
     continue
    total += price

print("총 가격은 " + str(total) + "원입니다.")