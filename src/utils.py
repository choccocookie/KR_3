import json
import datetime

def opening_from(filename):
    """
    Функция импорта данных о банковских операциях из .json
    возвращает список словарей
    """
    with open(filename) as f:
        raw_json = f.read()
    return json.loads(raw_json)


def filter_executed(operations):
    """
    Получает список словарей с данными о банковских операциях,
    выбирает EXECUTED словари, добавляет их в новый список словарей и возвращает его
    """
    operations_executed = []
    for operate in operations:
        if operate.get('state') == 'EXECUTED':
            operations_executed.append(operate)
    return operations_executed



def get_date(dictionary):
    """
    Функция для сортировки словарей из списка по ключу 'date'
    возвращает значение по ключу
    """
    return dictionary['date']


def date(operate):
    """
    Получает словарь из списка при итерации
    переформатирует значение ключа 'date' в формат даты с использованием библиотеки datetime
    возвращает дату и значение ключа 'description'
    """
    res = datetime.datetime.fromisoformat(operate["date"])
    res = res.strftime("%d.%m.%Y")
    return res

def first_line(operate):
    """
    Получает словарь из списка при итерации
    в зависимости от начала строки по ключу 'from'
    -разбивает строку сплитом на список строк
    -форматирует строку с номером счета или карты срезами строки
    -возвращает и замещает форматированную строку обратно в список
    - преобразует список строк в строку через джоин
    """
    if "from" in operate:
        if operate["from"].lower().startswith('счет'):
            num = operate["from"].split(' ')
            hide_num = f"**{(num[-1])[-4:]} ->"
            num[-1] = hide_num
            return (' ').join(num)
        else:
            num = operate["from"].split(' ')
            hide_num = f"{(num[-1])[:4]} {(num[-1])[4:6]}** **** {(num[-1])[-4:]} ->"
            num[-1] = hide_num
            return (' ').join(num)
    else:
        return ''


def second_line(operate):
    """
    Получает словарь из списка при итерации
    в зависимости от начала строки по ключу 'to'
    -разбивает строку сплитом на список строк
    -форматирует строку с номером счета или карты срезами строки
    -возвращает и замещает форматированную строку обратно в список
    - преобразует список строк в строку через джоин
    """
    if operate["to"].lower().startswith('счет'):
        num = operate["to"].split(' ')
        hide_num = f"**{(num[-1])[-4:]}"
        num[-1] = hide_num
        return (' ').join(num)
    else:
        num = operate["to"].split(' ')
        hide_num = f"{(num[-1])[:4]} {(num[-1])[4:6]}** **** {(num[-1])[-4:]}"
        num[-1] = hide_num
        return (' ').join(num)


