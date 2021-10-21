import kalkulator
import MyButton

def initScientificOperators(self, frame,items):
    scientificOperatorsGrid = kalkulator.QGridLayout()
    scientificOperatorsGrid.setSpacing(0)

    scientificOperators = ["|x|", "x\u00b2", "x\u00AA", "\u03C0",
                           "00", "\u00B2\u221A" ,"\u00AA\u221A" ,"x\u0021"]
    scientificOperatorsRange = [(i, j) for i in range(2) for j in range(4)]
    for position, name in zip(scientificOperatorsRange, scientificOperators):
        if name == '':
            continue
        button = MyButton.MyButton(name)
        self.items.append(button)
        button.clicked.connect(self.press_button)
        scientificOperatorsGrid.addWidget(button, *position)


    frame.addLayout(scientificOperatorsGrid)

def initOperators(self, frame,items):
    operatorsGrid = kalkulator.QGridLayout()
    operatorsGrid.setSpacing(0)

    operators = ["/", "*", "+", "-"]
    operatorsRange = [(i, j) for i in range(1) for j in range(4)]
    for position, name in zip(operatorsRange, operators):
        if name == '':
            continue
        button = MyButton.MyButton(name)
        self.items.append(button)
        button.clicked.connect(self.press_button)
        operatorsGrid.addWidget(button, *position)

    frame.addLayout(operatorsGrid)


def initNumbers(self, frame,items):
    numbersGrid = kalkulator.QGridLayout()
    numbersGrid.setSpacing(0)

    numbers = ["7", "8", "9",
               "4", "5", "6",
               "1", "2", "3",
               "\u232B", "0", ".", ]
    numbersRange = [(i, j) for i in range(4) for j in range(3)]
    for position, name in zip(numbersRange, numbers):
        if name == '':
            continue
        button = MyButton.MyButton(name)
        button.numbers_button()
        self.items.append(button)
        button.clicked.connect(self.press_button)
        numbersGrid.addWidget(button, *position)

    frame.addLayout(numbersGrid)


def initDownMarks(self, frame,items):

    downMarksGrid = kalkulator.QGridLayout()
    downMarksGrid.setSpacing(0)

    downMarks = ["C", "=", "THEME"]
    downMarksRange = [(i, j) for i in range(1) for j in range(3)]

    for position, name in zip(downMarksRange, downMarks):
        button = MyButton.MyButton(name)
        if name == '=':
            button.equals_mark()
            button.clicked.connect(self.press_button)
            downMarksGrid.addWidget(button, *position)
            continue
        button.down_marks()
        self.items.append(button)
        button.clicked.connect(self.press_button)
        downMarksGrid.addWidget(button, *position)

    frame.addLayout(downMarksGrid)
