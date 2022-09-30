# Form implementation generated from reading ui file 'Calcolo_grafico\form.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from numpy import gradient


class Ui_calc_flx(object):
    def setupUi(self, calc_flx):
        calc_flx.setObjectName("calc_flx")
        calc_flx.resize(900, 600)
        calc_flx.setStyleSheet("background-color: #d9ad7c;\n"
"color: #fff2df;\n"
"font-family:Arial;\n"
"font-size:15px;\n"
"font-weight:bold;\n"
"")
        self.line = QtWidgets.QFrame(calc_flx)
        self.line.setGeometry(QtCore.QRect(370, -30, 3, 800))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.tabWidget = QtWidgets.QTabWidget(calc_flx)
        self.tabWidget.setGeometry(QtCore.QRect(30, 70, 301, 211))
        self.tabWidget.setStyleSheet("color: #674d3c;\n"
"background-color: #a2836e;")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.TextElideMode.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.IR = QtWidgets.QWidget()
        self.IR.setObjectName("IR")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.IR)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 261, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(120, 0))
        self.label.setStyleSheet("color: rgb(255, 242, 223);\n"
"background-color: #a2836e;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.induttanza = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.induttanza.setStyleSheet("border: 2px solid #fff2df;\n"
"border-radius:6px;")
        self.induttanza.setObjectName("induttanza")
        self.horizontalLayout.addWidget(self.induttanza)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(120, 0))
        self.label_2.setStyleSheet("background-color: #a2836e;\n"
"color: rgb(255, 242, 223);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.resistenza_1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.resistenza_1.setStyleSheet("border: 2px solid #fff2df;\n"
"border-radius:6px;")
        self.resistenza_1.setObjectName("resistenza_1")
        self.horizontalLayout_2.addWidget(self.resistenza_1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_7 = QtWidgets.QLabel(self.IR)
        self.label_7.setGeometry(QtCore.QRect(-10, -30, 311, 241))
        self.label_7.setStyleSheet("background-color: #d9ad7c;\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.IR)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 281, 161))
        self.label_8.setStyleSheet("background-color: #a2836e;\n"
"border: 2px solid #fff2df;\n"
"border-radius:15px;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_7.raise_()
        self.label_8.raise_()
        self.verticalLayoutWidget.raise_()
        self.tabWidget.addTab(self.IR, "")
        self.RC = QtWidgets.QWidget()
        self.RC.setObjectName("RC")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.RC)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 30, 261, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setMinimumSize(QtCore.QSize(120, 0))
        self.label_3.setStyleSheet("color: rgb(255, 242, 223);\n"
"background-color: #a2836e;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.resistenza_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.resistenza_2.setStyleSheet("border: 2px solid #fff2df;\n"
"border-radius:6px;")
        self.resistenza_2.setObjectName("resistenza_2")
        self.horizontalLayout_3.addWidget(self.resistenza_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setMinimumSize(QtCore.QSize(120, 0))
        self.label_4.setStyleSheet("background-color: #a2836e;\n"
"color: rgb(255, 242, 223);\n"
"font-size:14px;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.condensatore = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.condensatore.setStyleSheet("border: 2px solid #fff2df;\n"
"border-radius:6px;")
        self.condensatore.setObjectName("condensatore")
        self.horizontalLayout_4.addWidget(self.condensatore)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.label_9 = QtWidgets.QLabel(self.RC)
        self.label_9.setGeometry(QtCore.QRect(-10, -10, 321, 221))
        self.label_9.setStyleSheet("background-color: #d9ad7c;")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.RC)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 281, 161))
        self.label_10.setStyleSheet("background-color: #a2836e;\n"
"border: 2px solid #fff2df;\n"
"border-radius:15px;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_9.raise_()
        self.label_10.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.tabWidget.addTab(self.RC, "")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(calc_flx)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 340, 261, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_5.setMinimumSize(QtCore.QSize(100, 0))
        self.label_5.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("background-color: #d9ad7c;")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.Vi = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.Vi.setStyleSheet("border: 2px solid #fff2df;\n"
"background-color: rgb(162, 131, 110);\n"
"border-radius:6px;")
        self.Vi.setObjectName("Vi")
        self.horizontalLayout_5.addWidget(self.Vi)
        self.label_6 = QtWidgets.QLabel(calc_flx)
        self.label_6.setGeometry(QtCore.QRect(-30, -10, 951, 651))
        self.label_6.setStyleSheet("background-color: #674d3c;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(calc_flx)
        self.label_11.setGeometry(QtCore.QRect(18, 45, 331, 261))
        self.label_11.setStyleSheet("background-color: rgb(162, 131, 110);\n"
"border-radius: 20px;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(calc_flx)
        self.label_12.setGeometry(QtCore.QRect(20, 320, 331, 101))
        self.label_12.setStyleSheet("background-color: rgb(162, 131, 110);\n"
"border-radius: 20px;")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(calc_flx)
        self.label_13.setGeometry(QtCore.QRect(30, 330, 311, 81))
        self.label_13.setStyleSheet("background-color: #d9ad7c;\n"
"border-radius: 10px")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(calc_flx)
        self.label_14.setGeometry(QtCore.QRect(20, 440, 331, 141))
        self.label_14.setStyleSheet("background-color: rgb(162, 131, 110);\n"
"border-radius: 20px;")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(calc_flx)
        self.label_15.setGeometry(QtCore.QRect(30, 450, 311, 121))
        self.label_15.setStyleSheet("background-color: #d9ad7c;\n"
"border-radius: 10px")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(calc_flx)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(40, 460, 281, 101))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.anteprimaGrafico = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.anteprimaGrafico.setStyleSheet("background-color: #674d3c;\n"
"")
        self.anteprimaGrafico.setObjectName("anteprimaGrafico")
        self.verticalLayout_3.addWidget(self.anteprimaGrafico)
        self.grafico = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.grafico.setStyleSheet("background-color: #674d3c;")
        self.grafico.setObjectName("grafico")
        self.verticalLayout_3.addWidget(self.grafico)
        self.salvataggio = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.salvataggio.setStyleSheet("background-color: #674d3c;")
        self.salvataggio.setObjectName("salvataggio")
        self.verticalLayout_3.addWidget(self.salvataggio)
        self.label_16 = QtWidgets.QLabel(calc_flx)
        self.label_16.setGeometry(QtCore.QRect(390, 520, 481, 61))
        self.label_16.setStyleSheet("background-color: rgb(162, 131, 110);\n"
"border-radius: 20px;")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(calc_flx)
        self.label_17.setGeometry(QtCore.QRect(410, 530, 441, 41))
        self.label_17.setStyleSheet("background-color: #d9ad7c;\n"
"border-radius: 10px")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.cartellaSalvataggi = QtWidgets.QPushButton(calc_flx)
        self.cartellaSalvataggi.setGeometry(QtCore.QRect(420, 540, 421, 24))
        self.cartellaSalvataggi.setStyleSheet("background-color: #674d3c;")
        self.cartellaSalvataggi.setObjectName("cartellaSalvataggi")
        self.frame = QtWidgets.QFrame(calc_flx)
        self.frame.setGeometry(QtCore.QRect(389, 29, 481, 471))
        self.frame.setStyleSheet("background-color: rgb(162, 131, 110);\n"
"border-radius: 20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_6.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_11.raise_()
        self.line.raise_()
        self.tabWidget.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.cartellaSalvataggi.raise_()
        self.frame.raise_()
        self.retranslateUi(calc_flx)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(calc_flx)


    def retranslateUi(self, calc_flx):
        _translate = QtCore.QCoreApplication.translate
        calc_flx.setWindowTitle(_translate("calc_flx", "calc_flx"))
        self.label.setText(_translate("calc_flx", "INDUTTANZA"))
        self.label_2.setText(_translate("calc_flx", "RESISTENZA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.IR), _translate("calc_flx", "I/R"))
        self.label_3.setText(_translate("calc_flx", "RESISTENZA"))
        self.label_4.setText(_translate("calc_flx", "CONDENSATORE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RC), _translate("calc_flx", "RC"))
        self.label_5.setText(_translate("calc_flx", "Vi(t)"))
        self.anteprimaGrafico.setText(_translate("calc_flx", " ANTEPRIMA GRAFICO"))
        self.grafico.setText(_translate("calc_flx", "GRAFICO"))
        self.salvataggio.setText(_translate("calc_flx", "SALVATAGGIO DATI"))
        self.cartellaSalvataggi.setText(_translate("calc_flx", "CARTELLA SALVATAGGI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calc_flx = QtWidgets.QWidget()
    ui = Ui_calc_flx()
    ui.setupUi(calc_flx)
    calc_flx.show()
    calc_flx.setFixedSize(900, 600)
    
    sys.exit(app.exec())
