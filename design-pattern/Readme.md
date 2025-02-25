## 简单工厂模式 - Simple Factory Pattern

核心思想：通过一个工厂类，根据传入的参数决定创建哪种具体产品类的实例

优点：
- 集中管理对象的创建逻辑，降低耦合。
- 客户端无需知道具体类的名称，只需通过参数调用。

缺点：
- 新增产品需修改工厂类，违反开闭原则。

## 工厂方法模式 - Factory Method Pattern

核心思想：定义一个创建对象的接口，由子类决定实例化哪个类。每个具体工厂类负责创建一种具体产品。



抽象工厂模式 - Abstract Factory Pattern

建造者模式 - Builder Pattern

原型模式 - Prototype Pattern

单例模式 - Singleton Pattern

适配器模式 - Adapter Pattern

桥梁模式/桥接模式 - Bridge Pattern

组合模式 - Composite Pattern

装饰模式 - Decorator Pattern

门面模式/外观模式 - Facade Pattern

享元模式 - Flyweight Pattern

代理模式 - Proxy Pattern

责任链模式 - Chain of Responsibility Pattern

命令模式 - Command Pattern

解释器模式 - Interpreter Pattern

迭代器模式 - Iterator Pattern

中介者模式 - Mediator Pattern

备忘录模式 - Memento Pattern

观察者模式 - Observer Pattern

状态模式 - State Pattern

策略模式 - Strategy Pattern

模板方法模式 - Template Method Pattern

访问者模式 - Visitor Pattern