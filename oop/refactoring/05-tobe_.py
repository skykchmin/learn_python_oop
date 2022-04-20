from abc import ABC, abstractclassmethod
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: int
    
class Store(ABC):
    
    @abstractclassmethod
    def __init__(self):
        self._money = 0
        self.name = ""
        self._products = {}

    @abstractclassmethod
    def show_product(self, product_id):
        pass

    @abstractclassmethod
    def sell_product(self, product_id, money):
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

    def sell_product(self, product_id, money):
        # Validation 코드는 최소화
        product = self.show_product(product_id=product_id)
        if not product:
            raise Exception("상품이 존재하지 않는다")

        self._take_money(money)
        try:
            _product = self._take_out_product(product_id=product_id)
            return _product
        except Exception as e:
            self._return_money(money)
            raise e
        

    def _take_out_product(self, product_id):
        return self._products.pop(product_id)

    def give_product(self, product_id):
        self._products.pop(product_id)   # products에 product_id를 key로 가지는 value를 지운다

    def _take_money(self, money):
        self._money += money

    def _return_money(self, money):
        self._money -= money

class User:
    def __init__(self, store: Store):
        self._money = 0
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
        price = product["price"]
        if self._check_money_enough(price=price):
            self._give_money(money=price)
            try:
                my_product = self.store.sell_product(product_id, money = price)
                self._add_belong(my_product)
                return my_product
            except Exception as e:
                self._take_money(money=price)
                print(f"구매 중 문제가 발생하였습니다 {str(e)}")
        else:
            raise Exception("잔돈이 부족합니다")

    def _give_money(self, money):
        self._money -= money

    def _take_money(self, money):
        self._money += money 

    def _add_belong(self, product):
        self.belongs.append(product) # List에 값을 추가

    def _check_money_enough(self, price):
        return self._money >= price

if __name__ == "__main__":
    store = EricStore(
        products={
            1: Product(name = "키보드", price = 30000),
            2: Product(name = "모니터", price = 50000)
        }
    )

    user = User(money=100000, store=store)
    user.purchase_product(product_id=1)
    print(f"user가 구매한 상품 : {user.get_belongs()}")