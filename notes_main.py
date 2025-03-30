from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout
import json

# Заготовка для заметок (запишется в файл, если его нет)
notes = {
    'Инструкция': {
        'текст': 'Это умное приложение для заметок.',
        'теги': ['пример', 'инструкция']
    }
}

# Инициализация приложения
app = QApplication([])
window = QWidget()
window.setWindowTitle('Умные заметке')
window.resize(800, 600)

# Текстовое поле для заметки
field_for_notes = QTextEdit()

# Список заметок
name_of_notes = QListWidget()
list_notes_name = QLabel('Список заметоке')

# Кнопки для заметок
give_a_live_for_note = QPushButton('Создать заметке')
the_note_not_worthy_for_a_live = QPushButton('Удалить заметке')
show_mercy_for_note = QPushButton('Сохранить заметке')

# Список тегов
name_of_tags = QListWidget()
list_tags_name = QLabel('Список теге')
enter_prelast_worlds = QLineEdit('')
enter_prelast_worlds.setPlaceholderText('Введите теге')

# Кнопки для тегов
blessing_for_note = QPushButton('Добавить теге')
curse_for_note = QPushButton('Удалить теге')
find_the_way_with_tag = QPushButton('Искать по теге')

# Лейауты
main_layout = QHBoxLayout()

notes_layout = QVBoxLayout()
notes_layout.addWidget(field_for_notes)

notes_and_tags_layout = QVBoxLayout()
notes_and_tags_layout.addWidget(list_notes_name)
notes_and_tags_layout.addWidget(name_of_notes)

galfn_and_tnnwfal_layout = QHBoxLayout()
galfn_and_tnnwfal_layout.addWidget(give_a_live_for_note)
galfn_and_tnnwfal_layout.addWidget(the_note_not_worthy_for_a_live)

smfn_layout = QHBoxLayout()
smfn_layout.addWidget(show_mercy_for_note)

notes_and_tags_layout.addLayout(galfn_and_tnnwfal_layout)
notes_and_tags_layout.addLayout(smfn_layout)

notes_and_tags_layout.addWidget(list_tags_name)
notes_and_tags_layout.addWidget(name_of_tags)

epw_layout = QHBoxLayout()
epw_layout.addWidget(enter_prelast_worlds)

bfn_and_cfn_layout = QHBoxLayout()
bfn_and_cfn_layout.addWidget(blessing_for_note)
bfn_and_cfn_layout.addWidget(curse_for_note)

ftwwt_layout = QHBoxLayout()
ftwwt_layout.addWidget(find_the_way_with_tag)

notes_and_tags_layout.addLayout(epw_layout)
notes_and_tags_layout.addLayout(bfn_and_cfn_layout)
notes_and_tags_layout.addLayout(ftwwt_layout)

main_layout.addLayout(notes_layout)
main_layout.addLayout(notes_and_tags_layout)

# Функции
def show_note():
    if name_of_notes.selectedItems():
        key = name_of_notes.selectedItems()[0].text()
        field_for_notes.setText(notes[key]['тексте'])
        name_of_tags.clear()
        name_of_tags.addItems(notes[key]["теге"])
    else:
        field_for_notes.clear()
        name_of_tags.clear()

def add_note():
    note_name, ok = QInputDialog.getText(window, 'Создать заметку', 'Название заметки:')
    if ok and note_name != '':
        notes[note_name] = {'тексте': '', 'теге': []}
        name_of_notes.addItem(note_name)

def save_note():
    if name_of_notes.selectedItems():
        key = name_of_notes.selectedItems()[0].text()
        notes[key]['тексте'] = field_for_notes.toPlainText()
        with open('notes_data.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
    else:
        print('Заметка не выбрана')

def del_note():
    if name_of_notes.selectedItems():
        key = name_of_notes.selectedItems()[0].text()
        del notes[key]
        name_of_notes.takeItem(name_of_notes.currentRow())
        field_for_notes.clear()
        name_of_tags.clear()
        with open('notes_data.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
    else:
        print('Заметка не выбрана')

def add_tag():
    if name_of_notes.selectedItems():
        key = name_of_notes.selectedItems()[0].text()
        tag = enter_prelast_worlds.text()
        if not tag in notes[key]['теге']:
            notes[key]['теге'].append(tag)
            name_of_tags.addItem(tag)
            enter_prelast_worlds.clear()
        with open('notes_data.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)      
    else:
        print('Замтеке не выбрана')
def del_tag():
    if name_of_tags.selectedItems():
        key = name_of_notes.selectedItems()[0].text()
        tag = name_of_tags.selectedItems()[0].text()
        notes[key]['теге'].remove(tag)
        name_of_tags.clear()
        name_of_tags.addItems(notes[key]['теге'])
        with open('notes_data.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
    else:
        print('замтека не выбрана')
def search_tag():
    tag = enter_prelast_worlds.text()
    if find_the_way_with_tag.text()=='Искать по теге' and tag:
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]['теге']:
                notes_filtered[note]=notes[note]
        find_the_way_with_tag.setText('Поиске сбросить тексте')
        name_of_notes.clear()
        name_of_tags.clear()
        name_of_notes.addItems(notes_filtered)
    elif find_the_way_with_tag.text()=='Поиске сбросить тексте':
        name_of_notes.clear()
        name_of_tags.clear()
        enter_prelast_worlds.clear()
        name_of_notes.addItems(notes)
        find_the_way_with_tag.setText('Искать по теге')
    

# Подключение событий
give_a_live_for_note.clicked.connect(add_note)
blessing_for_note.clicked.connect(add_tag)
curse_for_note.clicked.connect(del_tag)
find_the_way_with_tag.clicked.connect(search_tag)
the_note_not_worthy_for_a_live.clicked.connect(del_note)
show_mercy_for_note.clicked.connect(save_note)
name_of_notes.itemClicked.connect(show_note)

# Загрузка данных из файла
try:
    with open('notes_data.json', 'r', encoding='utf-8') as file:
        notes = json.load(file)
except FileNotFoundError:
    with open('notes_data.json', 'w', encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)

name_of_notes.addItems(notes)

# Запуск приложения
window.setLayout(main_layout)
window.show()
app.exec_()
