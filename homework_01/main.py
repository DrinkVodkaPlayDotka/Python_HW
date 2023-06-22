"""
Домашнее задание №1
Функции и структуры данных
"""


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def power_numbers(*args) -> [int]:
    return [arg ** 2 for arg in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(nums: [int], filter_type: str) -> [int]:
    if filter_type == ODD:
        return [num for num in nums if num % 2 != 0]
    elif filter_type == EVEN:
        return [num for num in nums if num % 2 == 0]
    elif filter_type == PRIME:
        return [num for num in nums if is_prime(num)]
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
