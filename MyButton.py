from PyQt5.QtWidgets import *

class MyButton(QPushButton):
    def __init__(self,name):
        super().__init__(name)
        self.mfont = super().font()
        self.mfont.setPointSize(17)
        super().setFont(self.mfont)
        super().setFixedSize(100,50)

    def numbers_button(self):
        self.mfont.setPointSize(20)
        super().setFont(self.mfont)
        super().setFixedSize(115,50)

    def down_marks(self):
        self.mfont.setPointSize(14)
        super().setFont(self.mfont)
        super().setFixedSize(80,40)

    def equals_mark(self):
        self.mfont.setPointSize(21)
        super().setFont(self.mfont)
        super().setFixedSize(90,50)
        super().setStyleSheet("background-color: #ffff99")