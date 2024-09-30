def divide1(first, second):
    try:
        res1 = first / second
        if second != 0:
            return res1
    except ZeroDivisionError:
        return "Ошибка"