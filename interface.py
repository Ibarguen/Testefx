import sys
from PyQt5 import QtWidgets
from mpl_toolkits.mplot3d import Axes3D
from firstwindow import *
from secondwindow import*
import numpy as np
from matplotlib import cm


class Programa(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Config_button.clicked.connect(self.Showconfwindow)


        self.ui.widget.canvas.ax.set_facecolor('#2A2A34')
        self.ui.widget.canvas.ax.set_title('Real Time Plotting')
        self.ui.widget.canvas.ax.set_xlim3d([-3, 3])
        self.ui.widget.canvas.ax.set_ylim3d([-3, 3])
        #self.ui.widget.canvas.ax.set_zlim3d([0, 20])
        self.ui.widget.canvas.ax.set_xticklabels([])
        self.ui.widget.canvas.ax.set_yticklabels([])
        self.ui.widget.canvas.ax.set_zticklabels([])
        angulo = np.linspace(0,2*np.pi,100)
        alfa, beta = np.meshgrid(angulo, angulo)
        X = 2 * np.cos(alfa) * np.sin(beta)
        Y = 2 * np.sin(alfa) * np.sin(beta)
        Z = 2 * np.cos(beta)
        self.ui.widget.canvas.ax.view_init(0,0)
        self.ui.widget.canvas.ax.plot_wireframe(X,Y,Z, color='b', rstride=5, cstride=5)

    def Showconfwindow(self):
        self.form2 = QtWidgets.QWidget()
        self.ui2 = Ui_SecondWindow()
        self.ui2.setupUi2(self.form2)
        self.form2.show()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_app = Programa()
    mi_app.show()
    sys.exit(app.exec_())