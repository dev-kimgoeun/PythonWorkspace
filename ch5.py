from random import *

subway=["푸","피글렛","티거"]
print(subway)
print(subway.index("피글렛"))

subway.append("이요르")
print(subway)

subway.insert(1, "루")
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

subway.clear()
print(subway)

subway=["푸", "피글렛", "티거"]
subway.append("푸")
print(subway)
print(subway.count("푸"))

num_list=[5,2,4,3,1]

num_list.sort() #오름차순
print(num_list)

num_list.sort(reverse=True) #내림차순
print(num_list)

num_list.reverse() #순서뒤집기
print(num_list)

mix_list=["푸", 20, True, [5,2,4,3,1]]
print(mix_list)

mix_list = ["푸", 20, True]
num_list = [5,2,4,3,1]
num_list.extend(mix_list)
print(mix_list)
print(num_list)

cabinet = {3:"푸", 100:"피글렛"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))

print(cabinet.get(5, "사용 가능"))

print(3 in cabinet)
print(5 in cabinet)

cabinet = {"a-3":"푸", "b-100":"피글렛"}
print(cabinet["a-3"])
print(cabinet["b-100"])

print(cabinet)
cabinet["a-3"] ="티거"
cabinet["c-20"] = "이요르"
print(cabinet)

del cabinet["a-3"]
print(cabinet)

print(cabinet.keys())

print(cabinet.values())

print(cabinet.items())

cabinet.clear()
print(cabinet)

menu = ("돈가스", "치즈돈가스")
print(menu[0])
print(menu[1])

name="피글렛"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("피글렛", 20, "코딩")
print(name, age, hobby)

(departure, arrival) = ("김포", "제주")
print(departure, ">",arrival)
(departure, arrival) = (arrival, departure)
print(departure, ">", arrival)

my_set = {1,2,3,3,3}
print(my_set)

java = {"푸", "피글렛", "티거"}
python = set(["푸","이요르"])

print(java & python)
print(java.intersection(python))
print(java | python)
print(java.union(python))

print(java - python)
print(java.difference(python))

python.add("피글렛")
print(python)

java.remove("피글렛")
print(java)

menu = {"커피", "우유", "주스"}
print(menu)
print(type(menu))

menu = list(menu) #리스트로 변환
print(menu, type(menu))

menu = tuple(menu) #튜플로 변환
print(menu, type(menu))

menu=set(menu) #세트로 변환
print(menu, type(menu))

#exam1 당첨자 뽑기

lst = [1,2,3,4,5]
print(lst) 
shuffle(lst) #리스트 섞기
print(lst)
print(sample(lst, 1))

users = range(1,21)
users = list(users)
shuffle(users)

winners = sample(users, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당청자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")


#exam2 수강신청

subject = ["자료구조", "알고리즘", "자료구조", "운영체제"]
subject=set(subject) #리스트를 세트로 변환해 중복제거
subject = list(subject) #세트를 리스트로 변환
print("신청한 과목은 다음과 같습니다.")
print(subject)






#3월4일 생일 축하해 그리고 잘가 날 사랑해줘서 고마워
