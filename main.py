import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic  # Импортируем uic
from random import randint


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('file.ui', self)  # Загружаем дизайн
        self.x = 250
        self.y = 250
        self.dwaw = False
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.dwaw:
            qp = QPainter()
            qp.begin(self)
            self.drawing(qp)
            qp.end()

    def run(self):
        self.dwaw = True
        self.update()

    def drawing(self, qp):
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        leigt = randint(10, 300)
        qp.drawEllipse(self.x - leigt // 2, self.y - leigt // 2, leigt, leigt)
        mywindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec())
