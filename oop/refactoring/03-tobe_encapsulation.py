# 3번 User가 많은 행위를 책임지고 있다. Store가 판매하는 책임을 가져야한다

from abc import ABC, abstractclassmethod

class Store(ABC):
    
    @abstractclassmethod
    def __init__(self):
        self.money = 0
        self.name = ""
        self.products = {}

    @abstractclassmethod
    def show_product(self, product_id):
        pass

    @abstractclassmethod
    def give_product(self, product_id):
        pass

    @abstractclassmethod
    def take_money(self, money):
        pass

class EricStore:
    def __init__(self, products):
        self._money = 0
        self.name = "에릭상점"
        self._products = products

    def set_money(self, money):
        self._money = money

    def set_products(self, products):
        self._products = products

    def show_product(self, product_id):
        return self._products[product_id]

    def give_product(self, product_id):
        self._products.pop(product_id)   # products에 product_id를 key로 가지는 value를 지운다

    def take_money(self, money):
        self._money += money

class User:
    def __init__(self, store: Store):
        self.money = 0
        self.store = store    # 의존성 주입(구현체 대신에 인터페이스가 들어간다) -> 런타임에서 생성자 주입
        self.belongs = []

    def set_money(self, money):
        self.money = money

    def set_belongs(self, belongs):
        self.belongs = belongs

    def get_money(self):
        return self.money

    def get_belongs(self):
        return self.belongs

    def get_store(self):
        return self.store

    def see_product(self, product_id):
        products = self.store.get_products()
        return products[product_id]

    def purchase_product(self, product_id):
        product = self.see_product(product_id)
        if self.money >= product["price"]:
            self.store.products.pop(product_id)  # 상점에서 상품 꺼내기
            self.money -= product["price"]  # 사용자가 돈 내기
            self.store.money += product["price"]  # 상점에서 돈 받기
            self.belongs.append(product)
            return product
        else:
            raise Exception("잔돈이 부족합니다")

if __name__ == "__main__":
    user = User()
