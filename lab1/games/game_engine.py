"""Модуль для управления логикой игры."""
MAX_ROUNDS = 3

def run_game(game, name):
    """Основной цикл для всех игр"""
    print(f"Hello, {name}! Let's start the game.")

    for _ in range(MAX_ROUNDS):
        question, correct_answer = game()
        print(f"Question: {question}")

        # Цикл для ввода ответа пользователя с проверкой на корректность
        while True:
            try:
                user_answer = int(input("Your answer: "))
                break  # Если ввод корректен, выходим из цикла
            except ValueError:
                print("Invalid choice. Please enter a number.")

        # Проверка правильности ответа
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong. The correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}.")
            return False  # Игра завершится при неправильном ответе

    print(f"Congratulations, {name}! You won the game.")
    return True
