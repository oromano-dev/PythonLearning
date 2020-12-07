from PySide2 import QtWidgets
import currency_converter

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.curConverter = currency_converter.CurrencyConverter()
        self.setWindowTitle("Convertisseur de devises")
        self.setup_ui()
        self.set_default_values()
        self.setup_connections()

    def setup_ui(self):
        self.layout = QtWidgets.QHBoxLayout(self)
        self.cbb_devisesFrom = QtWidgets.QComboBox()
        self.spn_montant = QtWidgets.QSpinBox()
        self.cbb_devisesTo = QtWidgets.QComboBox()
        self.spn_montantConverti = QtWidgets.QSpinBox()
        self.btn_inverser = QtWidgets.QPushButton("Inverser devises")

        self.layout.addWidget(self.cbb_devisesFrom)
        self.layout.addWidget(self.spn_montant)
        self.layout.addWidget(self.cbb_devisesTo)
        self.layout.addWidget(self.spn_montantConverti)
        self.layout.addWidget(self.btn_inverser)

    def set_default_values(self):
        self.cbb_devisesFrom.addItems(sorted(self.curConverter.currencies))
        self.cbb_devisesFrom.setCurrentText("CHF")

        self.cbb_devisesTo.addItems(sorted(self.curConverter.currencies))
        self.cbb_devisesTo.setCurrentText("EUR")

        self.spn_montant.setRange(1, 1000000)
        self.spn_montantConverti.setRange(1, 1000000)
        self.spn_montant.setValue(1)
        self.spn_montantConverti.setValue(1)

    def setup_connections(self):
        self.cbb_devisesFrom.activated.connect(self.compute)
        self.cbb_devisesTo.activated.connect(self.compute)

        self.spn_montant.valueChanged.connect(self.compute)
        self.btn_inverser.clicked.connect(self.inverser_devises)

    def compute(self):
        montant = self.spn_montant.value()
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()
        resultat = self.curConverter.convert(montant, devise_from, devise_to)

        # print("montant à convertir: ", str(montant))
        # print("Devise de base: ", devise_from)
        # print("Devise de conversion: ", devise_to)
        # print(f"Conversion de {montant} {devise_from} en {devise_to}: {resultat}")
        self.spn_montantConverti.setValue(resultat)

    def inverser_devises(self):
        # print("Inverser devise")
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()
        
        self.cbb_devisesFrom.setCurrentText(devise_to)
        self.cbb_devisesTo.setCurrentText(devise_from)

        self.compute()

myApp = QtWidgets.QApplication([])
win = App()
win.resize(150, 200)
win.show()

myApp.exec_()
