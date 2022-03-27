from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class Mp111(FigureCanvas):
    def __init__(self, parent = None):
        self.fig = Figure(figsize=(6, 6))
        self.fig = Figure(facecolor='#2A2A34')
        self.fig.subplots_adjust(0.0,0.0,1.1,1.0)
        self.ax = self.fig.gca(projection='3d')

        FigureCanvas.__init__(self, self.fig)

class Mp22(FigureCanvas):
    def __init__(self):
        self.fig = Figure(facecolor='0.94')
        self.ax1 = self.fig.add_subplot(221)
        self.ax2 = self.fig.add_subplot(222)
        self.ax3 = self.fig.add_subplot(223)
        self.ax4 = self.fig.add_subplot(224)
        FigureCanvas.__init__(self, self.fig)

class Mwbox(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.canvas = Mp111()
        self.vb1 = QtWidgets.QVBoxLayout()
        self.vb1.addWidget(self.canvas)
        self.setLayout(self.vb1)
