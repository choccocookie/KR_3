from utils import opening_from, filter_executed, get_date, date, first_line, second_line

operations = opening_from('operations.json')
operations_executed = filter_executed(operations)
operations_executed.sort(key=get_date, reverse=True)
fresh_operations = operations_executed[:5]
for operate in fresh_operations:
    print(f'{date(operate)} {operate["description"]}')
    print(first_line(operate), second_line(operate))
    print(f"{operate['operationAmount']['amount']} {operate['operationAmount']['currency']['name']} \n")