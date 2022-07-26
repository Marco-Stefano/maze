from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QIcon, QPainter, QPen, QBrush
import sys

class SquareWidget(QWidget):
    def __init__(self, parent, position, value):
        super().__init__(parent)
        self.position = position
        self.value = value
        self.resize(parent.square_size, parent.square_size)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        pen = QPen(Qt.GlobalColor.blue, 1, Qt.PenStyle.DotLine)
        painter.setPen(pen)
        if self.value == 0:
            color = Qt.GlobalColor.lightGray
        elif self.value > 0:
            color = Qt.GlobalColor.blue
        else:
            color = Qt.GlobalColor.cyan
        brush = QBrush(color, Qt.BrushStyle.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(0, 0, self.geometry().width(),
                                    self.geometry().height())
        painter.end()

    def mousePressEvent(self, event):
        if self.value == 0:
            self.value = 1
        elif self.value == 1:
            self.value = -1
        elif self.value == -1:
            self.value = 0
        self.update()

class MazeWidget(QWidget):
    def __init__(self, hsize, vsize, parent = None):
        super().__init__(parent)
        self.square_size = 20
        self.maze = [[]]*hsize
        for col in range(hsize):
            for row in range(vsize):
                sqw = SquareWidget(self, (row,col), 0)
                sqw.move(self.square_size * col, self.square_size * row)
                self.maze[col].append(sqw)
        self.resize(self.square_size * hsize, self.square_size * vsize)

class Path()

class QWindow(QWidget):
    def __init__(self):
        super().__init__()


app = QApplication(sys.argv)
window = MazeWidget(20, 20)
window.show()
#sys.exit(app.exec())
sys.exit(app.exec())