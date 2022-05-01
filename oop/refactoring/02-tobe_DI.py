# 1번 다른 Store가 들어오면 어떻게 될까?
# 개선점
# 1. Store을 추상화한다
# 2. 의존성 주입을 한다

from abc import ABC, abstractclassmethod

class Store(ABC):
    
    @abstractclassmethod
    def __init__(self):
        self.money = 0
        self.name = ""
        self.products = {}

    @abstractclassmethod
    def set_money(self, money):
        pass

    @abstractclassmethod
    def set_products(self, products):
        pass

    @abstractclassmethod
    def get_money(self):
        pass

    @abstractclassmethod
    def get_products(self):
        pass
    


class EricStore:
    def __init__(self):
        self.money = 0
        self.name = "에릭상점"
        self.products = {
            1: {"name": "키보드", "price": 30000},
            2: {"name": "모니터", "price": 50000},
        }

    def set_money(self, money):
        self.money = money

    def set_products(self, products):
        self.products = products

    def get_money(self):
        return self.money

    def get_products(self):
        return self.products

class FruitStore:
    def __init__(self):
        self.money = 0
        self.name = "과일상점"
        self.products = {
            1: {"name": "바나나", "price": 30000},
            2: {"name": "사과", "price": 50000},
        }

    def set_money(self, money):
        self.money = money

    def set_products(self, products):
        self.products = products

    def get_money(self):
        return self.money

    def get_products(self):
        return self.products



class User:
    def __init__(self, money, store: Store):
        self.money = money
        self.store = store    # 의존성 주입(구현체 대신에 인터페이스가 들어간다) -> 런타임에서 생성자 주입
        self.belongs = []

    def set_belongs(self, belongs):
        self.belongs = belongs

    def get_money(self):
        return self.money

    def get_belongs(self):
        return self.belongs

    def get_store(self):
        return self.store

    def see_product(self, product_id):
        product = self.store.show_product(product_id=product_id)
        return product

    def purchase_product(self, product_id):
        product = self.see_product(product_id=product_id)
        if self.money >= product["price"]:
            self.store.give_product(product_id=product_id)  # 상점에서 상품 꺼내기
            self.money -= product["price"]  # 사용자가 돈 내기
            self.store.take_money(product["price"])  # 상점에서 돈 받기
            self.belongs.append(product)
            return product
        else:
            raise Exception("잔돈이 부족합니다")

if __name__ == "__main__":
    store = EricStore(
        products = {
            1: {"name": "키보드", "price": 30000},
            2: {"name": "모니터", "price": 50000},
        }
    )