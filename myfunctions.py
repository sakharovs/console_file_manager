def separator(simbol, count):
    """
    Функция создает разделитель из любых символов любого количества
    :param simbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """
    for i in range(count):
        print(simbol, end='')
        i += 1
    return print('\n')


if __name__ == '__main__':
    separator('#', 50)


def attention_msg(msg_text):
    separator('!', 50)
    print(f'{msg_text}\n')
    separator('!', 50)


def balance_msg(msg_text):
    separator('#', 20)
    print(msg_text, '\n')
    separator('#', 20)


def purchase_list(msg_text):
    separator('|', 30)
    print(msg_text)
    separator('|', 30)
