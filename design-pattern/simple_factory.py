from abc import ABC, abstractmethod


# 商品接口
class Product(ABC):
    # 商品属性
    price: int

    @abstractmethod
    def get_info(self):
        """获取商品信息"""
        ...

    @abstractmethod
    def update_stock(self):
        """更新库存"""
        ...

    @abstractmethod
    def get_stock(self):
        """获取库存数量"""
        ...


# 具体商品
class Phone(Product):
    os: str
    cpu: str

    def get_info(self):
        return {"Price": self.price, "OS": self.os, "CPU": self.cpu}


class Watch(Product):
    size: str
    type: str

    def get_info(self):
        return {"Price": self.price, "Size": self.size, "Type": self.type}


# 简单工厂类
class ProductFactory:
    def create_product(self, product_type):
        if product_type == "phone":
            return Phone()
        elif product_type == "watch":
            return Watch()
        else:
            raise ValueError("Unknown product type")


if __name__ == "__main__":
    ...
