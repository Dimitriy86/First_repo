fh = open('test.txt', 'w')
try:
    # Виконання операцій з файлом
    fh.write('Some data')
finally:
    # Закриття файлу в блоці finally гарантує, що файл заакривається навідь у разі помилки
    fh.close()