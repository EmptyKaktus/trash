import sys
from random import randrange

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ell_TF = False
        self.setGeometry(100, 100, 700, 700)
        self.setWindowTitle('gfhdjsk')

        self.btn = QPushButton(self)
        self.btn.move(290, 320)
        self.btn.resize(120, 30)
        self.btn.setText('Draw ellipse')
        self.btn.clicked.connect(self.ell_click)

    def paintEvent(self, event):
        if self.ell_TF:
            qp = QPainter()
            qp.begin(self)
            self.draw_ell(qp)
            qp.end()
            self.ell_TF = False

    def ell_click(self):
        self.ell_TF = True
        self.repaint()

    def draw_ell(self, qp):
        qp.setBrush(QColor('yellow'))
        x, y = randrange(700), randrange(700)
        rad = randrange(350)
        qp.drawEllipse(x, y, rad, rad)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())