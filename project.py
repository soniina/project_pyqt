import sqlite3
import sys
import os

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog, QScrollArea
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel


class MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        self.image = QImage("back.jpeg")
        self.background = self.image.scaled(QSize(700, 600))
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Window, QBrush(self.background ))
        self.setPalette(self.palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 500, 30))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(211, 38, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.options = QtWidgets.QComboBox(self.centralwidget)
        self.options.setGeometry(QtCore.QRect(351, 43, 141, 19))
        self.options.setObjectName("options")
        self.options.addItems(['1', '2', '3', '4', '5'])
        self.options.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 60, 680, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(315, 80, 61, 31))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.task_number = QtWidgets.QLabel(self.frame)
        self.task_number.setGeometry(QtCore.QRect(20, 0, 45, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.task_number.setFont(font)
        self.task_number.setObjectName("task_number")
        self.scrolling = QScrollArea(self)
        self.scrolling.setWidgetResizable(True)
        self.task_pic = QtWidgets.QLabel(self.centralwidget)
        self.task_pic.setGeometry(QtCore.QRect(10, 110, 340, 161))
        self.task_pic.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.scrolling.setWidget(self.task_pic)
        self.scrolling.setGeometry(QtCore.QRect(10, 110, 340, 161))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.task_pic.setFont(font)
        self.task_pic.setText("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 385, 300, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(302, 319, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 300, 680, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 360, 300, 20))
        self.label_7.setObjectName("label_7")
        self.show_scale = QtWidgets.QPushButton(self.centralwidget)
        self.show_scale.setGeometry(QtCore.QRect(279, 407, 140, 30))
        self.show_scale.setObjectName("show_scale")
        self.show_scale.setStyleSheet("background-color: rgb(211, 211, 211);")
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('exam.db')
        db.open()
        self.scale_table = QtWidgets.QTableView(self.centralwidget)
        self.scale_table.setGeometry(QtCore.QRect(10, 445, 680, 100))
        self.scale_table.setObjectName("scale_table")
        model = QSqlTableModel(self, db)
        model.setTable('points')
        model.select()
        self.scale_table.setModel(model)
        self.grade = QtWidgets.QLabel(self.centralwidget)
        self.grade.setGeometry(QtCore.QRect(382, 320, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.grade.setFont(font)
        self.grade.setText("")
        self.grade.setObjectName("grade")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 340, 300, 20))
        self.label_9.setObjectName("label_9")
        self.right = QtWidgets.QLabel(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(183, 342, 100, 16))
        self.right.setText("")
        self.right.setObjectName("right")
        self.wrong = QtWidgets.QLabel(self.centralwidget)
        self.wrong.setGeometry(QtCore.QRect(200, 362, 100, 16))
        self.wrong.setText("")
        self.wrong.setObjectName("wrong")
        self.total = QtWidgets.QLabel(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(140, 385, 310, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.total.setFont(font)
        self.total.setText("")
        self.total.setObjectName("total")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(375, 120, 106, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.your_answer = QtWidgets.QTextEdit(self.centralwidget)
        self.your_answer.setGeometry(QtCore.QRect(440, 122, 191, 31))
        self.your_answer.setObjectName("your_answer")
        self.your_answer.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.show_result = QtWidgets.QPushButton(self.centralwidget)
        self.show_result.setGeometry(QtCore.QRect(270, 276, 160, 29))
        self.show_result.setObjectName("show_result")
        self.show_result.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(9, 276, 80, 29))
        self.open.setObjectName("open")
        self.open.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(494, 250, 80, 30))
        self.next.setObjectName("next")
        self.next.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(351, 110, 20, 161))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.show_answer = QtWidgets.QPushButton(self.centralwidget)
        self.show_answer.setGeometry(QtCore.QRect(435, 160, 202, 25))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.show_answer.setFont(font)
        self.show_answer.setObjectName("show_answer")
        self.show_answer.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(370, 190, 151, 20))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(545, 220, 112, 21))
        self.label_15.setObjectName("label_15")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(435, 185, 202, 30))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.answer = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.answer.setFont(font)
        self.answer.setGeometry(QtCore.QRect(0, 5, 600, 30))
        self.answer.setText("")
        self.answer.setObjectName("answer")
        self.points = QtWidgets.QComboBox(self.centralwidget)
        self.points.setGeometry(QtCore.QRect(600, 220, 60, 22))
        self.points.setObjectName("points")
        self.points.addItems(['0', '1', '2'])
        self.points.setStyleSheet("background-color: rgb(211, 211, 211);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Exam"))
        self.label.setText(_translate("MainWindow", "Реши вариант ОГЭ и узнай свою оценку"))
        self.label_2.setText(_translate("MainWindow", "Выбери вариант:"))
        self.task_number.setText(_translate("MainWindow", "0/15"))
        self.label_5.setText(_translate("MainWindow", "Всего баллов:"))
        self.label_6.setText(_translate("MainWindow", "Оценка:"))
        self.label_7.setText(_translate("MainWindow", "Неправильных заданий:"))
        self.show_scale.setText(_translate("MainWindow", "Показать таблицу"))
        self.label_9.setText(_translate("MainWindow", "Правильных заданий:"))
        self.label_13.setText(_translate("MainWindow", "Ответ:"))
        self.show_result.setText(_translate("MainWindow", "Узнать результат"))
        self.open.setText(_translate("MainWindow", "Открыть"))
        self.next.setText(_translate("MainWindow", "Начать"))
        self.show_answer.setText(_translate("MainWindow", "Отправить ответ"))
        self.label_15.setText(_translate("MainWindow", "Баллы:"))


