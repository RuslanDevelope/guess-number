import random


class Computer:

    def __init__(self):
        self.__hidden_number: int

    def get_hidden_number(self, first_range: int, last_range: int):
        self.__hidden_number = random.randint(first_range, last_range)
        return self.__hidden_number


class Player:

    def input_number(self, first_range: int, last_range: int) -> int:
        messege = f"Введите число от {first_range} до {last_range-1}\n"
        while True:
            try:
                number = int(input(messege))
                return number
            except ValueError:
                print("Вы ввели не число повторите попытку")
