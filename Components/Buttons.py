from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from variables import MEDIUM_FONT_SIZE, BIG_FONT_SIZE
from PySide6.QtCore import Slot
from utils import isNumOrDot, isEmpty
from typing import TYPE_CHECKING

from asteval import Interpreter

if TYPE_CHECKING:
    from Components.Display import Display
    from Components.Historic import Historic
    import MyWindow
    from PySide6.QtWidgets import QMessageBox


class Button(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configStyle()
        self.value = None

    def configStyle(self):
        font = self.font()
        font.setPixelSize(BIG_FONT_SIZE)
        self.setFont(font)

        self.setMinimumSize(110, 80)

class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', historic: 'Historic', myWindow: 'MyWindow',  parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '='],
        ]
        self.display = display
        self._makeGrid()
        self.historic = historic
        self.myWindow = myWindow

    def _makeGrid(self):
        for row, values_row in enumerate(self._gridMask):
            for columns, button_text in enumerate(values_row):
                button = Button(button_text)
                button.value = button_text

                if not isNumOrDot(button_text):
                    button.setProperty('cssClass', 'specialButton')
                    
                if(button_text == '0'):
                    self.addWidget(button, row, columns, 1, 1)
                else:
                    self.addWidget(button, row, columns)

                buttonSlot = self._makeButtonFunctionSlot(
                    self._insertButtonTextToDisplay,
                    button,
                )

                button.clicked.connect(buttonSlot)
                    
    def _makeButtonFunctionSlot(self, func, button: Button):
        @Slot()
        def realSlot():
            if button.text() in '0123456789*+-./^':
                self._insertButtonTextToDisplay(button)

            match button.text():
                case '=':
                    self.equalFunction()
                case 'C':
                    self.allDeleteFunction()
                    self.display.setText('')
                    self.display.setPlaceholderText('')
                case '◀':
                    self.deleteFunction()
                
        return realSlot

    def equalFunction(self):
        calculate = Interpreter()
        accountText = self.display.text()
        account = accountText.replace('^', '**')
        result = str(calculate(account))

        if result == 'None':
            self.display.setText('')
            self.display.setPlaceholderText('Account Error')
            self._showError('Account Error', 'The value entered cannot be calculated')
        elif len(result) > 18:
            self.display.setText('')
            self.display.setPlaceholderText('OverFlow Error')
            self._showError('OverFlow Error', 'The result was a very large number')
        else:
            self.display.setText(result)
            self.historic.addHistoric(accountText, result)
            self.historic.saveHistoric()
            self.historic.updateHistoric()

    def allDeleteFunction(self):
        self.display.clear()

    def deleteFunction(self):
        self.display.setText(self.display.text()[0:-1])

    def _insertButtonTextToDisplay(self, button: Button):
        buttonText = button.text()
        self.display.insert(buttonText)

    def _showError(self, text, info):
        msgBox = self.myWindow.makeMsg()
        msgBox.setText(text)
        msgBox.setInformativeText(info)
        msgBox.setWindowTitle('Error')
        msgBox.setIcon(msgBox.Icon.Warning)
        msgBox.exec()