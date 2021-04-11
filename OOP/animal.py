class Animal:
    def __init__(self):
        type = "none"
        name = "none"
        age = 0
        weight = 0
        isFly = false
        isWalk = false
        isSwim = false

    def display(self):
        print(f"Тип: {type} Имя: {name}, Возраст: {age}, Вес: <Вес животного>, Умеет летать: <Да/Нет>, Умеет ходить: <Да/Нет>, Умеет плавать: <Да/Нет>.")

