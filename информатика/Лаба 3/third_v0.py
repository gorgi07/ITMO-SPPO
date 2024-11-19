# --------------------------------- №3 (Вариант 0) ---------------------------------
# Написать регулярное выражение, которое проверяет корректность email и в качестве
# ответа выдаёт почтовый сервер (почтовый сервер – часть email идущая после «@»).
# Для простоты будем считать, что почтовый адрес может содержать в себе буквы,
# цифры, «.» и «_», а почтовый сервер только буквы и «.». При этом почтовый сервер,
# обязательно должен содержать верхний уровень домена («.ru», «.com», etc.)
# ----------------------------------------------------------------------------------

import re


def check_email(email: str) -> str:
    try:
        if re.match(r"[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]", email):
            return re.split(r"@", email)[-1]
        return "Не email!"
    except TypeError:
        return "Ошибка! Функция принимает только данные типы str"
    except Exception:
        return "Неизвестная ошибка! Попробуйте заново"


def testing() -> None:
    tests = {"example@example": "Не email!",
             "example@example.com": "example.com",
             "students.spam@yandex.ru": "yandex.ru",
             "Erohin_Egor.2007@gmail.com": "gmail.com",
             "Albertik228-Krytoi@itmo.ru": "Не email!",
             "Vasilev@Anton@Gavidovich@yandex.ru": "Не email!",
             "gorgi07@yandex.ru": "yandex.ru"}

    print("=" * 22 + " №3v0 " + "=" * 22)
    for test in tests:
        print(f"Тест: {test}\nРезультат программы: {check_email(test)}\nПравильный ответ: {tests[test]}")
        print("-" * 50)


if __name__ == '__main__':
    testing()


