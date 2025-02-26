
from abc import ABC, abstractmethod


# 抽象类产品
class Product(ABC):
    @abstractmethod
    def operation(self):
        ...

# 具体产品A


class ConcreteProductA(Product):
    def operation(self):
        return "Result of ConcreteProductA"

# 具体产品B


class ConcreteProductB(Product):
    def operation(self):
        return "Result of ConcreteProductB"


# 抽象工厂类
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        ...

    def some_operation(self):
        product = self.factory_method()
        result = product.operation()
        return result

# 具体工厂A


class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

# 具体工厂B


class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

# 客户端代码


def client_code(creator: Creator):
    print(f"Client: I'm not aware of the creator's class, but it still works.")
    print(creator.some_operation())


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreatorA.")
    client_code(ConcreteCreatorA())
    print("\n")

    print("App: Launched with the ConcreteCreatorB.")
    client_code(ConcreteCreatorB())
