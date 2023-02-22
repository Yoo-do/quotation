from PyQt5.QtWidgets import  QPushButton, QWidget, QApplication, QBoxLayout, QToolBar, QMainWindow, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys
import requests


class MainWindow(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.api_init()
        self.setup_ui()


        sys.exit(self.app.exec_())


    def api_init(self):
        self.api = 'https://api.lovelive.tools/api/SweetNothings/1/Serialization/Text?genderType='
        self.gender_type = 'M'

    def get_response(self):
        response = requests.get(self.api+self.gender_type)
        return response.text

    def set_gendertype(self, gendertype: str):
        self.gender_type = gendertype
        if gendertype == 'M':
            self.setWindowTitle('渣男语录❤')
        if gendertype == 'F':
            self.setWindowTitle('茶言茶语🍵')

    def setup_ui(self):
        self.resize(400, 300)
        self.show()
        self.setWindowTitle('渣男语录❤')
        self.setWindowIcon(QIcon())


        self.toolbar = QToolBar(self)
        self.toolbar.show()
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)


        male_btn = QPushButton('渣男语录❤', self.toolbar)
        male_btn.show()
        male_btn.clicked.connect(lambda: self.set_gendertype('M'))
        self.toolbar.addWidget(male_btn)
        female_btn = QPushButton('茶言茶语🍵', self.toolbar)
        female_btn.show()
        female_btn.clicked.connect(lambda: self.set_gendertype('F'))
        self.toolbar.addWidget(female_btn)

        self.subwindow = QWidget(self)
        self.subwindow.show()
        self.setCentralWidget(self.subwindow)

        subwindow_layout = QBoxLayout(QBoxLayout.TopToBottom, self.subwindow)

        self.show_text_edit = QTextEdit(self.subwindow)
        self.show_text_edit.setReadOnly(True)
        self.show_text_edit.show()
        subwindow_layout.addWidget(self.show_text_edit)

        btns_layout = QBoxLayout(QBoxLayout.LeftToRight)
        subwindow_layout.addLayout(btns_layout)

        def like():
            try:
                self.show_text_edit.setText(self.show_text_edit.toPlainText() + '❤')
            except Exception as e:
                self.show_text_edit.setText(e.__str__())

        self.like_btn = QPushButton('喜欢', self.subwindow)
        self.like_btn.show()
        self.like_btn.clicked.connect(like)
        btns_layout.addWidget(self.like_btn)

        def show_text():
            try:
                self.show_text_edit.setText(self.get_response())
            except Exception as e:
                self.show_text_edit.setText(e.__str__())

        self.next_btn = QPushButton('再来一条', self.subwindow)
        self.next_btn.show()
        self.next_btn.clicked.connect(show_text)
        btns_layout.addWidget(self.next_btn)

        def top():
            try:
                self.show_text_edit.setText(self.show_text_edit.toPlainText() + '👎')
            except Exception as e:
                self.show_text_edit.setText(e.__str__())

        self.top_btn = QPushButton('不喜欢', self.subwindow)
        self.top_btn.show()
        self.top_btn.clicked.connect(top)
        btns_layout.addWidget(self.top_btn)

if __name__ == '__main__':
    mainwindow = MainWindow()