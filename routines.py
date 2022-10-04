
import os
from main_6_grafici import *
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import subprocess
import math

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
Vi_caso = 0
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
        # CHECL SISTEMA DA USARE
        global induttanza, resistenza_1, resistenza_2, condensatore
        induttanza = self.induttanza.text()
        resistenza_1 = self.resistenza_1.text()
        resistenza_2 = self.resistenza_2.text()
        condensatore = self.condensatore.text()
        global caso         #PER VEDERE COME FARE IL GRAFICO
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

        # CHECK CASO DA FARE E TIPO DI GRAFICO
        global Vi, Vi_caso
        if((self.box_costante.isChecked()==True)and(self.box_rampa.isChecked()==False)and(self.box_parabola.isChecked()==False)and
            (self.box_sinusoide.isChecked()==False)and(self.box_sinusoide_2.isChecked()==False)and(self.box_quadra.isChecked()==False)):
            Vi_caso = 1
        elif((self.box_costante.isChecked()==False)and(self.box_rampa.isChecked()==False)and(self.box_parabola.isChecked()==False)and
            (self.box_sinusoide.isChecked()==False)and(self.box_sinusoide_2.isChecked()==False)and(self.box_quadra.isChecked()==True)):
            Vi_caso=2
        elif((self.box_costante.isChecked()==False)and(self.box_rampa.isChecked()==True)and(self.box_parabola.isChecked()==False)and
            (self.box_sinusoide.isChecked()==False)and(self.box_sinusoide_2.isChecked()==False)and(self.box_quadra.isChecked()==False)):
            Vi_caso=3
        elif((self.box_costante.isChecked()==False)and(self.box_rampa.isChecked()==False)and(self.box_parabola.isChecked()==True)and
            (self.box_sinusoide.isChecked()==False)and(self.box_sinusoide_2.isChecked()==False)and(self.box_quadra.isChecked()==False)):
            Vi_caso=4
        elif((self.box_costante.isChecked()==False)and(self.box_rampa.isChecked()==False)and(self.box_parabola.isChecked()==False)and
            (self.box_sinusoide.isChecked()==True)and(self.box_sinusoide_2.isChecked()==False)and(self.box_quadra.isChecked()==False)):
            Vi_caso=5
        elif((self.box_costante.isChecked()==False)and(self.box_rampa.isChecked()==False)and(self.box_parabola.isChecked()==False)and
            (self.box_sinusoide.isChecked()==False)and(self.box_sinusoide_2.isChecked()==True)and(self.box_quadra.isChecked()==False)):
            Vi_caso=6
        else:
            self.errore("Selezionare la Vi")
            return
        
        Vo=0
        tempo = 0
        global Vo_list, tempo_list
        Vo_list = []
        tempo_list = []
        for item in range(50):
            if(Vi_caso==1): #GRADINO
                try:
                    Vi=int(self.Vi_const.text())
                except:
                    self.errore("Scrivi una Vi costante corretta")
                    caso = 0
                    return
            if(Vi_caso==2): #ONDA QUADRA
                try:
                    if (item<10 or (item>20 and item<30) or item>40):
                        Vi=int(self.Vi_quad1.text())
                    else:
                        Vi=int(self.Vi_quad2.text())
                except:
                    self.errore("Scrivi una Vi quadra corretta")
                    caso = 0
                    return
            if(Vi_caso==3): #RAMPA
                try:
                    Vi=tempo
                except:
                    self.errore("Problema con Vi = tempo")
                    caso = 0
                    return
            if(Vi_caso==4): #PARABOLA
                try:
                    Vi=(tempo**2)/2
                except:
                    self.errore("Scrivi una Vi costante corretta")
                    caso = 0
                    return
            if(Vi_caso==5): #SINUSOIDE
                try:
                    costante_sinusoide_1=int(self.const_sinusoide_1.text())
                except:
                    self.errore("Errore lettura costante sinusoide")
                    caso = 0
                    return
                try:
                    frequenza_1=int(self.omega_1.text())
                except:
                    self.errore("Errore lettura frequenza sinusoide")
                    caso = 0
                    return
                Vi=costante_sinusoide_1*math.sin(math.radians(6.28)*frequenza_1*tempo)
            if(Vi_caso==6): #SINUSOIDE DISTURBATA
                try:
                    costante_sinusoide_2=int(self.const_sinusoide_2.text())
                except:
                    self.errore("Errore lettura costante sinusoide")
                    caso = 0
                    return
                try:
                    frequenza_2=int(self.omega_2.text())
                except:
                    self.errore("Errore lettura frequenza sinusoide")
                    caso = 0
                    return
                try:
                    disturbo=float(self.disturbo.text())
                except:
                    self.errore("Errore lettura frequenza sinusoide")
                    caso = 0
                    return
                Vi=costante_sinusoide_2*math.sin(math.radians(6.28)*frequenza_2*tempo)+disturbo*math.sin(math.radians(6.28)*frequenza_2*1000*tempo)
            
               

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
            self.errore("nessun dato da salvare")
            return
        tabella = {
            "TEMPO":tempo_list,
            "Vi(t)":Vi,
            "Vo(t)":Vo_list
        }
        convert=pd.DataFrame(tabella)
        if (caso==1):
            convert.to_csv(f"Vi_caso{Vi_caso}_L{induttanza}_R{resistenza_1}.csv",index=False)
        if (caso==2):
            convert.to_csv(f"Vi_caso{Vi_caso}_R{resistenza_2}_C{condensatore}.csv",index=False)
        



    def apricartella(self):
        try:
            subprocess.call(["open", percorso])  # MACOS
        except:
            subprocess.Popen(f'explorer "{percorso}"')  # WINDOWS

app = QtWidgets.QApplication(sys.argv)
Widget = QtWidgets.QWidget()
ui = Edit(Widget)
Widget.show()
Widget.setFixedSize(890, 690)
sys.exit(app.exec())