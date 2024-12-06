import sys
import random

from PyQt6 import uic
from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.btn_clicked)
        self.clicked = False

    def paintEvent(self, event):
        if not self.clicked:
            return

        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 216, 0))
        qp.setPen(QColor(255, 216, 0))

        for i in range(3):
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
