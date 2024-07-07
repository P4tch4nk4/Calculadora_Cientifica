from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
import csv
from variables import MEDIUM_FONT_SIZE, HISTORIC_PATH

class Historic(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        self.historic = self.getHistoric()


    def configStyle(self):
        self.setStyleSheet(f'font-size: {MEDIUM_FONT_SIZE}px')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

    def getHistoric(self):
        with open(HISTORIC_PATH , mode='r', newline='') as file:
            reader = csv.DictReader(file)
            accounts = list(reader)

        return accounts
        
    def saveHistoric(self):
        with open(HISTORIC_PATH, mode='w', newline='') as file:
            writer = csv.DictWriter(file, ('accounts', 'results'))
            writer.writeheader()
            writer.writerows(self.historic)

    def addHistoric(self, account, result):
        self.historic.append({'accounts': account, 'results': result})

    def updateHistoric(self):
        if len(self.historic) != 0:
            lestAccount = self.historic[-1]
            self.setText(lestAccount['accounts'] + ' = ' + lestAccount['results'])

