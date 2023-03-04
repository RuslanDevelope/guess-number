from game import Game
from game import SettingsGame
import random
def main():
    game = Game()
    game.start()
    settings = SettingsGame()
    game.set_settings(settings)
    game.play()

if __name__ == "__main__":
    main()
