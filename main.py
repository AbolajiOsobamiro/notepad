import sys
from PySide6 import QtWidgets
from widget import mainWindow


app = QtWidgets.QApplication(sys.argv)

window = mainWindow(app)
window.show()
app.exec()