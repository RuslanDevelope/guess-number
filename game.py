from difficult import Difficult
from players import Computer , Player


class Game:

    def __init__(self):
        self.settings: SettingsGame = None
        self.__computer = Computer()
        self.player = Player()

    def start(self, welocom_messege: str = None):
        if welocom_messege:
            print(welocom_messege)
        else:
            print("Добро пожаловать в игру 'Угадай число'\n" \
                  "Вам доступны три уровня сложности\n" \
                  "\t1. Легкий - число загадывается от 1 до 10, количество попыток 3\n" \
                  "\t2. Средний - число загадывается от 1 до 50, количество попыток 10\n" \
                  "\t3. Сложный - число загадывается от 1 до 100, количество попыток 15\n")

    def play(self):
        hidden_number = self.__computer.get_hidden_number(
            self.settings.get_first_range(), self.settings.get_last_range())
        amount_attemps = self.settings.get_amount_attemps()
        i = 0
        while i < amount_attemps:
            input_number_player = self.player.input_number(self.settings.get_first_range(),self.settings.get_last_range())
            if hidden_number == input_number_player:
                print(f"Вы угадали, это число {hidden_number}, использовано попыток {i + 1}")
                return
            else:
                print(f"Нет, это не - {input_number_player}, осталось попыток - {amount_attemps - (i + 1)}")
            i += 1
        print("Вы проиграли. Количество попыток 0 ")

    def set_settings(self, settings):
        self.settings = settings


class SettingsGame:

    def __init__(self):
        self.__level_difficult: Difficult = None
        self.__first_range: int = 0
        self.__last_range: int = 0
        self.__amount_attemps: int = 0
        self.__get_settings_game()
        self.__set_settings_game()

    def get_first_range(self) -> int:
        return self.__first_range

    def get_last_range(self) -> int:
        return self.__last_range

    def get_amount_attemps(self) -> int:
        return self.__amount_attemps

    def __set_settings_game(self):
        match self.__level_difficult:
            case Difficult.EASY:
                self.__first_range = 1
                self.__last_range = 11
                self.__amount_attemps = 3
            case Difficult.MIDDLE:
                self.__first_range = 1
                self.__last_range = 51
                self.__amount_attemps = 10
            case Difficult.HARD:
                self.__first_range = 1
                self.__last_range = 101
                self.__amount_attemps = 15

    def __get_settings_game(self):
        input_number = 0
        while input_number < 1 or input_number > 3:
            try:
                input_number = int(input("Введите вариант сложности от 1 до 3 где\n"
                                         " 1 - легкий \n 2 - средний \n 3 - тяжелый\n"))
            except ValueError:
                print("Ввели не число")
        match input_number:
            case 1:
                self.__level_difficult = Difficult.EASY
            case 2:
                self.__level_difficult = Difficult.MIDDLE
            case 3:
                self.__level_difficult = Difficult.HARD
        return self

    def info(self):
        print(f"first_range = {self.__first_range} \n"
              f"last_range = {self.__last_range}\n"
              f"amount_attemps = {self.__amount_attemps}\n"
              f"level_difficult = {self.__level_difficult}\n")
