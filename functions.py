from asteval import Interpreter

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Components.Display import Display
    from Components.Historic import Historic
    from Components.Buttons import ButtonsGrid
    import MyWindow


class Functions:
    def __init__(self,buttonsGrid: 'ButtonsGrid',  display: 'Display', historic: 'Historic', myWindow: 'MyWindow') -> None:
        self.display = display
        self.buttonsGrid = buttonsGrid
        self.historic = historic
        self.myWindow = myWindow
        
        display.equalRequested.connect(self.equal)
        display.allDeleteRequested.connect(self.allDelete)
        display.deleteRequested.connect(self.delete)

        buttonsGrid.insertButtonTextRequested.connect(self.insertButtonText)
        buttonsGrid.equalRequested.connect(self.equal)
        buttonsGrid.allDeleteRequested.connect(self.allDelete)
        buttonsGrid.deleteRequested.connect(self.delete)

    def equal(self):
        calculate = Interpreter()
        accountText = self.display.text()
        account = accountText.replace('^', '**')
        result = str(calculate(account))


        if len(accountText) == 0:
            return
        elif result == 'None':
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

    def allDelete(self):
        self.display.clear()
        self.display.setText('')
        self.display.setPlaceholderText('')

    def delete(self):
        self.display.backspace()

        if len(self.display.text()) == 0:
            self.display.setText('')
            self.display.setPlaceholderText('')

    def _showError(self, text, info):
        msgBox = self.myWindow.makeMsg()
        msgBox.setText(text)
        msgBox.setInformativeText(info)
        msgBox.setWindowTitle('Error')
        msgBox.setIcon(msgBox.Icon.Warning)
        msgBox.exec()

    def insertButtonText(self, button):
        buttonText = button.text()
        self.display.insert(buttonText)