from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication, QSlider, QFileDialog, QLabel
from ui_notepad import Ui_Padnote  
from spell_checker import SpellCheckedTextEdit


class mainWindow(QMainWindow, Ui_Padnote):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)

        self.app = app
        self.setWindowTitle("PadNote")

        self.spell_checked_text_edit = SpellCheckedTextEdit()
        self.verticalLayout.replaceWidget(self.textEdit, self.spell_checked_text_edit)
        self.textEdit.deleteLater()
        self.textEdit = self.spell_checked_text_edit



        # Connect menu actions
        self.actionquit.triggered.connect(self.quit)
        self.actioncopy.triggered.connect(self.copy)
        self.actioncut.triggered.connect(self.cut)
        self.actionpaste.triggered.connect(self.paste)
        self.actionundo.triggered.connect(self.undo)
        self.actionredo.triggered.connect(self.redo)
        self.actionhelp.triggered.connect(self.help)
        self.actionSave.triggered.connect(self.save_file)
        self.actionSaveas.triggered.connect(self.save_file_as)
        self.actionAbout.triggered.connect(self.about)
        self.actionAboutQt.triggered.connect(self.aboutQt)

        # Set shortcuts
        self.actioncopy.setShortcut("Ctrl+C")
        self.actioncut.setShortcut("Ctrl+X")
        self.actionpaste.setShortcut("Ctrl+V")
        self.actionundo.setShortcut("Ctrl+Z")
        self.actionredo.setShortcut("Ctrl+Y")
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSaveas.setShortcut("Ctrl+Shift+S")

        # Status bar elements
        self.char_count_label = QLabel("Characters: 0", self)
        self.word_count_label = QLabel("Words: 0", self)

        # Font size slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(20)
        self.slider.setMaximum(100)
        self.slider.setValue(20)
        self.slider.valueChanged.connect(self.update_font_size)

        self.update_font_size(self.slider.value())

        # Add widgets to the status bar
        self.statusBar().addWidget(self.char_count_label)
        self.statusBar().addWidget(self.word_count_label)
        self.statusBar().addWidget(self.slider)

        # Connect text edit signals
        self.textEdit.textChanged.connect(self.update_counts)

        self.current_file = None

    def update_counts(self):
        text = self.textEdit.toPlainText()
        char_count = len(text)
        word_count = len(text.split())
        self.char_count_label.setText(f"Characters: {char_count}")
        self.word_count_label.setText(f"Words: {word_count}")

    def update_font_size(self, value):
        font = self.textEdit.font()
        font.setPointSize(value)
        self.textEdit.setFont(font)

    def quit(self):
        self.app.quit()

    def copy(self):
        self.textEdit.copy()

    def cut(self):
        self.textEdit.cut()

    def paste(self):
        self.textEdit.paste()

    def undo(self):
        self.textEdit.undo()

    def redo(self):
        self.textEdit.redo()

    def help(self):
        QMessageBox.information(self, "Help", "This is a simple notepad application with spell checking.")

    def about(self):
        QMessageBox.information(self, "About", "PadNote v1.0\nA simple notepad application with spell checking.")

    def aboutQt(self):
        QApplication.aboutQt()

    def save_file(self):
        if self.current_file is None:
            self.save_file_as()
        else:
            self.write_to_file(self.current_file)

    def save_file_as(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options 
        )
        if file_path:
            self.current_file = file_path
            self.write_to_file(file_path)
            self.setWindowTitle(f"PadNote - {self.current_file}")

    def write_to_file(self, file_path):
        text = self.textEdit.toPlainText()
        try:
            with open(file_path, 'w') as file:
                file.write(text)
            self.statusBar().showMessage("File saved successfully!", 2000)
        except Exception as e:
            self.statusBar().showMessage(f"Error saving file: {e}", 2000)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = mainWindow(app)
    window.show()
    sys.exit(app.exec())