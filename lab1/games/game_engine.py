"""Модуль для управления логикой игры."""
MAX_ROUNDS = 3

def greet_player(name):
    """Приветствие игрока."""
    print(f"Hello, {name}! Let's start the game.")

def get_user_answer():
    """Запрос и проверка корректности ответа пользователя."""
    while True:
        try:
            return int(input("Your answer: "))
        except ValueError:
            print("Invalid choice. Please enter a number.")

def check_answer(user_answer, correct_answer):
    """Проверка правильности ответа пользователя."""
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong. The correct answer was '{correct_answer}'.")
        return False

def run_game(game, name):
    """Основной цикл для всех игр."""
    greet_player(name)

    for _ in range(MAX_ROUNDS):
        question, correct_answer = game()
        print(f"Question: {question}")

        user_answer = get_user_answer()

        if not check_answer(user_answer, correct_answer):
            print(f"Let's try again, {name}.")
            return False  # Игра завершится при неправильном ответе

    print(f"Congratulations, {name}! You won the game.")
    return True
