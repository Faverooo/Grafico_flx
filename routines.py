
from main import *
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Edit(Ui_calc_flx):
    def __init__(self, Widget):
        self.setupUi(Widget)

        #AGGIUNTA GRAFICO
        self.horizontalLayout_20=QtWidgets.QHBoxLayout(self.frame)#AGGIUNGERE LAYOUT AL POSTO DI FRAME VUOTO
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.figure=plt.figure()
        self.canvas=FigureCanvas(self.figure)
        self.horizontalLayout_20.addWidget(self.canvas)#CANVAS DENTRO AL LAYOUT
        self.check()


    #CHECK TASTI E LINK FUNZIONI
    def check(self):
        self.horizontalLayout_20.addWidget(self.canvas)#CANVAS DENTRO AL LAYOUT
        pass





app = QtWidgets.QApplication(sys.argv)
Widget = QtWidgets.QWidget()
ui = Edit(Widget)
Widget.show()
sys.exit(app.exec())