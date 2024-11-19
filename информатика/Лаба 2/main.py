class NumberAlphabetError(Exception):
    pass


class MessageLengthError(Exception):
    pass


def verification(message: str) -> str | int:
    """
    Проверка входного сообщения на корректность
    """
    try:
        if set(message) != {"0", "1"}:
            raise NumberAlphabetError
        if len(message) != 7:
            raise MessageLengthError
        return 1
    except NumberAlphabetError:
        return "Неправильный формат сообщения (содержит символы отличные от цифр 0 и 1)"
    except MessageLengthError:
        return "Длина сообщения не равна 7"


def message_analysis(data: list[int]) -> str:
    names_index = ["r1", "r2", "i1", "r3", "i2", "i3", "i4"]
    s1 = str(data[0] ^ data[2] ^ data[4] ^ data[6])
    s2 = str(data[1] ^ data[2] ^ data[5] ^ data[6])
    s3 = str(data[3] ^ data[4] ^ data[5] ^ data[6])
    s = int(s3 + s2 + s1, 2)
    full_mes = f"\n{data[0]}{data[1]}{data[2]}{data[3]}{data[4]}{data[5]}{data[6]} - полное сообщение (с битами четности)"
    if s != 0:
        err = names_index[s - 1]
        correction = f"\nИсправлена ошибка в бите {'{'}{err}{'}'}"
        if "r" in err:
            mes = f"{data[2]}{data[4]}{data[5]}{data[6]} - сообщение (информационные биты)"
        else:
            if err == "i1":
                mes = f"{(data[2] + 1) % 2}{data[4]}{data[5]}{data[6]} - сообщение (информационные биты)"
            elif err == "i2":
                mes = f"{data[2]}{(data[4] + 1) % 2}{data[5]}{data[6]} - сообщение (информационные биты)"
            elif err == "i3":
                mes = f"{data[2]}{data[4]}{(data[5] + 1) % 2}{data[6]} - сообщение (информационные биты)"
            elif err == "i4":
                mes = f"{data[2]}{data[4]}{data[5]}{(data[6] + 1) % 2} - сообщение (информационные биты)"
        return mes + full_mes + correction
    else:
        mes = f"{data[2]}{data[4]}{data[5]}{data[6]} - сообщение (было получено без ошибок)"
        return mes + full_mes


def main(message: str) -> str:
    verdict = verification(message)
    if verdict == 1:
        array = list(map(int, message))
        return message_analysis(array)
    else:
        return verdict


if __name__ == '__main__':
    try:
        print("Программа для анализа сообщения на основе классического кода Хэмминга (7;4)")
        while True:
            inp = input("Введите сообщение длиной 7 символов (для завершения работы программы напишите Ex): ")
            if inp == "Ex":
                print("Пока-пока")
                break
            else:
                print(main(inp))
                print("-" * 94)
    except EOFError:
        print("Ручное завершение программы")
    except KeyboardInterrupt:
        print("\nРучное завершение программы")
    finally:
        print("Приходите ещё ^_^")
