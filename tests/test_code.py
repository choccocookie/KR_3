import pytest
import datetime
import json
from src.utils import filter_executed, get_date, date, first_line, second_line


with_executed = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }]

without_executed = [
  {
    "id": 441945886,
    "state": "CANCELL",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }]

def test_with_executed():
    assert filter_executed(with_executed) == with_executed

def test_without_executed():
    assert filter_executed(without_executed) == []


date_test_1 = {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041'}
date_test_2 = {'id': 441945886, 'state': 'CANCELED', 'date': '2019-08-26T10:50:58.294041'}
def test_get_date():
    assert get_date(date_test_1) == '2019-08-26T10:50:58.294041'
    assert get_date(date_test_2) == '2019-08-26T10:50:58.294041'


for_test_date = {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'description': 'yes'}
def test_date():
    assert date(for_test_date) == ('26.08.2019', 'yes')



for_test_first_line_ = {"from": "Maestro 1596837868705199"}
for_test_first_line = {"from": "счет 64686473678894779589"}
def test_first_line():
    assert first_line(for_test_first_line_) == 'Maestro 1596 83** **** 5199 ->'
    assert first_line(for_test_first_line) == 'счет **9589 ->'

for_test_second_line_ = {"to": "Maestro 1596837868705199"}
for_test_second_line = {"to": "счет 64686473678894779589"}
def test_second_line():
    assert second_line(for_test_second_line_) == 'Maestro 1596 83** **** 5199'
    assert second_line(for_test_second_line) == 'счет **9589'