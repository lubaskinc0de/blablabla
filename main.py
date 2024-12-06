import sys
import random

from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow

from ui_py import Ui_MainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)
        self.ui = ui

        self.ui.btn.clicked.connect(self.btn_clicked)
        self.clicked = False

    def paintEvent(self, event):
        if not self.clicked:
            return

        qp = QPainter()
        qp.begin(self)
        for i in range(3):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            qp.setBrush(QColor(r, g, b))

            x = random.randint(50, self.width())
            y = random.randint(50, self.height())
            d = random.randint(50, 150)

            qp.drawEllipse(QPoint(x, y), d, d)
        qp.end()

    def btn_clicked(self):
        self.clicked = True
        self.repaint()
        self.clicked = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
