def get_fibonacci_list_to_index(index: int) -> list[int]:
    """
    Возвращает список первых index + 1 чисел Фибоначчи
    """
    first_num = 1
    second_num = 1
    array = [1]
    count = 1
    while count < index:
        array.append(second_num)
        first_num, second_num = second_num, first_num + second_num
        count += 1
    array.append(second_num)
    return array


def fib_to_decimal(num: str) -> int | str:
    """
    Функция переводит число из СС-Фиб в СС-10
    """
    try:
        if "11" in num:
            return "Неправильный формат числа (содержится 11, что невозможно)"
        decimal_num = 0
        len_num = len(num)
        fib_nums = get_fibonacci_list_to_index(len_num)
        for i in range(len_num):
            if num[i] == "1":
                decimal_num += fib_nums[len_num - i]
        return decimal_num
    except TypeError:
        return "Пожалуйста, соблюдайте типизацию"


if __name__ == '__main__':
    print(fib_to_decimal("10010100001"))    # 144 + 34 + 13 + 1 = 192
    print(fib_to_decimal("10101010101"))    # 144 + 55 + 21 + 8 + 3 + 1 = 232
    print(fib_to_decimal("1001010001"))     # 89 + 21 + 8 + 1 = 119
    print(fib_to_decimal("100100"))         # 13 + 3 = 16
    print(fib_to_decimal("1000101010010"))  # 377 + 55 + 21 + 8 + 2 = 463
    print(fib_to_decimal("1101010001010"))  # error
    print(fib_to_decimal(1010000101))       # ошибка типизации
