import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

## first class is for the window/menu page 
class MenuPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu Page')
        self.setGeometry(100, 100, 300, 200)
        self.setStyleSheet(
            "background-color: black;"
        )
        self.showMaximized() ## make the window full screen

        self.title_label = QLabel('CS 2316 Final Project GUI')
        self.title_label.setStyleSheet(
            "font-size: 20px;"
            "font-weight: bold;"
            "margin-bottom: 20px;"
            "color: yellow;"
        )

        self.calculator_button = QPushButton('GDP Calculator')
        self.calculator_button.setStyleSheet(
            "background-color: #4CAF50;"
            "border: none;"
            "border-radius: 5px;"
            "padding: 10px;"
            "color: #ffffff;"
        )
        self.calculator_button.clicked.connect(self.open_gdp_calculator)

        vbox = QVBoxLayout()
        vbox.addWidget(self.title_label, alignment=Qt.AlignCenter)
        vbox.addWidget(self.calculator_button, alignment=Qt.AlignCenter)
        vbox.addStretch(1)

        self.setLayout(vbox)

    def open_gdp_calculator(self):
        self.gdp_calculator = GDP_Calculator() ## opens the calculator page 
        self.gdp_calculator.show()
        self.hide()

## second class is for the calculator 
class GDP_Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('GDP Calculator')
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet( "background-color: black;""color: yellow;")
        self.showMaximized() ## full screen
        title_label = QLabel('GDP Calculator')
        title_label.setStyleSheet(
            "font-size: 24px;"
            "font-weight: bold;"
            "margin-bottom: 20px;"
            "color: yellow;"
        )

        self.year_label = QLabel('Enter the Year:')
        self.year_input = QLineEdit()
        self.year_input.setStyleSheet(
            "background-color: #ffffff;"
            "border: 1px solid #cccccc;"
            "border-radius: 5px;"
            "padding: 8px;"
            "color: #333333;"
        )

        self.calculate_button = QPushButton('Calculate GDP')
        self.calculate_button.setStyleSheet(
            "background-color: #4CAF50;"
            "border: none;"
            "border-radius: 5px;"
            "padding: 10px;"
            "color: #ffffff;"
        )

        self.clear_button = QPushButton('Clear')
        self.clear_button.setStyleSheet(
            "background-color: #f44336;"
            "border: none;"
            "border-radius: 5px;"
            "padding: 10px;"
            "color: #ffffff;"
        )

        self.output = QLabel('GDP will be displayed here:')
        self.output.setStyleSheet(
            "font-size: 16px;"
            "margin-top: 20px;"
        )

        self.table = QTableWidget()
        self.table.setStyleSheet("background-color: #333333; color: white;")
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Year", "Predicted GDP (Million $)"])

        self.calculate_button.clicked.connect(self.calculate_gdp)
        self.clear_button.clicked.connect(self.clear_inputs)

        vbox = QVBoxLayout()
        vbox.addWidget(title_label, alignment=Qt.AlignCenter)
        vbox.addWidget(self.year_label)
        vbox.addWidget(self.year_input)
        vbox.addWidget(self.calculate_button)
        vbox.addWidget(self.clear_button)
        vbox.addWidget(self.output)
        vbox.addWidget(self.table)
        vbox.addStretch(1)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        hbox.addStretch(1)

        self.setLayout(hbox)

    def calculate_gdp(self):
        year_text = self.year_input.text()
        ## error handling 
        if not year_text.isdigit():
            QMessageBox.warning(self, 'Invalid Input', 'Please enter a valid year (numeric value).')
            return

        year = int(year_text)

        if year < 1776:
            QMessageBox.warning(self, 'Invalid Year', 'Please enter a year from 1776 onwards.')
            return

        # Coefficients
        intercept = -1160868.6852244905
        coefficient = 586.1733469387759

        # Predict GDP using the linear regression formula (derived from the insights) 
        predictgdp = intercept + coefficient * year
        # Updated the table with the predicted year and GDP
        entry1 = self.table.rowCount()
        self.table.insertRow(entry1)
        self.table.setItem(entry1, 0, QTableWidgetItem(str(year)))
        self.table.setItem(entry1, 1, QTableWidgetItem(f'${predictgdp:.2f}'))
        self.output.setText(f'Predicted GDP for {year} is: ${predictgdp:.2f} million')

    def clear_inputs(self):
        self.year_input.clear()
        self.output.setText('GDP will be displayed here')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu_page = MenuPage()
    menu_page.show()
    sys.exit(app.exec_())
