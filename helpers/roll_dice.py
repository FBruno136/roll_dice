import random

def roll_dice(dice_type):
    """
    Rola um dado baseado no tipo informado (d4, d6, etc.).
    Retorna o resultado da rolagem.
    """
    try:
        sides = int(dice_type[1:])  # Extrai o número de lados (ex.: 'd6' -> 6)
        return random.randint(1, sides)
    except (ValueError, IndexError):
        return "Erro: Tipo de dado inválido"
