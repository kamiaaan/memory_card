
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import(QApplication, QRadioButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QPushButton, QButtonGroup)
from random import shuffle

class Question():
    def __init__(self, quest, right_answer, wrong1, wrong2, wrong3):
        self.quest = quest
        self.right_answer = right_answer
        self.wrong1  = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(400, 200)

question_list = []
q = Question('Сколько лет городу Бухара?', '2500', '1200', '2345', '1456')
q1 = Question('Когда закончилась Вторая Мировая война?', '1945', '1942', '1943', '1941')
q2 = Question('Самая дорогая машина?', 'Rolce Royce Ghost', 'Ferrari', 'Melaren', 'Matiz Best')
q3 = Question('Кто лучший футболист в мире?', 'Ronaldo', 'Messi', 'Makimi', 'Mbappe')

question_list.append(q)
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question = QLabel('Сколько лет Ташкенту?')

rbtn_1 = QRadioButton('2700')
rbtn_2 = QRadioButton('10000')
rbtn_3 = QRadioButton('1000')
rbtn_4 = QRadioButton('5200')

btn = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответов:')
h_line_group = QHBoxLayout()
v_line_group1 = QVBoxLayout()
v_line_group2 = QVBoxLayout()

v_line_group1.addWidget(rbtn_1)
v_line_group1.addWidget(rbtn_2)
v_line_group2.addWidget(rbtn_3)
v_line_group2.addWidget(rbtn_4)

h_line_group.addLayout(v_line_group1)
h_line_group.addLayout(v_line_group2)

RadioGroupBox.setLayout(h_line_group)

AnsGroupBox = QGroupBox('Правльный ответ:')
result = QLabel('Прав ты или нет?')
correct = QLabel('Ответ будет здесь!')
ans_v_line = QVBoxLayout()
ans_v_line.addWidget(result, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
ans_v_line.addWidget(correct, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(ans_v_line)

#Группа с кнопками
ButtonGroup = QButtonGroup()
ButtonGroup.addButton(rbtn_1)
ButtonGroup.addButton(rbtn_2)
ButtonGroup.addButton(rbtn_3)
ButtonGroup.addButton(rbtn_4)

h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()
main_v_line = QVBoxLayout()
