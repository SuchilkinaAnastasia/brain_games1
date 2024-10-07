"""Этот модуль содержит основной вызов функций программы."""

# Импорты локальных модулей
from src.cli import welcome_user
from games.game_engine import run_game
from games.lcm_game import game_lcm
from games.progression_game import game_progression

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
