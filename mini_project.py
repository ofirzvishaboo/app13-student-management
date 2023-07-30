import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout,\
    QLineEdit, QPushButton, QComboBox

class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        amount_label = QLabel("Distance: ")
        self.amount_line_edit = QLineEdit()
        self.combo_box = QComboBox()
        self.combo_box.addItem('KM')
        self.combo_box.addItem('Miles')

        time_label = QLabel("Time(hours): ")
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Speed")
        calculate_button.clicked.connect(self.output)

        self.output_label = QLabel("")

        grid.addWidget(amount_label, 0, 0)
        grid.addWidget(self.amount_line_edit, 0, 1)
        grid.addWidget(self.combo_box, 0, 2)

        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)

        grid.addWidget(calculate_button, 2, 1)

        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def output(self):
        calculation = int(self.amount_line_edit.text()) / int(self.time_line_edit.text())
        if self.combo_box.currentText() == "KM":
            self.output_label.setText(f"the speed is {calculation} kph")
        else:
            self.output_label.setText(f"the speed is {calculation} mph")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
