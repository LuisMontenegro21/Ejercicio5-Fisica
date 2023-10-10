
import Functions
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QGraphicsScene,
    QGraphicsEllipseItem
)
from PyQt5.QtGui import QColor, QBrush, QPen
from PyQt5.QtCore import QRectF
from PyQt5 import uic


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("CapacitanceUI.ui", self)
        items = ["","Completo","Mitad"]
    

        self.cmbDielectric.addItems(items)

        self.flag = 0
        self.scene = QGraphicsScene(self)

        self.scene = QGraphicsScene(self)
        self.gvMainImage.setScene(self.scene)

        self.txbDimension3.setVisible(False)
        self.lblDimension3.setVisible(False)
        self.txfChargeFree.setVisible(False)
        self.txfChargeBonded.setVisible(False)
        self.lblFreeCharge.setVisible(False)
        self.lblBondedCharge.setVisible(False)

        #Button listeners para hacer uso de las implementaciones en UI
        self.rbParallel.clicked.connect(self.rbParallelClicked)
        self.rbSphere.clicked.connect(self.rbSphereClicked)
        self.rbCylinder.clicked.connect(self.rbCylinderClicked)
        self.cbDielectric.clicked.connect(self.cbDielectricClicked)
        self.btnLoad.clicked.connect(self.btnLoadClicked)
        self.btnExit.clicked.connect(self.close)

        # Initialize instance variables
        self.dimension = 0.0
        self.length = 0.0
        self.charge = 0.0

    def btnLoadClicked(self):
        
        #Declaración de variables útiles
        dataItems  = ["","full","half"]
        C_0 = C = Q = Q_0 = U = 0
        sigma = sigma_i = []

        #Estética del programa
        self.cleaningData()
        if self.cbDielectric.isChecked() and self.cmbDielectric.currentText() == "":
            self.showErrorMessageBox("No se ha especificado la distribución del dieléctrico")

        #Toma de datos para realizar los cálculos
        d1 = float(self.txbDimension1.text())
        d2 = float(self.txbDimension2.text())
        d3 = float(self.txbDimension3.text())
        d = float(self.txbDistance.text())
        v = float(self.txbVoltage.text())
        dielectric = "y" if self.cbDielectric.isChecked() else "n"
        ref= self.cmbDielectric.currentIndex()
        quantity = dataItems[ref]

        #Se selecciona la accion a realizar según las banderas (var. flag)
        if self.flag == 0:
            #Confirmation of selection
            self.showErrorMessageBox("No se ha seleccionado el tipo de capacitor")

        #Capacitor de placas paralelas
        elif self.flag == 1:
            C_0 = Functions.capacitanceParallel(d1, d2, d)
            C = Functions.capacitanceParallelDielectric(d1, d2, d, dielectric, quantity)
            Q = Functions.capacitanceCharge(C_0, v)
            Q_0 = Functions.capacitanceCharge(C_0, v)
            U = Functions.storedEnergy(C, C_0, v, quantity)

            #Dieléctrico (Placas paralelas)
            if(dielectric == "y"):
                print(Q_0)
                sigma = Functions.freeChargeParallel(Q_0, d1, d2, quantity)
                sigma_i = Functions.bondedChargeParallel(Q_0, d1, d2, quantity)
            else:
                C = C_0
                print(C, C_0)
                Q = Q_0 

            self.drawParallelCapacitor(d1, d2, d, dielectric, quantity)

        #Capacitor de esfera
        elif self.flag == 2:
            C_0 = Functions.capacitanceSphere(d1, d2)
            C = Functions.capacitanceSphereDielectric(d1, d2, dielectric, quantity)
            Q = Functions.capacitanceCharge(C_0, v)
            Q_0 = Functions.capacitanceCharge(C_0, v)
            U = Functions.storedEnergy(C, C_0, v, quantity)

            #Dieléctrico (Esfera)
            if(dielectric == "y"):
                sigma = Functions.freeChargeSphere(Q_0, d1, d2, quantity)
                sigma_i = Functions.bondedChargeSphere(Q_0, d1, d2, quantity)
            else:
                C = C_0
                Q = Q_0

            self.drawTransversalCut(d1, d2, dielectric, quantity)

        #Capacitor de cilindro
        elif self.flag == 3:
            C_0 = Functions.capacitanceCylinder(d1, d2, d3)
            C = Functions.capacitanceCylinderDielectric(d1, d2, d3, dielectric, quantity)
            Q = Functions.capacitanceCharge(C_0, v)
            Q_0 = Functions.capacitanceCharge(C_0, v)
            U = Functions.storedEnergy(C, C_0, v, quantity)

            #Dieléctrico (Cilindro)
            if(dielectric == "y"):
                sigma = Functions.freeChargeCylinder(Q_0, d1, d2, d3, quantity)
                sigma_i = Functions.bondedChargeCylinder(Q_0, d1, d2, d3, quantity)
            else:
                C = C_0
                Q = Q_0

            self.drawTransversalCut(d1, d2, dielectric, quantity)
    
        #Envio de resultados para mostrar en interfaz
        if self.flag != 0:
            self.txfCapacitance.setText(str(f"{C:.2e}"))
            self.txfCharge.setText(f"{Q:.2e}")
            print(Q)
            self.txfEnergy.setText(f"{U:.2e}")
            self.txfChargeFree.setText(str([0 if num == 0 else format(num, ".2e") for num in sigma]))
            self.txfChargeBonded.setText(str([0 if num == 0 else format(num, ".2e") for num in sigma_i]))

    def showErrorMessageBox(self, message):
        QMessageBox.critical(self, "Error", message, QMessageBox.Ok)

    def cleaningData(self):
        self.txfCapacitance.setText("")
        self.txfEnergy.setText("")
        self.txfCharge.setText("")
        self.txfChargeBonded.setText("")
        self.txfChargeFree.setText("")


    def rbParallelClicked(self):
        self.txbDimension3.setVisible(False)
        self.lblDimension3.setVisible(False)
        self.lblDistance.setVisible(True)
        self.txbDistance.setVisible(True)

        self.flag = 1
        self.lblDimension1.setText("Altura (m)")
        self.lblDimension2.setText("Largo (m)")

    def rbSphereClicked(self):
        self.txbDimension3.setVisible(False)
        self.lblDimension3.setVisible(False)
        self.lblDistance.setVisible(False)
        self.txbDistance.setVisible(False)

        self.flag = 2
        self.lblDimension1.setText("Radio exterior (m)")
        self.lblDimension2.setText("Radio interior (m)")

    def rbCylinderClicked(self):
        self.txbDimension3.setVisible(True)
        self.lblDimension3.setVisible(True)
        self.lblDistance.setVisible(False)
        self.txbDistance.setVisible(False)
        
        self.flag = 3
        self.lblDimension1.setText("Radio exterior (m)")
        self.lblDimension2.setText("Radio interior (m)")
        self.lblDimension3.setText("Largo (m)")

    def cbDielectricClicked(self):
        value = self.cbDielectric.isChecked()
        self.cmbDielectric.setEnabled(value)
        self.txfChargeFree.setVisible(value)
        self.txfChargeBonded.setVisible(value)
        self.lblFreeCharge.setVisible(value)
        self.lblBondedCharge.setVisible(value)
        self.lblDistribution.setEnabled(value)
        self.cmbDielectric.setCurrentIndex(1 if value else 0)

    def drawParallelCapacitor(self, d1, d2, d, dielectric, quantity):
        self.scene.clear() 

        scale_factor = 5

        d1 *= scale_factor
        d2 *= scale_factor
        d *= scale_factor

        pen = QPen(QColor(0, 0, 0))
        brush = QBrush(QColor(255, 255, 255))

        self.scene.addRect(0, 0, d2, d1, pen, brush)
        
        self.scene.addRect(0, d1 + d, d2, d1, pen, brush)

        if dielectric == "y":
            dielectric_brush = QBrush(QColor(173, 216, 230))  
            dielectric_length = d2 if quantity == "full" else d2 / 2
            self.scene.addRect(0, d1, dielectric_length, d, pen, dielectric_brush)

    def drawTransversalCut(self, r_outer, r_inner, dielectric, quantity):
        self.scene.clear() 

        scale_factor = 5  

        r_outer_scaled = r_outer * scale_factor
        r_inner_scaled = r_inner * scale_factor


        pen = QPen(QColor(0, 0, 0))
        brush_no_fill = QBrush(QColor(255, 255, 255))
        brush_fill = QBrush(QColor(173, 216, 230))  

        outer_rect = QRectF(-r_outer_scaled, -r_outer_scaled, 2*r_outer_scaled, 2*r_outer_scaled)
        inner_rect = QRectF(-r_inner_scaled, -r_inner_scaled, 2*r_inner_scaled, 2*r_inner_scaled)

        if dielectric == "y":
            if quantity == "full":
                self.scene.addEllipse(outer_rect, pen, brush_fill)
            elif quantity == "half":
                
                self.scene.addEllipse(outer_rect, pen, brush_no_fill)
                
                half_ellipse = QGraphicsEllipseItem(outer_rect)
                half_ellipse.setStartAngle(0)
                half_ellipse.setSpanAngle(-180*16)
                half_ellipse.setPen(pen)
                half_ellipse.setBrush(brush_fill)
                self.scene.addItem(half_ellipse)
        else:
            self.scene.addEllipse(outer_rect, pen, brush_no_fill)

        self.scene.addEllipse(inner_rect, pen, brush_no_fill)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()