# Простой калькулятор
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    print("Добро пожаловать в простой калькулятор!")
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    
    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")