list_example = [5, 'sdfs', [], {}, 'foo']

list_example.append(567)

print(list_example[1])

for elem in list_example:
    print(elem)

print([elem + 'bar' for elem in list_example if isinstance(elem, str)])

dict_example = {'bar': 56, 'dk': []}

print({elem: elem + 'val' for elem in list_example if isinstance(elem, str)})

set_example = {4, 7, 8, 5}

tuple_example = (5, 7, 4, 8)

for num in range(0, 10):
    print(num)

