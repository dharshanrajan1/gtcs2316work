## used pyqt5 as my installation for pyqt6 was bugging 

## prompt: https://docs.google.com/document/d/1CrSk7TqEA6WcscVH1ymrajAvK_HMw-z9JusLwzMwIFc/edit


  ### EXTRA CREDIT FEATURES TO Test: 
    ## Color Changed to turquoise (my favorite color :)): 
        ## https://doc.qt.io/qtforpython-6/overviews/stylesheet-examples.html (documentation for color changing) 
    ## Added a progress bar to indicate the percentage of the letters the user has input. I used the assigned documentation and 
    # https://www.geeksforgeeks.org/pyqt5-qprogressbar-how-to-create-progress-bar/ (Functionality and Widget Requirement)



import re, random, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import requests
import donottouch as dt

class Window(QMainWindow):
    def __init__(self):
        ######################################
        #Basic Set Up Code - DO NOT TOUCH
        super().__init__()
        frame = self.frameGeometry()
        #center = self.screen().availableGeometry().center()
        #frame.moveCenter(center)
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        self.move(frame.topLeft())
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setStyleSheet("background-color: #40E0D0;") ## changed the color of background using setStyleSheet (Ec 1) 
        self.board = dt.Board()
        self.board.setHidden(True)
        self.board.setFixedWidth(500)
        self.leftpane = dt.LeftPane()
        self.leftpane.addItems(self.board.WORDLIST)

        ######################################
        #Insert Code Below
        self.setWindowTitle("Wordle 2 Electric Boogaloo")
        self.leftpane.hide()
        self.points = 0

        ## labeles 1-3
        self.start_label1 = QLabel("WELCOME")
        self.start_label1.setFont(QFont("Arial", 20))
        self.start_label2 = QLabel("TO", self)
        self.start_label2.setFont(QFont("Arial", 20))
        self.start_label3 = QLabel("WORDLE 2", self)
        self.start_label3.setFont(QFont("Arial", 20))
        self.start_label1.setAlignment(Qt.AlignCenter)
        self.start_label2.setAlignment(Qt.AlignCenter)
        self.start_label3.setAlignment(Qt.AlignCenter)
        ##---------
        self.points_label = QLabel(f"Total Points: {self.points}", self)
        self.points_label.hide()
        self.points_label.setFont(QFont("Arial", 16))
        self.points_label.setAlignment(Qt.AlignCenter)
        self.points_label.setFixedSize(400, 100)

        ## ---- 
        self.valid_word_labell = QLabel("Check Word: ", self)
        self.valid_word_labell.hide()
        self.valid_word_labell.setFont(QFont("Arial", 16))
        self.valid_word_labell.setAlignment(Qt.AlignCenter)
        self.valid_word_labell.setFixedSize(150, 100)

        ##---
        self.start_button= QPushButton("Start")
        self.start_button.clicked.connect(self.startGame)
        self.start_button.setFont(QFont("Arial", 24))
        self.start_button.setFixedSize(200,100)
        ##--
        self.reset_button= QPushButton("Reset")
        self.reset_button.clicked.connect(self.resetGame)
        self.reset_button.setHidden(True)
        self.reset_button.setFont(QFont("Arial", 16))
        self.reset_button.setFixedSize(100,50)

        #---
        self.hint_button= QPushButton("Hint")
        self.hint_button.clicked.connect(self.toggleHint)
        self.hint_button.setHidden(True)
        self.hint_button.setEnabled(False)
        self.hint_button.setFont(QFont("Arial", 16))
        self.hint_button.setFixedSize(100,50)

        self.easy_mode_button= QRadioButton("Easy Mode")
        self.easy_mode_button.setFont(QFont("Arial", 10))
        self.easy_mode_button.setFixedWidth(200)


        self.valid_word_box= QLineEdit("Enter Word")
        self.valid_word_box.textEdited.connect(self.validWord)
        self.valid_word_box.setHidden(True)
        self.valid_word_box.setFont(QFont("Arial", 16))
        self.valid_word_box.setFixedHeight(100)
        self.valid_word_box.setFixedWidth(150)
        self.valid_word_box.setAlignment(Qt.AlignCenter)


        ## ------
        self.vbox_start = QVBoxLayout()
        self.vbox_start.addWidget(self.start_label1)
        self.vbox_start.addWidget(self.start_label2)
        self.vbox_start.addWidget(self.start_label3)
        self.vbox_start.addWidget(self.start_button)
        self.vbox_start.addWidget(self.easy_mode_button)
        #+ hbox
        self.hbox_buttons = QHBoxLayout()
        self.hbox_buttons.addWidget(self.reset_button)
        self.hbox_buttons.addWidget(self.hint_button)

        self.hbox_valid_word = QHBoxLayout()
        self.hbox_valid_word.addWidget(self.valid_word_labell)
        self.hbox_valid_word.addWidget(self.valid_word_box)

        # vbox for game part
        self.vbox_game = QVBoxLayout()
        self.vbox_game.addWidget(self.points_label)
        self.vbox_game.addLayout(self.hbox_buttons)
        self.vbox_game.addLayout(self.hbox_valid_word)

        ## main hbox 
        self.hbox_main = QHBoxLayout(self.centralwidget)
        self.hbox_main.addLayout(self.vbox_start)
        self.hbox_main.addWidget(self.leftpane)
        self.hbox_main.addWidget(self.board)
        self.hbox_main.addLayout(self.vbox_game)


      






        
        ######################################


    def updateProgressBar(self):
     text_length = len(self.valid_word_box.text())
     self.progress_bar.setValue(text_length)


    def startGame(self):

        ######################################
        #Basic Set Up Code - DO NOT TOUCH
        self.setFixedWidth(1000)
        ######################################
        #Insert Code Below
        self.start_button.setHidden(True)
        self.start_label1.setHidden(True)
        self.start_label2.setHidden(True)
        self.start_label3.setHidden(True)
        self.board.setHidden(False)
        self.reset_button.setHidden(False)
        self.hint_button.setHidden(False)
        self.points_label.setHidden(False)
        self.valid_word_labell.setHidden(False)
        self.valid_word_box.setHidden(False)
        if self.easy_mode_button.isChecked():
            self.hint_button.setEnabled(True)
        else:
            self.hint_button.setEnabled(False)
        ## hide it aftert the if 
        self.easy_mode_button.setHidden(True)

               ## Ec 2 (part 1) 
        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedWidth(300)
        self.progress_bar.setRange(0, 5)  
        self.valid_word_box.textChanged.connect(self.updateProgressBar)
        self.vbox_game.addWidget(self.progress_bar)

        ######################################


    def resetGame(self):
        ######################################
        # Basic Set Up Code - DO NOT TOUCH
        self.board.reset()
        self.setFixedWidth(500)
        ######################################
        
        self.board.setHidden(True)
        self.reset_button.setHidden(True)
        self.hint_button.setHidden(True)
        self.leftpane.setHidden(True)
        self.points_label.setHidden(True)
        self.valid_word_labell.setHidden(True)
        self.valid_word_box.setHidden(True)
        self.start_button.setHidden(False)
        self.start_label1.setHidden(False)
        self.start_label2.setHidden(False)
        self.start_label3.setHidden(False)
        self.easy_mode_button.setHidden(False)
        self.valid_word_labell.setText("Check Word:")
        self.valid_word_box.setText("Enter Word")
        self.easy_mode_button.setChecked(False)
        self.points = 0
        self.points_label.setText(f"Total Points: {self.points}")
        self.hint_button.setEnabled(False)
        self.progress_bar.setValue(0)
        self.progress_bar.setEnabled(False)
        self.progress_bar.setHidden(True)

        
        ######################################

    def toggleHint(self):
        ######################################
        #Insert code here
        
#         Check whether or not self.leftpane is hidden or not. 
# If it is hidden, un-hide the left pane
# Otherwise, hide the left pane
        if self.leftpane.isHidden():
            self.leftpane.setHidden(False)
        else: 
            self.leftpane.setHidden(True)




        ######################################


    def addPoints(self):
        ######################################
        #Insert code here
#         Increment self.points by 1
# Update the text on self.points_label to reflect the new total points

        self.points+=1
        self.points_label.setText(f"Total Points  {self.points}")



        ######################################

    def validWord(self):
        ######################################
        #Insert code here
        r = requests.get(f"https://www.dictionary.com/browse/{self.valid_word_box.text()}")
        if r.status_code == 200:
            if len(self.valid_word_box.text()) == 5:
                # print(len(self.valid_word_box.text()))
                self.valid_word_labell.setText("Valid word!")
            else: 
                self.valid_word_labell.setText("Not valid word!")
        else: 
            self.valid_word_labell.setText("Not valid word!")
        ######################################

if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Fusion')
    window = Window()
    window.show()
    window.setFixedSize(window.size())
    sys.exit(app.exec())