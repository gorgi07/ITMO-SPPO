# ---------- №1 (Вариант 026) ----------
# Смайлик: 8-{O
# --------------------------------------

import re


def check_smile(smile: str) -> int | str:
    """
    Функция для нахождения количества смайликов соотвествующих формату: 8-{O
    """
    try:
        answer = len(re.findall(r"8-\{O", smile)) + len(re.findall(r"8-\{О", smile))
        return answer
    except TypeError:
        return "Ошибка! Функция принимает только данные типы str"
    except Exception:
        return "Неизвестная ошибка! Попробуйте заново"


def testing() -> None:
    tests = {"8-{O8-{O8-{O": 3, "8- {O{.8-\8-\{": 0, "8-{O8-{O8-{O8-{O..8-{O.8-\{О.": 5, ".8-{O/": 1, "8-{O-8-O8-{O": 2}
    print("=" * 18 + " №1 " + "=" * 18)
    print("Смайлик: 8-{O")
    print("-" * 40)
    for test in tests:
        print(f"Тест: {test}\nРезультат программы: {check_smile(test)}\nПравильный ответ: {tests[test]}")
        print("-" * 40)


if __name__ == '__main__':
    testing()
