from setup import Setup
from game import Game

setup = Setup()

Game(setup.get_display()).run_game_loop()

setup.quit()