class Exam(QMainWindow, MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.open.hide()  # кнопка для открытия файлов
        self.scale_table.hide()  # изначально таблица скрыта
        self.points.hide()  # выбор баллов тоже
        self.label_15.hide()  # надпись 'Баллы' рядом с выпадающим списком (points)
        self.connection = sqlite3.connect("exam.db")
        self.show_answer.clicked.connect(self.show_answer_f)  # отправка ответа или показа критериев и решений
        self.next.clicked.connect(self.next_f)  # перелистывание на задание вперёд
        self.show_result.clicked.connect(self.show_result_f)  # показ результата
        self.show_scale.clicked.connect(self.show_scale_f)  # показ или скрытие таблицы
        self.options.activated[str].connect(self.start)  # выбор варианта
        self.points.activated[str].connect(self.select_points)  # выбор баллов самим пользователем (в заданиях 13,14,15)
        self.open.clicked.connect(self.open_f)  # открытие файлов
        self.num_show_scale = 0  # счётчик для показа или скрытия таблицы
        self.result = 0  # количество набранных баллов
        self.done = 0  # количество правильно выполненных заданий
        self.flag = False  # флаг для того, чтобы проверить получил ли пользователь результат
        self.option = 1  # номер варианта; если пользователь нажмёт кнопку 'Начать', не выбрав вариант, то автоматически
                         # вариант будет первым
        self.fname = None  # имя выбранного файла

    # выбор варианта, его запоминание в переменную и начало решения (открытие первого задания)
    def start(self, text):
        self.option = text
        try:
            with open('options/{}_option/1.txt'.format(self.option), 'r', encoding='utf-8') as f:
                self.task_pic.setText(f.read())
            self.task_number.setText('1/15')
        except FileNotFoundError:
            self.statusBar().showMessage('В директории нет файла с первым заданием')
        self.next.setText('Далее ->')

    # отправка ответа, сравнение его с правильным и начисление баллов (для заданий, которые оцениваются одним баллом),
    # изменение количества правильно решенных заданий
    def show_answer_f(self):
        text = self.task_number.text().split('/')  # список состоящий из номера текущего задания и '15'
        if 0 < int(text[0]) < 13:
            try:
                with open('options/{}_option/answers.txt'.format(self.option), 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    if self.your_answer.toPlainText().lower().strip() == lines[int(text[0]) - 1].lower().strip():
                        self.result += 1
                        self.done += 1
            except FileNotFoundError:
                self.statusBar().showMessage('В директории нет файла с ответами')
        elif int(text[0]) <= 0:
            self.answer.setText('Вы не выбрали вариант и задание не загрузилось')
        else:
            self.answer.setText('Пролистайте до самого конца')
        self.your_answer.setText("")

    # при нажатии клавиши A(англ. раскладка) или D происходит перелистывание на задание назад или вперед соответственно
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_D:
            self.next_f()
        if event.key() == Qt.Key_A:
            self.back_f()

    # перелистывание на задание вперёд, изменение экрана при решении заданий с автоматически проверяющимися ответами и
    # без
    def next_f(self):
        text = self.task_number.text().split('/')  # список состоящий из номера текущего задания и '15'
        if int(text[0]) < 15:
            self.next.setText('Далее ->')
            self.answer.setText("")
            self.task_pic.setText("")
            if (int(text[0]) + 1) <= 15:
                self.task_number.setText(str(int(text[0]) + 1) + '/15')
            if 12 <= int(text[0]) <= 15:
                self.show_answer.setText('Показать критерии и решение')
                self.points.show()
                self.label_15.show()
            if int(text[0]) == 13:
                self.points.addItems(['3'])
            else:
                self.points.removeItem(3)
            try:
                with open('options/{}_option/{}.txt'.format(self.option, int(text[0]) + 1), 'r', encoding='utf-8') as f:
                    self.task_pic.setText(f.read())
            except FileNotFoundError:
                self.statusBar().showMessage('В директории нет файла с {} заданием'.format(int(text[0]) + 1))
            if self.task_number.text().strip() == '4/15' or self.task_number.text().strip() == '8/15' or \
                    self.task_number.text().strip() == '9/15' or self.task_number.text().strip() == '11/15'\
                    or self.task_number.text().strip() == '12/15' or self.task_number.text().strip() == '13/15'\
                    or self.task_number.text().strip() == '14/15' or self.task_number.text().strip() == '15/15':
                self.open.show()
            else:
                self.open.hide()
            if int(text[0]) + 1 == 15:
                self.next.hide()
            else:
                self.next.show()

    # перелистывание на задание назад, изменение экрана при решении заданий с автоматически проверяющимися ответами и
    # без
    def back_f(self):
        self.answer.setText("")
        self.task_pic.setText("")
        text = self.task_number.text().split('/')  # список состоящий из номера текущего задания и '15'
        if (int(text[0]) - 1) >= 0:
            self.task_number.setText(str(int(text[0]) - 1) + '/15')
        if 0 < int(text[0]) <= 13:
            self.show_answer.setText('Отправить ответ')
            self.points.hide()
            self.label_15.hide()
        if int(text[0]) == 1:
            self.next.setText('Начать')
        if int(text[0]) != 15:
            try:
                with open('options/{}_option/{}.txt'.format(self.option, int(text[0]) + 1), 'r', encoding='utf-8') as f:
                    self.task_pic.setText(f.read())
            except FileNotFoundError:
                self.statusBar().showMessage('В директории нет файла c {} заданием'.format(int(text[0]) + 1))
        if self.task_number.text().strip() == '4/15' or self.task_number.text().strip() == '8/15' or\
                self.task_number.text().strip() == '9/15' or self.task_number.text().strip() == '11/15'\
                or self.task_number.text().strip() == '12/15':
            self.open.show()
        else:
            self.open.hide()
        if int(text[0]) + 1 == 15:
            self.next.hide()
        else:
            self.next.show()

    # начисление баллов для заданий, оценивающихся более чем в 1 балл самим пользователем
    def select_points(self, points):
        self.result += int(points)
        text = self.task_number.text().split('/')  # список состоящий из номера текущего задания и '15'
        if text[0] == '13' or text[0] == '15':
            if points == '2':
                self.done += 1
        if text[0] == '14':
            if points == '3':
                self.done += 1

    # вывод результата: оценки, количества правильно и неправильно решённых заданий, количества баллов
    def show_result_f(self):
        self.flag = True
        self.total.setText(str(self.result))
        self.right.setText(str(self.done))
        self.wrong.setText(str(15 - self.done))
        res = self.connection.cursor().execute("""SELECT Оценка FROM Informatics
        WHERE Баллы = ?""", (self.result,)).fetchall()
        for elem in res:
            self.grade.setText(str(elem[0]))

    # показать или скрыть таблицу Оценка -> Баллы
    def show_scale_f(self):
        self.num_show_scale += 1
        if self.num_show_scale % 2 != 0:
            self.scale_table.show()
            self.show_scale.setText('Спрятать таблицу')
        else:
            self.scale_table.hide()
            self.show_scale.setText('Показать таблицу')

    # закрытие программы, рассмотрение случая выхода без получения результата
    def closeEvent(self, event):
        if self.flag is False:
            close_message = QMessageBox()
            close_message.setText("Вы уверены, что хотите выйти, не получив результат?")
            button_yes = close_message.addButton("Да", QMessageBox.AcceptRole)
            button_cancel = close_message.addButton("Отменить", QMessageBox.RejectRole)
            close_message.exec()
            if close_message.clickedButton() == button_yes:
                self.connection.close()
                event.accept()
            else:
                event.ignore()

    # выбор и открытие файла
    def open_f(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать нужный файл', 'options/{}_option'.format(self.option),
                                                 'Картинка (*.png);;Архив (*.rar);;Документ Excel (*.xls)')[0]
        os.startfile(self.fname)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exam()
    ex.show()
    sys.exit(app.exec())
