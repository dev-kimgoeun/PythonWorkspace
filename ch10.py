# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return "[오류 코드 001]" + self.msg #오류 메시지 가공

# try :
#     print("나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} /{1} = {1}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("오류 발생 : 잘못된 값을 입력했습니다.")
# except BigNumberError as err:
#     print("오류가 발생했습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally: #오류 발생 여부와 상관없이 항상 실행
#     print("계산기를 이용해 주셔서 감사합니다.")


# #실습 -> 치킨 주문
# class SoldOutError(Exception) :
#     pass 

# chicken = 10
# waiting = 1

# while True :
#     try:
#         print("[남은 치킨 :{0}]".format(chicken))
#         order = int(input("치킨을 몇 마리 주문하시겠습니까? "))
#         if order > chicken:
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         else :
#             print("[대기번호 {0}] {1}마리를 주문했습니다.".format(waiting, order))
#             waiting +=1
#             chicken -= order
#         if chicken == 0:
#             raise SoldOutError
#     except ValueError:
#         print("잘못된 값을 입력했습니다.")
#     except SoldOutError:
#         print("재료가 소진돼 더 이상 주문을 받지 않습니다.")
#         break

#셀프체크
    
def save_battery(level):
    try:
        print(f"배터리 잔량 : {level}%")
        if level > 30:
            print("일반 모드로 사용합니다.")
        elif level > 5:
            print("절전모드로 사용합니다.")
        else:
            raise Exception("배터리가 부족해 스마트폰을 종료합니다.") #오류발생
    except Exception as e:
        print(e)
        
    print()

save_battery(75)
save_battery(25)
save_battery(3)