"""Этот модуль содержит основной вызов функций программы."""

import os
import sys

# Импорты локальных модулей
from src.cli import welcome_user
from games.game_engine import run_game
from games.lcm_game import game_lcm
from games.progression_game import game_progression

# Добавляем директорию lab1 в пути поиска модулей
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def main():
    """Главная логика для выбора и запуска игры"""
    name = welcome_user()

    while True:
        print("\nChoose a game:")
        print("1 - Find the smallest common multiple")
        print("2 - What number is missing in the progression?")
        choice = input("Enter your choice: ")

        if choice == "1":
            run_game(game_lcm, name)
        elif choice == "2":
            run_game(game_progression, name)
        else:
            print("Invalid choice. Please try again.")
            continue

if __name__ == "__main__":
    main()
