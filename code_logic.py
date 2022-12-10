import random
import sys
from main import *
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit
from PySide6.QtCore import Slot


class View(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sign = ["+", "-", "×", "÷"]
        self.practice = []

    @Slot()
    def resets(self):
        local = []
        self.rate.setText("")
        for index in range(1, 23):
            a, s, b = random.randint(1, 99), random.choice(self.sign), random.randint(1, 99)
            local.append((index, a, s, b, " = "))
        for index, practice_item in enumerate(local):
            line_text = self.widget_15.findChild(QLineEdit, "lineEdit" + str(index + 1))
            line_text.setText("")
            line_text.setStyleSheet("#" + "lineEdit" + str(index + 1) + "{border-radius:8px;}")

            if practice_item[2] == "+":
                result = practice_item[1] + practice_item[3]
            elif practice_item[2] == "-":
                result = practice_item[1] - practice_item[3]
            elif practice_item[2] == "×":
                result = practice_item[1] * practice_item[3]
            elif practice_item[2] == "÷":
                result = format(practice_item[1] / practice_item[3], ".2f")
            label = self.widget_15.findChild(QLabel, "label" + str(index + 1))
            label.setText(str(practice_item[1]) + practice_item[2] + str(practice_item[3]) + practice_item[4])
            local[index] = practice_item + (result,)
        self.practice = local

    @Slot()
    def checks(self):
        i = 0
        for result in self.practice:
            line_text = self.widget_15.findChild(QLineEdit, "lineEdit" + str(result[0]))
            print(str(result[5]), line_text.text())
            if str(result[5]) == line_text.text():

                line_text.setStyleSheet("#" + "lineEdit" + str(result[0]) + "{\n"
                                                                            "    background-color: rgb(199, 210, 212);\n"
                                                                            "    color: rgb(166, 27, 41);\n"
                                                                            "    border-radius:8px;\n"
                                                                            "}\n"
                                                                            "")
                i = i + 1
            else:
                line_text.setStyleSheet("#" + "lineEdit" + str(result[0]) + "{\n"
                                                                            "    background-color: rgb(166, 27, 41);\n"
                                                                            "    color: rgb(199, 210, 212);\n"
                                                                            "    border-radius:8px;\n"
                                                                            "}\n"
                                                                            "")
        rate = format(i * 100 / 22, ".2f")
        self.rate.setText(rate)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QtWidgets.QWidget()
    View = View()
    View.show()
    sys.exit(app.exec())
