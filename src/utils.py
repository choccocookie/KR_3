import json
import datetime

def opening_from(filename):
    with open(filename) as f:
        raw_json = f.read()
    return json.loads(raw_json)


def filter_executed(operations):
    operations_executed = []
    for operate in operations:
        if operate.get('state') == 'EXECUTED':
            operations_executed.append(operate)
    return operations_executed



def get_date(dictionary):
   return dictionary['date']


def first_line(fresh_operations):
    for operate in fresh_operations:
        res = datetime.datetime.fromisoformat(operate["date"])
        res = res.strftime("%d.%m.%Y")
    return res, operate["description"]

def date(operate):
    res = datetime.datetime.fromisoformat(operate["date"])
    res = res.strftime("%d.%m.%Y")
    return res, operate["description"]

def first_line(operate):
    if "from" in operate:
        if operate["from"].lower().startswith('счет'):
            num = operate["from"].split(' ')
            hide_num = f"**{(num[-1])[-5:-1]} ->"
            num[-1] = hide_num
            #print((' ').join(num))
            return (' ').join(num)
        else:
            num = operate["from"].split(' ')
            hide_num = f"{(num[-1])[:5]} {(num[-1])[5:7]}** **** {(num[-1])[-5:-1]} ->"
            num[-1] = hide_num
            #print((' ').join(num))
            return (' ').join(num)


def second_line(operate):
    if operate["to"].lower().startswith('счет'):
        num = operate["to"].split(' ')
        hide_num = f"**{(num[-1])[-5:-1]}"
        num[-1] = hide_num
        #print((' ').join(num))
        return (' ').join(num)
    else:
        num = operate["to"].split(' ')
        hide_num = f"{(num[-1])[:5]} {(num[-1])[5:7]}** **** {(num[-1])[-5:-1]}"
        num[-1] = hide_num
        #print((' ').join(num))
        return (' ').join(num)


