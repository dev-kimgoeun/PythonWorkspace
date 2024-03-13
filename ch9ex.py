class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.hous_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    #매물정보표시    
    def show_detail(self):
        print(self.location, self.hous_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억원", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억원", "2007년")
house3 = House("송파", "빌라", "월세", "500/50만원", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}가지 매물이 있습니다. ".format(len(houses)))
for house in houses :
    house.show_detail()


#차량등록

class ParkingManager :
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        print(f"총 {capacity}대를 등록할 수 있습니다.")

    def register(self):
        if self.count >= self.capacity:
            print(" 더 이상 등록할 수 없습니다.")
            return
        self.count += 1
        print(f"차량 신규 등록 ({self.count}/{self.capacity})")
        
#테스트 코드
manager = ParkingManager(5)
for i in range(6):
    manager.register()