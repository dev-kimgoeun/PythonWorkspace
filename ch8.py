import sys
import pickle

# answer = input("아무 값이나 입력하세요.")
# print("입력한 값은 " + answer + "입니다.")
# print( type(answer))

print("파이썬", "자바")
print("파이썬", "자바", "자바 스크립트", sep=" vs ")

print("파이썬", "자바", sep=", ", end="? ")
print("무엇이 더 재미있을까요?")

print("파이썬", "자바", file=sys.stdout) #일반적인 내용의 오류 남김
print("파이썬", "자바", file=sys.stderr) #오류가 발생했을때 관련 내용 출력

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

for num in range(1,21):
    print("대기번호: " + str(num).zfill(3))

print("{0}".format(500))
print("{0: >10}".format(500)) #빈칸으로 두기, 오른쪽정렬 10칸 

print("{0: >+10}".format(500))
print("{0: >+10}".format(-500)) #빈칸으로 두기, 오른쪽정렬 기호 붙이기 

print("{0:_<10}".format(500)) #빈칸을 _로, 왼쪽정렬

print("{0:,}".format(10000000000)) #3자리마다 쉼표찍기
print("{0:+,}".format(10000000000000))
print("{0:+,}".format(-10000000000000))

print("{0}".format(5/3))

print("{0:f}".format(5/3))

print("{0:.2f}".format(5/3)) 

score_file = open("score.txt","w",encoding="utf8")
print("수학: 0", file=score_file)
print("영어: 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") #a 이어쓰기
score_file.write("과학: 80\n")
score_file.write("코딩: 100\n")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline() #1문장씩 읽어옴
    if not line:  #더이상 읽어올 내용이 없을때 반복문 탈출
        break
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #파일에서 모든 줄을 읽어 와 리스트 형태로 저장
for line in lines: #lines에 내용이 있을 때까지 
    print(line, end="")
score_file.close()



profile_file = open("profile.pickle","wb") #바이너리 형태로 저장
profile = {"이름":"스누피", "나이":30, "취미":["축구","골프","코딩"]}
print(profile)                  
pickle.dump(profile, profile_file) #profile데이터를 파일에 저장
profile_file.close() #파일닫기


profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file)

print(profile)
profile_file.close()

with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt","r", encoding="utf8") as study_file:
    print(study_file.read())