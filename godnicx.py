with open('python') as f:
    count = f.read().count('а')

if count:
    print(f'Количество элементов в файле: {count}')
else:
    print('Элементов в файле нет')