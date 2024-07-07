from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMessageBox

class MyWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.myCentralWidget = QWidget()
        self.myLayout = QVBoxLayout()

        self.myCentralWidget.setLayout(self.myLayout)
        self.setCentralWidget(self.myCentralWidget)

        self.setWindowTitle('Calculadora')

    def addToWidgetVLayout(self, widget:QWidget):
        self.myLayout.addWidget(widget)

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
        print(self.width(), self.height())

    def makeMsg(self) -> QMessageBox:
        return QMessageBox(self)
