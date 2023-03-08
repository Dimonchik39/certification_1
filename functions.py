import csv, os, datetime
import io
from constants import ABILITIES
from typing import Optional

def menu_select():
    '''
    Функция выбора меню
    '''
    start_text = 'Выберите действие: '
    
    for i, item in list(enumerate(ABILITIES, start = 1)):
        print(i, item, end= '\n')
    choise = give_int(start_text, 1, 5)
    return choise

def is_file_exists(filename:str):
    '''
    Функция проверки наличия файла/ заполнения файла
    '''
    return os.path.exists(filename) and os.path.getsize(filename)

def sequence(filename: str = "my_notes.csv"):
    '''
    Функция порядкого номера(ID)
    '''
    if not is_file_exists(filename):
        open(filename, 'a')
        return 2
    with open(filename, encoding='utf-8') as note:
        note_reader = csv.reader(note, delimiter= ";")
        return sum(1 for row in note_reader) + 1
    
def input_info():
    '''
    Функция ввода текста пользователем/ заполнение времени, ID
    '''
    present_time = datetime.datetime.today()
    new_present_time = present_time - datetime.timedelta(1)
        
    my_id = sequence()
    my_heading = input('Введите заголовок: ')
    my_note = input('Введите заметку: ')
    my_data = new_present_time.strftime('%Y-%m-%d %H.%M.%S')

    input_text = {
        "___ID___": (my_id),
        "Заголовок": (my_heading),
        "_Заметка_": (my_note),
        "__Дата__": (my_data)
        }
    return input_text

def write_row():
    '''
    Функция создания файла/ записи в файл
    '''
    with open("my_notes.csv", mode="a", encoding='utf-8') as note:
        names = ["___ID___", "Заголовок", "_Заметка_", "__Дата__"]
        note_writer = csv.DictWriter(note, delimiter= ";", lineterminator ="\r", fieldnames=names)
        if not is_file_exists("my_notes.csv"):
            note_writer.writeheader()

        note_writer.writerow(input_info())
        

def read_row():
    '''
    Функция просмотра файла
    '''
    with open("my_notes.csv", encoding='utf-8') as note:
        note_reader = csv.reader(note, delimiter= ";")
        count = 0
        print()
        for row in note_reader:
            if count == 0:
                print(" ; ".join(row))
            else:
                print(f'{row[0]} - {row[1]} - {row[2]} - {row[3]}')
            count += 1

        print()
        print(f'Количество строк в файле: {count}')

def del_input():
    del_note = input('Введите ID заметки для удаления: ')
    return del_note

def delete_row(filename: str = "my_notes.csv"):
    '''
    Фунция удаления строки
    '''
    del_note = del_input()

    with open(filename):
        input = open(filename, 'r', newline='')
        output = open("time_notes.csv", 'w', newline='')
        writer = csv.writer(output)
    
        for row in csv.reader(input):
            id=str(row[0]).split(';')[0]
            if id != del_note:
                writer.writerow(row)
    
        input.close()
        output.close()
        os.remove(filename)
        os.rename("time_notes.csv", "my_notes.csv")

def give_int(input_number:  str,
            min_num: Optional[int] = None,
            max_num: Optional[int] = None) -> int:
    '''
    Функция ввода числа
    '''
    while True:
        try:
            num = int(input(input_number)) 
            if min_num and num < min_num:
                print(f'Введите число больше или равно: {min_num}')
                continue  
            if max_num and num > max_num:
                print(f'Введите число меньше или равно: {max_num}')
                continue 
            return num
        except ValueError:
            print('Вы ввели не число. Введите число.')

def info():
    text = 'Функция не доступна! Совет: удалите заметку и добавьте новую.'
    print()
    print(text)
    print()

# def edit_input():
#     edit_note = input('Введите Заголовок заметки для редактирования: ')
#     return edit_note

# def edit_row(filename: str = "my_notes.csv"):
#     edit_note = edit_input()
#     a = write_row()
#     with io.open(filename):
#         input = open(filename, 'r', newline='')
#         output = open("time_notes.csv", 'a', newline='')
#         note_writer = csv.DictWriter(output, delimiter= ";", lineterminator ="\r", fieldnames=None)
    
#         for row in csv.DictReader(input):
#             data = dict(csv.reader(input))
#             if (data['Заголовок']) != edit_note :
#                 note_writer.writerow(row)
#             if (data['Заголовок']) == edit_note :   
#                 note_writer.writerow(a)
    
#         input.close()
#         output.close()
#         os.remove(filename)
#         os.rename("time_notes.csv", "my_notes.csv")
