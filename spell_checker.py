from PySide6.QtGui import QTextCursor, QColor, QTextCharFormat
from PySide6.QtWidgets import QTextEdit, QWidget, QVBoxLayout
from spellchecker import SpellChecker


class SpellCheckedTextEdit(QTextEdit):
    def __init__(self):
        super().__init__()
        self.spell_checker = SpellChecker()
        self.textChanged.connect(self.check_spelling)

    def check_spelling(self):
        self.blockSignals(True)

        cursor = self.textCursor()
        cursor.beginEditBlock()

        text = self.toPlainText()
        words = text.split()
        misspelled = self.spell_checker.unknown(words)

    
        fmt = QTextCharFormat()
        fmt.setUnderlineStyle(QTextCharFormat.NoUnderline)
        cursor.select(QTextCursor.Document)
        cursor.setCharFormat(fmt)

        # Apply spell-check underline formatting to misspelled words
        fmt.setUnderlineStyle(QTextCharFormat.SpellCheckUnderline)
        fmt.setUnderlineColor(QColor("red"))

        for word in misspelled:
            # Find all occurrences of the misspelled word efficiently using find()
            highlight_cursor = self.document().find(word)
            while highlight_cursor.hasSelection():
                highlight_cursor.mergeCharFormat(fmt)
                highlight_cursor = self.document().find(word, highlight_cursor)  # Start from next position

        cursor.endEditBlock()

        self.blockSignals(False)



class textEdit (QWidget):
    def __init__(self,app):
        super().__init__()

        self.app = app
        self.setWindowTitle("QlineEdit")

        self.text_edit = SpellCheckedTextEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)

        self.setLayout(layout)