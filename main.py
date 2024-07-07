import sys
from MyWindow import MyWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from styles import setupTheme
from Components.Historic import Historic
from Components.Display import Display
from Components.Buttons import ButtonsGrid



if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme()
    window = MyWindow()
    icon = QIcon(str(WINDOW_ICON_PATH))

    # Historic
    historic = Historic('')
    window.addToWidgetVLayout(historic)

    # Display
    display = Display()
    window.addToWidgetVLayout(display)
    historic.updateHistoric()

    # ButtonsGrid
    buttonsGrid = ButtonsGrid(display, historic, window)
    window.myLayout.addLayout(buttonsGrid)

    # Icon
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Configs
    window.adjustFixedSize()
    window.show()
    app.exec()