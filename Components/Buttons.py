from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from variables import MEDIUM_FONT_SIZE, BIG_FONT_SIZE
from PySide6.QtCore import Slot, Signal
from utils import isNumOrDot, isEmpty
from typing import TYPE_CHECKING

from asteval import Interpreter

if TYPE_CHECKING:
    from functions import Functions
    from Components.Display import Display


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
    equalRequested = Signal()
    deleteRequested = Signal()
    allDeleteRequested = Signal()

    def __init__(self, display: 'Display',  parent: QWidget | None = None) -> None:
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

                buttonSlot = self._makeButtonFunctionSlot(button)

                button.clicked.connect(buttonSlot)
                    
    def _makeButtonFunctionSlot(self, button: Button):
        @Slot()
        def realSlot():
            if button.text() in '0123456789*+-./^':
                self._insertButtonTextToDisplay(button)

            match button.text():
                case '=':
                    self.equalRequested.emit()
                case 'C':
                    self.allDeleteRequested.emit()
                case '◀':
                    self.deleteRequested.emit()
                
        return realSlot

    def _insertButtonTextToDisplay(self, button: Button):
        buttonText = button.text()
        self.display.insert(buttonText)