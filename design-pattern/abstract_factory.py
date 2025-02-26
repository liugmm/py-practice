"""
假设我们正在设计一个跨平台的UI工具包，该工具包需要在不同的操作系统（如Windows和macOS）上提供按钮（Button）和复选框（Checkbox）两种UI组件

1. 抽象产品:

* `AbstractButton`: 定义按钮的基本操作。

* `AbstractCheckbox`: 定义复选框的基本操作。

2. 具体产品:

* `WindowsButton`, `MacOSButton`: 分别实现Windows和macOS风格的按钮。

* `WindowsCheckbox`, `MacOSCheckbox`: 分别实现Windows和macOS风格的复选框。

3. 抽象工厂:

* `AbstractUIFactory`: 定义创建按钮和复选框的方法。

4. 具体工厂:

* `WindowsUIFactory`, `MacOSUIFactory`: 分别负责创建Windows和macOS风格的UI组件。

"""
# 抽象产品


class AbstractButton:
    def paint(self):
        pass


class AbstractCheckbox:
    def check(self):
        pass

# 具体产品


class WindowsButton(AbstractButton):
    def paint(self):
        return "Rendering a Windows style button."


class MacOSButton(AbstractButton):
    def paint(self):
        return "Rendering a macOS style button."


class WindowsCheckbox(AbstractCheckbox):
    def check(self):
        return "Checking a Windows style checkbox."


class MacOSCheckbox(AbstractCheckbox):
    def check(self):
        return "Checking a macOS style checkbox."

# 抽象工厂


class AbstractUIFactory:
    def create_button(self):
        pass

    def create_checkbox(self):
        pass

# 具体工厂


class WindowsUIFactory(AbstractUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacOSUIFactory(AbstractUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()

# 客户端代码（与之前相同）


def client_code(factory: AbstractUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.paint())
    print(checkbox.check())


if __name__ == "__main__":
    # 创建Windows UI组件
    print("Testing Windows UI components:")
    windows_factory = WindowsUIFactory()
    client_code(factory=windows_factory)

    # 创建macOS UI组件
    print("Testing macOS UI components:")
    macos_factory = MacOSUIFactory()
    client_code(factory=macos_factory)
