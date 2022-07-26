from PyQt6.QtCore import Qt, QObject, QPoint, pyqtProperty, QPropertyAnimation
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
        self.maze = []
        for col in range(hsize):
            self.maze.append([])
            for row in range(vsize):
                sqw = SquareWidget(self, (row,col), 0)
                sqw.move(self.square_size * col, self.square_size * row)
                self.maze[col].append(sqw)
        self.resize(self.square_size * hsize, self.square_size * vsize)
    
    def get_square(self, col, row):
        return self.maze[col][row]

    def get_square(self, col, row):
        return self.maze[col][row]

class Path(QObject):
    @pyqtProperty(int)
    def step(self):
        return self._step

    @step.setter
    def step(self, n):
        self._step = n
        col, row = self.path[n]
        sq = self.maze.get_square(col, row)
        sq.value = -1
        sq.update()

    def __init__(self, maze, path):
        self.path = path
        self.maze = maze
        self._step = 0
        super().__init__()
    
    def show(self):
        for (row,col) in self.path:
            sq = self.maze.get_square(col, row)
            print(sq.position)
            sq.value = -1
            sq.update()
        
    def animate(self):
        k = len(self.path)-1
        self.anim = QPropertyAnimation(self, b"step")
        self.anim.setStartValue(0)
        self.anim.setEndValue(k)
        self.anim.setDuration(500*k)
        self.anim.start()


class QWindow(QWidget):
    def __init__(self):
        super().__init__()


app = QApplication(sys.argv)
maze = MazeWidget(20, 20)
path = Path(maze, [(i,i) for i in range(2,18)])
maze.show()
path.animate()
#sys.exit(app.exec())
sys.exit(app.exec())