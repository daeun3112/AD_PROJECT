from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QGridLayout, QLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QComboBox, QMessageBox
from PyQt5.QtGui import QColor, QFont

from Petstate import *
import random

class Dog_raising_game(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Status Layout creation
        gameLayout = QGridLayout()

        #pet state display window
        self.petstate = QTextEdit()
        self.petstate.setReadOnly(True)
        self.petstate.setAlignment(Qt.AlignLeft)
        font = self.petstate.font()
        font.setPointSize(font.pointSize())
        self.petstate.setFont(font)
        gameLayout.addWidget(self.petstate, 0, 0, 5, 2)

        #current pet display window
        self.currentpet = QTextEdit()
        self.currentpet.setReadOnly(True)
        gameLayout.addWidget(self.currentpet, 0, 2, 5, 1)

        #each function button (eat, walk, stroke, shower, sleep)
        self.eatButton = QToolButton()
        self.eatButton.setText('    Feeding    ')
        self.eatButton.clicked.connect(self.eatClicked)
        self.eatButton.setStyleSheet('QToolButton {font: bold; background-color: #B0E0E6;}')
        gameLayout.addWidget(self.eatButton, 0, 3)

        self.walkButton = QToolButton()
        self.walkButton.setText('    walking    ')
        self.walkButton.clicked.connect(self.walkClicked)
        self.walkButton.setStyleSheet('QToolButton {font: bold; background-color: #B0E0E6;}')
        gameLayout.addWidget(self.walkButton, 1, 3)

        self.strokeButton = QToolButton()
        self.strokeButton.setText('    stroking   ')
        self.strokeButton.clicked.connect(self.strokeClicked)
        self.strokeButton.setStyleSheet('QToolButton {font: bold; background-color: #B0E0E6;}')
        gameLayout.addWidget(self.strokeButton, 2, 3)

        self.showerButton = QToolButton()
        self.showerButton.setText('  showering  ')
        self.showerButton.clicked.connect(self.showerClicked)
        self.showerButton.setStyleSheet('QToolButton {font: bold; background-color: #B0E0E6;}')
        gameLayout.addWidget(self.showerButton, 3, 3)

        self.sleepButton = QToolButton()
        self.sleepButton.setText('    sleeping   ')
        self.sleepButton.clicked.connect(self.sleepClicked)
        self.sleepButton.setStyleSheet('QToolButton {font: bold; background-color: #B0E0E6;}')
        gameLayout.addWidget(self.sleepButton, 4, 3)

        # new game button
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New game')
        self.newGameButton.clicked.connect(self.startgame)
        self.newGameButton.setStyleSheet('QToolButton {font: bold; background-color: #A3C1DA; color: blue;}')
        gameLayout.addWidget(self.newGameButton, 5, 0)

        # game rules button
        self.ruleButton = QToolButton()
        self.ruleButton.setText('?')
        self.ruleButton.clicked.connect(self.gameRules)
        self.ruleButton.setStyleSheet('QToolButton {font: bold; background-color: #A3C1DA; color: blue;}')
        gameLayout.addWidget(self.ruleButton, 5, 1)

        #pet Status Change message
        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignCenter)
        gameLayout.addWidget(self.message, 5, 2)

        #job select box
        self.job = QComboBox()
        self.job.addItem('doctor')
        self.job.addItem("president")
        self.job.addItem("soccer player")
        self.job.addItem("teacher")
        gameLayout.addWidget(self.job, 5, 3)

        # Layout placement
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(gameLayout, 0, 0)
        self.setLayout(mainLayout)
        self.setWindowTitle('Rasing your own Pet')

        #game start
        self.startgame()

    def startgame(self):
        self.Petname = input("Enter your pet name")

        self.colorChange()    # pet's color changes at random
        self.state = state(self.Petname)
        self.petstate.setText(self.state.displayCurrent())
        self.currentpet.setText(self.state.currentShape())
        self.message.clear()

        self.eatButton.setDisabled(False)
        self.showerButton.setDisabled(False)
        self.strokeButton.setDisabled(False)
        self.sleepButton.setDisabled(False)
        self.walkButton.setDisabled(False)

    def colorChange(self):    #pet color change
        color_list = [QColor(250, 140, 0), QColor(145, 210, 80), QColor(0, 180, 20), QColor(230, 30, 100),
                      QColor(155, 40, 175), QColor(105, 60, 185), QColor(255,70,50)]
        colorvar = random.choice(color_list)
        self.currentpet.setTextColor(colorvar)
        self.currentpet.setFontWeight(QFont.Bold)

    def gameRules(self):   #gamerule message box
        rule = """
        ✔ feeding: hungry-20, happy+15, dirty+15
        ✔ walking: hungry+20, happy+20, tired+30, dirty+25
        ✔ sleeping: happy+15, tired-20
        ✔ showering: happy-25, tired+15, dirty-30
        ✔ stroking: happy+15, dirty+10
        
        ✔ You can choose your own pet's job. 
          When a pet's level reaches 10, it turns into a job!

        ✘ Keep your pet happiness index above zero! 
        (Your pet may run away.)
        """
        QMessageBox.about(self, 'Game rules', rule)


    def eatClicked(self):
        if self.state.current['°⌓° hungry']<=20:
            self.message.setText("I\'m not hungry")
        else:
            self.state.current['°⌓° hungry'] -= 20  #pet state change
            self.state.current['･ᴗ･  happy'] += 15
            self.state.current['ʘ‿ʘ  dirty'] += 15
            self.petstate.setText(self.state.displayCurrent())
            self.currentpet.setText(self.state.currentShape())
            self.message.setText('hungry: -20, happy, dirty: +15!')
        self.checkLevel()


    def walkClicked(self):
        if self.state.current['⌣_⌣́    tired']>=80:
            self.message.setText("I\'m very tired")
        elif self.state.current['°⌓° hungry']>=80:
            self.message.setText("I\'m very hungry")
        elif self.state.current['ʘ‿ʘ  dirty']>=70:
            self.message.setText('Let me take a shower first!')
        else:
            self.state.current['°⌓° hungry'] += 20  #pet state change
            self.state.current['･ᴗ･  happy'] += 20
            self.state.current['⌣_⌣́    tired'] += 30
            self.state.current['ʘ‿ʘ  dirty'] += 25
            self.petstate.setText(self.state.displayCurrent())
            self.currentpet.setText(self.state.currentShape())
            self.message.setText('hungry, happy: +20, dirty: +25, tired: +30')
        self.checkLevel()


    def showerClicked(self):
        if self.state.current['⌣_⌣́    tired']>=80:
            self.message.setText("I\'m very tired")
        elif self.state.current['ʘ‿ʘ  dirty']<=30:
            self.message.setText("I\'m clean now!")
        else:
            self.state.current['･ᴗ･  happy'] -= 25  #pet state change
            self.state.current['⌣_⌣́    tired'] += 15
            self.state.current['ʘ‿ʘ  dirty'] -= 30
            self.petstate.setText(self.state.displayCurrent())
            self.currentpet.setText(self.state.currentShape())
            self.message.setText('happy: -25, tired: +15, dirty: -30')
        self.checkLevel()


    def strokeClicked(self):
        if self.state.current['ʘ‿ʘ  dirty']>=90:
            self.message.setText('Let me take a shower first!')
        else:
            self.state.current['･ᴗ･  happy'] += 15   #pet state change
            self.state.current['ʘ‿ʘ  dirty'] += 10
            self.petstate.setText(self.state.displayCurrent())
            self.currentpet.setText(self.state.currentShape())
            self.message.setText('happy: +15, dirty: +10')
            self.checkLevel()


    def sleepClicked(self):
        if self.state.current['⌣_⌣́    tired']<=20:
            self.message.setText("I\'m not sleepy")
        else:
            self.state.current['･ᴗ･  happy'] += 15    #pet state change
            self.state.current['⌣_⌣́    tired'] -= 20
            self.petstate.setText(self.state.displayCurrent())
            self.currentpet.setText(self.state.currentShape())
            self.message.setText('happy: +15, tired: -20')
        self.checkLevel()


    def checkLevel(self):
        if self.state.current['･ᴗ･  happy'] <= 0:
            self.currentpet.setText(self.state.currentShape())
            self.message.setText('Sorry. Your pet ran away')
            self.eatButton.setDisabled(True)    #button deactivation
            self.showerButton.setDisabled(True)
            self.strokeButton.setDisabled(True)
            self.sleepButton.setDisabled(True)
            self.walkButton.setDisabled(True)

        elif self.state.current['✔ Level']>=10:
            job = self.job.currentText()
            self.petstate.setText(self.state.displayCurrent())
            self.currentpet.setText(self.state.futureShape(job))
            self.message.setText('Your pet got a job!: {}'.format(job))
            QMessageBox.about(self, "The end", "Congratulations!")
            self.eatButton.setDisabled(True)    #button deactivation
            self.showerButton.setDisabled(True)
            self.strokeButton.setDisabled(True)
            self.sleepButton.setDisabled(True)
            self.walkButton.setDisabled(True)

        elif self.state.current['･ᴗ･  happy']>=90:
            self.state.current['✔ Level']+=1
            self.state.current['･ᴗ･  happy'] = 30
            self.petstate.setText(self.state.displayCurrent())
            self.currentpet.setText(self.state.currentShape())
            self.message.setText('Level up!')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = Dog_raising_game()
    game.show()
    sys.exit(app.exec_())