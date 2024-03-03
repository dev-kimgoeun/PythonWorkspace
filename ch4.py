sentence1 = '나는 소년입니다.'
print(sentence1, type(sentence1))

sentence2 = "파이썬은 쉬워요"
print(sentence2, type(sentence2))

sentence3 = """
나는 소년이고, 
파이썬은 쉬워요.
"""

print(sentence3)

print("파인" + "애플")

jumin = "990229-1234567"
print("성별 식별 번호 : " + jumin[7])

print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])
print("주민번호 뒷자리 :" +jumin[7:])
print("주민번호 뒷자리 :" +jumin[-7:])

msg = "나도코딩"
print(msg[1])

python = "Python is Amazing"

print(python.lower()) #전체 소문자로 변환
print(python.upper()) #전체 대문자로 변환
print(python[0].isupper()) #인덱스 0에 있는 값이 대문자인지 확인
print(python[1:3].islower()) #인덱스 1부터 2에 있는 값이 소문자인지 확인
print(python.replace("Python", "Java")) #Python을 Java로 변경

find = python.find("n") #처음 발견한 n의 인덱스

print(find) # python에서 인덱스5
find = python.find("n", find+1) #인덱스 6 이후부터 찾아 처음 발견한 n의 인덱스
print(find) #is amazing에서 인덱스 15
print(find)


index = python.index("n")
print(index)
index = python.index("n", index+1)
print(index)
index = python.index("n", 2,6)
print(index)
# index = python.index("java")
# print(index) 오류

print(python.count("n")) #2
print(python.count("v")) #0

print(len(python))

print("ab" +"ab")
print("ab", "ab")

print("나는 %d살입니다. " %20)
print("나는 %s를 좋아합니다. " %"파이썬")
print("apple은 %c로 시작해요. " %"A")
print("나는 %s살 입니다." %20)
print("나는 %s색과 %s색을 좋아해요. " %("파란", "빨간"))

print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))

print("나는 {age}살 이며, {color}색을 좋아해요.".format(age=20, color="파란"))
print("나는 {age}살 이며, {color}색을 좋아해요.".format(color="파란", age=20))

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

print("카페에서 {1}, {0}을 주문했다.".format("케이크", "커피"))

apple = "사과"
banana = "바나나"
print(f"빨가면 apple 맛있으면 banana")

print("백문이 불여일견\n백견이 불여일타") #\n 줄바꿈

print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

print("Red Apple\rPine") #PineApple?

print("Red\tApple")

url = "http://naver.com"
my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")]
password = my_str[:3]+str(len(my_str)) + str(my_str.count("e")) + "!"

print("{0}의 비밀번호는 {1}입니다.".format(url, password))

proverb = "the early bird catches the worm."
print(proverb[0].upper() + proverb[1:].lower())
print(proverb.capitalize())