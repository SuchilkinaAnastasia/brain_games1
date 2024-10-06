"""Модуль для приветствия пользователя."""
def welcome_user():
    """Функция приветствия пользователя"""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name
