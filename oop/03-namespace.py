"""
#* namespace : 개체를 구분할 수 있는 범위
#* __dict__ : 네임스페이스를 확인할 수 있다.
#* dir() : 네임스페이스의 key 값을 확인할 수 있다.
#* __doc__ : class의 주석을 확인한다.
#* __class__ : 어떤 클래스로 만들어진 인스턴스인지 확인할 수 있다.
"""


class Robot:
    
    # 클래스 변수: 인스턴스들이 공유하는 변수 
    population = 0

    # 생성자 함수
    def __init__(self, name, code): #self는 각각의 인스턴스
        self.name = name    # 인스턴스 변수 
        self.code = code
        Robot.population += 1
    
    # 인스턴스 메서드
    def say_hi(self):   
        print(f"Grettings, my masters call me {self.name}.")
    
    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b
    
    # 인스턴스 메서드
    def die(self):
        print(f"{self.name} is being destoryed")

    @classmethod
    def how_many(cls):
        print(f"we have {cls.population} robots")


# siri, javais, bixby 
siri = Robot("siri", 123)
print(siri.__dict__)

siri.cal_add(2, 3)
print(siri.population)
print(siri.how_many())

Robot.say_hi(siri)
siri.say_hi()
print(dir(siri))