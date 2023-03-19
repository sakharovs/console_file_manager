def separator(simbol, count):
    """
    Функция создает разделитель из любых символов любого количества
    :param simbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """
    print(f'{simbol * count}', end='\n')


if __name__ == '__main__':
    separator('T', 50)


def attention_msg(msg_text):
    separator('!', 50)
    print(msg_text)
    separator('!', 50)


def balance_msg(msg_text):
    separator('#', 20)
    print(msg_text)
    separator('#', 20)


def purchase_list(msg_text):
    separator('|', 30)
    print(msg_text)
    separator('|', 30)


def selection_block(sel_text):
    separator('#', 20)
    print(sel_text)
    separator('#', 20)
    return sel_text


if __name__ == '__main__':
    selection_block('Sometext')
