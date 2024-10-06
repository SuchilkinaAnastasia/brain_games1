"""Модуль для вычисления прогрессии."""
import random

def game_progression():
    """Игра 'Прогрессия': возвращает вопрос и правильный ответ"""
    length = random.randint(5, 10)
    first_term = random.randint(1, 10)
    ratio = random.randint(2, 5)
    progression = [first_term * (ratio ** i) for i in range(length)]
    missing_index = random.randint(0, length - 1)
    correct_answer = progression[missing_index]
    progression[missing_index] = ".."
    question = " ".join(map(str, progression))
    return question, correct_answer
