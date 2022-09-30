
import os
from mainV2 import *
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from threading import Thread
import pandas as pd
import subprocess

#CREAZIONE DIR SALVATAGGIO DATI
try:
    os.makedirs("Salvataggi grafici")
except:
    pass
percorso = os.getcwd()
os.chdir(f"{percorso}/Salvataggi grafici")
percorso = os.getcwd()

Vo_list = []
tempo_list = []
Vi = 0
caso = 0
induttanza = ""
resistenza_1 = ""
resistenza_2 = ""
condensatore = ""

class Edit(Ui_calc_flx):
    def __init__(self, Widget):
        self.setupUi(Widget)

        #AGGIUNTA GRAFICO
        self.horizontalLayout_20=QtWidgets.QHBoxLayout(self.frame)#AGGIUNGERE LAYOUT AL POSTO DI FRAME VUOTO
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.figure=plt.figure()
        self.canvas=FigureCanvas(self.figure)
        self.horizontalLayout_20.addWidget(self.canvas)#CANVAS DENTRO AL LAYOUT
        self.tempo_ripetizioni.setText("0.002")
        self.check()


    #CHECK TASTI E LINK FUNZIONI
    def check(self):
        self.anteprimaGrafico.clicked.connect(self.anteGraph)
        self.salvataggio.clicked.connect(self.save)
        self.cartellaSalvataggi.clicked.connect(self.apricartella)

        

    def errore(self,testo):
        errore = QtWidgets.QErrorMessage()
        errore.showMessage(testo)
        errore.exec()

    def Graph(self):
        global induttanza, resistenza_1, resistenza_2, condensatore
        induttanza = self.induttanza.text()
        resistenza_1 = self.resistenza_1.text()
        resistenza_2 = self.resistenza_2.text()
        condensatore = self.condensatore.text()
        global caso
        if(((induttanza!="") and (resistenza_1!="")) and ((resistenza_2!="") and (condensatore!=""))):
            self.errore("Scegliere il tipo di circuito da analizzare")
            return
        if(((induttanza=="") and (resistenza_1=="")) and ((resistenza_2=="") and (condensatore==""))):
            self.errore("Mettere dei dati")
            return
        tempoRipetizioni= self.tempo_ripetizioni.text()
        if(tempoRipetizioni==""):
            self.errore("Scrivi un tempo per la campionatura ")
            return
        else:
            try:
                tempoRipetizioni = float(self.tempo_ripetizioni.text())
            except:
                self.errore("Scrivi un numero sul tempo di campionatura")
                return
        if ((induttanza!="") and (resistenza_1!="")):
            try:
                induttanza = float(self.induttanza.text())
            except:
                self.errore("Scrivi un numero sulla induttanza")
                return
            try:
                resistenza_1 = int(self.resistenza_1.text())
            except:
                self.errore("Scrivi un numero intero sulla resistenza")
                return
            caso = 1
            tau = induttanza/resistenza_1
        elif((resistenza_2!="") and (condensatore!="")):
            try:
                resistenza_2 = int(self.resistenza_2.text())
            except:
                self.errore("Scrivi un numero intero sulla resistenza")
                return
            try:
                condensatore = float(self.condensatore.text())
            except:
                self.errore("Scrivi un numero sul condensatore")
                return
            caso = 2
            tau = resistenza_2*condensatore
        else:
            self.errore("Scrivi numeri per formare il tau")

        global Vi
        Vi = int(self.Vi.text())
        Vo=0
        tempo = 0
        global Vo_list, tempo_list
        Vo_list = []
        tempo_list = []
        for item in range(50):
            Vo = ((tempo/tau)*Vi)+Vo*((tau-tempo)/tau)
            Vo_list.append(Vo)
            tempo_list.append(tempo)
            tempo = tempo+tempoRipetizioni
        self.figure.clear()
        plt.plot(tempo_list,Vo_list)
        self.canvas.draw()
        
    def anteGraph(self):
        self.Graph()

    def save(self):
        if (caso == 0):
            return
        tabella = {
            "TEMPO":tempo_list,
            "Vi(t)":Vi,
            "Vo(t)":Vo_list
        }
        convert=pd.DataFrame(tabella)
        if (caso==1):
            convert.to_csv(f"Vi{Vi}_L{induttanza}_R{resistenza_1}.csv",index=False)
        if (caso==2):
            convert.to_csv(f"Vi{Vi}_R{resistenza_2}_C{condensatore}.csv",index=False)
        



    def apricartella(self):
        try:
            subprocess.call(["open", percorso])  # MACOS
        except:
            subprocess.Popen(f'explorer "{percorso}"')  # WINDOWS

app = QtWidgets.QApplication(sys.argv)
Widget = QtWidgets.QWidget()
ui = Edit(Widget)
Widget.show()
Widget.setFixedSize(900, 600)
sys.exit(app.exec())