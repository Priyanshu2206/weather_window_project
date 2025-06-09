import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget , QPushButton , QHBoxLayout , QLineEdit , QMessageBox
from PyQt5.QtCore import QTimer, QTime , Qt

class UnitControl(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Unit Control")
        self.setGeometry(100, 100, 300, 200)
 
        self.category_label = QLabel("Select Category:", self)
        self.cateroryInput = QLineEdit(self)
        self.cateroryInput.setPlaceholderText("Enter length, weight, or temperature")
        
        self.category_label.setAlignment(Qt.AlignCenter)
        self.category_label.setStyleSheet("font-size: 20px; font-weight: bold;")

        #  input lineEdit for user input
        self.input_label = QLineEdit(self)
        self.input_label.setPlaceholderText("Enter value to convert (e.g., 100)")
        self.input_label.setGeometry(50, 50, 200, 30)
        self.input_label.setAlignment(Qt.AlignCenter)
        self.input_label.setStyleSheet("font-size: 18px; padding: 5px;")

        #  button to submit the input
        
        self.SubmitButton = QPushButton("convert" , self)
        self.SubmitButton.setGeometry(100, 100, 100, 30)
        self.SubmitButton.setStyleSheet("font-size: 18px; background-color: lightblue;")
        self.SubmitButton.clicked.connect(self.convertUnits)

        # result label to display the output
        self.ResultLabel = QLabel("Result will be displayed here : ", self)
        self.ResultLabel.setAlignment(Qt.AlignCenter)
        self.ResultLabel.setStyleSheet("font-size: 18px; color: green;")
        

        #   for layouts
        vbox = QVBoxLayout()
        vbox.addWidget(self.category_label)
        vbox.addWidget(self.cateroryInput)
        vbox.addWidget(self.input_label)
        vbox.addWidget(self.SubmitButton)
        vbox.addWidget(self.ResultLabel)

        self.setLayout(vbox)
        
        # Connect the button click to the method
        self.SubmitButton.clicked.connect(self.convertUnits)

    def convertUnits(self):
        category = self.cateroryInput.text().strip().lower()
        try:
            value = float(self.input_label.text())
        except ValueError:
            QMessageBox.warning(self , "Invalid Input", "Please enter a valid number.")
            return
        
        result = ""
        if category == "length":
            result += f"{value} centimeters = {value * 100:.3f} centimeters\n"
            result += f"{value} kilometers = {value / 1000:.3f} kilometers\n"
            result += f"{value} milimiters = {value * 1000:.3f} milimiters\n"
            result += f"{value} feet = {value * 3.28:.3f} feet\n"

        elif category == "weight":
            result += f"{value} kilograms = {value * 1000:.3f} grams\n"
            result += f"{value} pounds = {value * 2.20462:.3f} pounds\n"
            result += f"{value} ounces = {value * 35.272:.3f} ounces\n"

        elif category == "temperature":
            result += f"{value} Fahrenheit = {(value - 32) * 5/9:.2f} Celsius\n"
            result += f"{value} Kelvin = {value + 273.15:.2f} Kelvin\n"
        else:
            result = "Unknown category! Use: length, weight, or temperature."
        
        self.ResultLabel.setText(result)
       


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UnitControl()
    window.show()
    sys.exit(app.exec_())