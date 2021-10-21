import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import initFunctions
import math

previous_value = 0

class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator")
        self.setFixedSize(400,500)
        self.frame = QVBoxLayout()
        self.initUI()

    def initUI(self):
        self.current = ''

        self.display = QLineEdit('0')
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        font = self.display.font()
        font.setPointSize(30)
        self.display.setFont(font)

        self.frame.addWidget(self.display)
        self.setLayout(self.frame)

        self.items = []

        initFunctions.initScientificOperators(self, self.frame,self.items)
        initFunctions.initOperators(self,self.frame,self.items)
        initFunctions.initNumbers(self,self.frame,self.items)
        initFunctions.initDownMarks(self,self.frame,self.items)

        print(self.items)


    def showColorDialog(self):
        selected_color = QColorDialog.getColor()
        if selected_color.isValid():
            x = len(self.items)
            for a in range(x):
                button = self.items[a]
                button.setStyleSheet("QWidget { background-color: %s}" % selected_color.name())


    def press_button(self):
        clickedChar = self.sender()
        global previous_value
        if clickedChar.text() == '\u232B': #backspace
            self.current = str(eval(self.current))
            self.current = self.current[:-1]
            self.display.setText(self.current)

        elif clickedChar.text() == 'x\u00b2': #power2
            temp = float(self.current)
            temp = pow(temp,2)
            if temp == int(temp):
                self.current = int(temp)
                self.display.setText(str(self.current))
            else:
                self.current = str(temp)
                self.display.setText(self.current)

        elif clickedChar.text() == 'x\u00AA': #powerX
            self.current += '^'
            self.display.setText(str(self.current))

        elif clickedChar.text() == '\u03C0': # pi
            self.current += '\u03C0'
            self.display.setText(str(self.current))

        elif clickedChar.text() == '|x|': #|x|
            if float(self.current) >=0:
                self.display.setText(str(self.current))
            else:
                self.current = float(self.current) * -1
                if self.current == int(self.current):
                    self.display.setText(str(int(self.current)))
                else:
                    self.display.setText(str(self.current))

        elif clickedChar.text() == '\u00B2\u221A':  # root2
            temp = float(self.current)
            temp = math.sqrt(temp)
            self.current = str(temp)
            self.display.setText(self.current)

        elif clickedChar.text() == '\u00AA\u221A':  # rootX
            self.current += '\u221A'
            self.display.setText(str(self.current))
            "x\u0021"

        elif clickedChar.text() ==  "x\u0021":  # factorial
            self.current = math.factorial(int(self.current))
            self.display.setText(str(self.current))

        elif clickedChar.text() == 'C':
            self.current = ''
            self.display.setText(self.current)

        elif clickedChar.text() == 'THEME':
            self.showColorDialog()
        elif clickedChar.text() == '=':
            try:
                if "^" in self.current:
                    temp1 = self.current.split("^",1)[0]
                    temp2 = self.current.split("^",1)[1]
                    temp3 = float(temp1)**float(temp2)
                    self.current = str(temp3)
                    self.display.setText(self.current)
                    previous_value = temp3

                elif "\u221A" in self.current:
                    temp1 = self.current.split("\u221A",1)[0]
                    temp2 = self.current.split("\u221A",1)[1]
                    temp1 = int(temp1)
                    temp3 = float(temp2) ** float((1/temp1))
                    self.current = str(temp3)
                    self.display.setText(self.current)
                    previous_value = temp3

                else:
                    if self.current == '':
                        temp = 0
                        self.current = str(temp)
                        self.display.setText(self.current)
                    else:
                        if '\u03C0' in self.current:
                            self.current = self.current.replace('\u03C0', str(math.pi))
                        temp = eval(self.current)

                    if temp == previous_value:
                        self.current = str(temp)
                        self.display.setText(self.current)
                    else:
                            if '\u03C0' in self.current:
                                self.current = self.current.replace('\u03C0', str(math.pi))
                            temp = eval(self.current)
                            if temp == int(temp):
                                self.current = int(temp)
                            tmp = eval (self.current)
                            self.current = str(tmp)
                            self.display.setText(self.current)
                            previous_value = self.current
                tmp = eval(self.current)
                if tmp == int(tmp):
                    self.current = str(int(tmp))
                    self.display.setText(self.current)
            except Exception as e:
                QMessageBox.about(self, 'Error', 'Podano złe wyrażenie! Powód: ' + str(e) )
        else:
            self.current += clickedChar.text()
            self.display.setText(str(self.current))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = Calculator()
    run.show()
    sys.exit(app.exec_())

