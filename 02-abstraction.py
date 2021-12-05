siri_name = 'siri'

siri_code = 123456789

def siri_say_hi():
    print("say Hello!! my name is siri")

def siri_add_cal():
    return 2 + 3

def siri_die():
    print()


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
print(Robot.population)
javais = Robot("jabis", 456)
print(Robot.population)
bixby = Robot("bixby", 789)
print(Robot.population)

print(siri.name)
siri.say_hi()   #시리 안에 있는 공간에 접근하는 메서드

Robot.how_many()
