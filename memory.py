#создай приложение для запоминания информации
# подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton, QButtonGroup, QGroupBox
from random import randint, shuffle
# КЛАСС ДЛЯ ВОПРОСОВ
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question1 = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3







# ВАЖНЫЕ def'ы:
def show_question():
    RadioGroupBox.show() #СКРЫВАЕТ ФОРМУ ВОПРОСА
    AnsGroupBox.hide()    #ПОКАЗАТЬ ФОРМУ ОТВЕТА
    push_button.setText('Ответить') #ИЗМЕНИТЬ НАДПИСЬ 'Следующий вопрос' НА 'Ответить'
    RadioGroup.setExclusive(False) #СБРАШИВАЕТ ВСЕ ПЕРЕКЛЮЧАТЕЛИ
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_result():
    AnsGroupBox.show()    #СКРЫВАЕТ ФОРМУ ОТВЕТА
    RadioGroupBox.hide() #ПОКАЗЫВАЕТ ФОРМУ ВОПРОСА
    push_button.setText('Следующий вопрос') #ИЗМЕНИТЬ НАДПИСЬ 'Ответить' НА 'Следующий вопрос'

def start_test():
    if 'Ответить' == push_button.text():
        show_result()
    else:
        show_question()

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question1)
    right_questions.setText(q.right_answer)
    # ВЫЗОВ ФУНКЦИИ ПОКАЗАТЬ ВОПРОС:
    show_question()

def show_correct(res):
    right_or_not.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print(f'    Статистика\nВсего вопросов: {main_win.total}\nправильный ответов: {main_win.score}')
        print(f'Рейтинг: {main_win.score}/{main_win.total*100} %')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

def next_question():
    main_win.total += 1
    print(f'    Статистика\nВсего вопросов: {main_win.total}\nправильный ответов: {main_win.score}')
    curquestions = randint(0, len(questions_list)-1)
    '''main_win.cur_question = main_win.cur_question +1
    if main_win.cur_question >= len(questions_list):
        main_win.cur_question = 0'''
    q = questions_list[curquestions]
    ask(q)

def click_ok():
    if push_button.text() == 'Ответить':
        check_answer()
    else:
        next_question()
# СПИСОК ВОПРОСОВ
questions_list = []
q1 = Question('Как объявить список в Python?', '[1, 2, 3]', '(1, 2, 3)', '{1, 2, 3}', '"1, 2, 3"')  

q2 = Question('Какой оператор возводит в степень?', '**', '^', '//', '%%')  
q3 = Question('Как создать функцию в Python?', 'def my_func():', 'function my_func():', 'func my_func():', 'create my_func():')  
q4 = Question('Какой символ начинает комментарий?', '#', '//', '--', '/*')  
q5 = Question('Как проверить равенство a и b?', 'a == b', 'a = b', 'a equals b', 'a === b')  
q6 = Question('Как добавить элемент в конец списка?', 'list.append()', 'list.push()', 'list.insert()', 'list.add()')  
q7 = Question('Какой тип данных неизменяем?', 'str', 'list', 'dict', 'set')  
q8 = Question('Как открыть файл для чтения?', 'open("file.txt", "r")', 'open("file.txt", "read")', 'open("file.txt", "w")', 'open("file.txt", "write")')  
q9 = Question('Какой оператор выполняет целочисленное деление?', '//', '/', '%', '**')  
q10 = Question('Как импортировать модуль math?', 'import math', 'include math', 'require math', 'using math')  
q11 = Question('Type O ...?', 'Negative', 'Positive', '', 'qwerty')

questions_list.append(q1)
questions_list.append(q2)
questions_list.append(q3)
questions_list.append(q4)
questions_list.append(q5)
questions_list.append(q6)
questions_list.append(q7)
questions_list.append(q8)
questions_list.append(q9)
questions_list.append(q10)
questions_list.append(q11)


# создание приложения и главного окна
app = QApplication([])

# ... ваш исходный код выше ...

