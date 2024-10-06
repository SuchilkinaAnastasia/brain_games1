"""Модуль для вычисления наименьшего общего кратного (НОК)."""
import random
import math

def game_lcm():
    """Игра НОК"""
    numbers = random.sample(range(1, 20), 3)
    lcm_value = math.lcm(*numbers)
    question = " ".join(map(str, numbers))
    return question, lcm_value
