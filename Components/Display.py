from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt
from variables import BIG_FONT_SIZE

TEXT_MARGIN = 10

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        self.setPlaceholderText('')

    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins( *[TEXT_MARGIN for _ in range(4)])