# Добавим стиль тёмной темы с фиолетовыми оттенками
dark_style = """
QWidget {
    background-color: #2e2e3e;
    color: #c0aaff;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 14px;
}

QGroupBox {
    border: 2px solid #6a4baf;
    border-radius: 8px;
    margin-top: 10px;
    font-weight: bold;
    color: #d3baff;
}

QGroupBox:title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding: 0 3px;
}

QLabel {
    color: #d3baff;
}

QPushButton {
    background-color: #6a4baf;
    border: 2px solid #8c6fff;
    border-radius: 10px;
    padding: 8px 16px;
    color: #f0eaff;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #8c6fff;
    border-color: #b299ff;
}

QPushButton:pressed {
    background-color: #4a2f8f;
    border-color: #6a4baf;
}

QRadioButton {
    spacing: 10px;
    color: #c0aaff;
}

QRadioButton::indicator {
    width: 20px;
    height: 20px;
    border-radius: 10px;
    border: 2px solid #6a4baf;
    background: #3a3a4a;
}

QRadioButton::indicator:checked {
    background-color: #8c6fff;
    border: 2px solid #b299ff;
}

QRadioButton::indicator:hover {
    border: 2px solid #b299ff;
}

QRadioButton::indicator:checked:hover {
    background-color: #a88fff;
    border-color: #d1baff;
}
"""

# Применяем стиль к приложению
app.setStyleSheet(dark_style)

# ... остальной ваш код ниже ...



app.setStyleSheet(dark_style)



main_win = QWidget()
main_win.setWindowTitle('Memory Card') #НАЗВАНИЕ ОКНА
main_win.resize(400,200) #РАЗМЕР ОКНА

# создание виджетов главного окна
question = QLabel()
answer1 = QRadioButton()
answer2 = QRadioButton()
answer3 = QRadioButton()
answer4 = QRadioButton()

answer1.setStyleSheet("""
    QRadioButton::indicator {
        width: 200px;
        height: 200px;
    }
""")
answer2.setStyleSheet("""
    QRadioButton::indicator {
        width: 200px;
        height: 200px;
    }
""")
answer3.setStyleSheet("""
    QRadioButton::indicator {
        width: 200px;
        height: 200px;
    }
""")
answer4.setStyleSheet("""
    QRadioButton::indicator {
        width: 200px;
        height: 200px;
    }
""")

answers = [answer1, answer2, answer3, answer4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(answer1)
RadioGroup.addButton(answer2)
RadioGroup.addButton(answer3)
RadioGroup.addButton(answer4)

push_button = QPushButton('Ответить')
push_button.setFixedSize(1500,300)

# ПРАВИЛЬНЫЙ ИЛИ НЕПРАВИЛЬНЫЙ ОТВЕТ
AnsGroupBox = QGroupBox('Варианты ответов:')
ans_layout = QVBoxLayout()
right_or_not = QLabel('Правильно/Непраавильно')
right_questions = QLabel('Правильный ответ')
ans_layout.addWidget(right_or_not, alignment = Qt.AlignLeft)
ans_layout.addWidget(right_questions, alignment = Qt.AlignRight)
AnsGroupBox.setLayout(ans_layout)
#   ВАЖНЫЕ ПЕРЕМЕННЫЕ:
main_win.score = 0
main_win.total = 0


# СОЗДАНИЕ ГРУППЫ ОТВЕТОВ
layoutH1_radio = QHBoxLayout()
layoutH2_radio = QHBoxLayout()

layoutH1_radio.addWidget(answer1)
layoutH1_radio.addWidget(answer2)
layoutH2_radio.addWidget(answer3)
layoutH2_radio.addWidget(answer4)

layout_main_radio = QVBoxLayout() #ГЛАВНАЯ ЛИНИЯ

layout_main_radio.addLayout(layoutH1_radio)
layout_main_radio.addLayout(layoutH2_radio)

RadioGroupBox = QGroupBox('Варианты ответов:') #ГРУППА ОТВЕТОВ
RadioGroupBox.setLayout(layout_main_radio)
# расположение виджетов по лэйаутам
#СОЗДАНИЕ ВСЕХ ЛИНИЙ И ДОБАВЛЕНИЕ ГОРИЗОНТАЛЬНЫХ ЛИНИЙ К ГЛАВНОЙ ЛИНИИ:
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layout_main = QVBoxLayout() #ГЛАВНАЯ ЛИНИЯ

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
#РАСПОЛОЖЕНИЕ ВИДЖЕТОВ(ВОПРОСА И ОТВЕТОВ) ПО ЛИНИЯМ:
layoutH1.addWidget(question, alignment = Qt.AlignCenter)

layoutH2.addWidget(RadioGroupBox)
layoutH2.addWidget(AnsGroupBox)
layoutH3.addWidget(push_button)
layout_main.setSpacing(50)
AnsGroupBox.hide()


# обработка нажатий на переключатели


#ask('b?','b1', 'b2', 'b3', 'b4')

main_win.cur_question=0
push_button.clicked.connect(click_ok)
# отображение окна приложения
main_win.setLayout(layout_main)
next_question()
main_win.show()
app.exec_()
#hjhkl;
