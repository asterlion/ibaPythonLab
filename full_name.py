def full_name(last, first, middle):
    # соединяем ФИО
    full = last + ' ' + first + ' ' + middle
    # возвращаем ФИО с большими буквами
    return full.title()
