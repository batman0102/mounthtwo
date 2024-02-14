while True:
    class Calculator:
        def __add__(self, num1, num2):
            return num1 + num2

        def __sub__(self, num1, num2):
            return num1 - num2

        def __mul__(self, num1, num2):
            return num1 * num2

        def __truediv__(self, num1, num2):
            if num2 == 0:
                return "Ошибка. Нельзя делить на ноль!"
            return num1 / num2

        def calculate(self):
            num1 = float(input("Введите первое число: "))
            operation = input("Выберите действие: ")
            num2 = float(input("Введите второе число: "))

            if operation == '+':
                result = self.__add__(num1, num2)
            elif operation == '-':
                result = self.__sub__(num1, num2)
            elif operation == '*':
                result = self.__mul__(num1, num2)
            elif operation == '/':
                result = self.__truediv__(num1, num2)
            else:
                return "Ошибка 404"

            return f"Ответ: {result}"

    calculate = Calculator()
    result1 = calculate.calculate()
    print(result1)