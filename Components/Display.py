from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from variables import BIG_FONT_SIZE

TEXT_MARGIN = 10

class Display(QLineEdit):
    equalRequested = Signal()
    deleteRequested = Signal()
    allDeleteRequested = Signal()
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        self.setPlaceholderText('')

    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins( *[TEXT_MARGIN for _ in range(4)])

    def keyPressEvent(self, event: QKeyEvent) -> None:
        key = event.key()
        keyText = event.text()

        if key in (Qt.Key.Key_Enter, Qt.Key.Key_Return):
            self.equalRequested.emit()
        elif key in (Qt.Key.Key_Backspace, Qt.Key.Key_Delete):
            self.deleteRequested.emit()
            return event.ignore()
        elif key in (Qt.Key.Key_Escape, Qt.Key.Key_C):
            self.allDeleteRequested.emit()
        elif keyText in '1234567890-+*.^/':
            self.insert(keyText)