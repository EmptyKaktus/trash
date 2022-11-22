import sys
from random import randrange

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ell_TF = False
        uic.loadUi('UI.ui', self)
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
        x, y = 350, 350
        rad = randrange(350)
        qp.drawEllipse(x - (rad // 2), y - (rad // 2), rad, rad)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())