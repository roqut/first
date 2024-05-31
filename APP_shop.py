import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import psycopg2

font = QFont()
font.setPointSize(36)
font.setBold(True)

font2 = QFont()
font2.setPointSize(20)

font3 = QFont()
font3.setPointSize(14)

font4 = QFont()
font4.setPointSize(11)


class DataBase:
    def __init__(self, dbname, user, password):
        self.con = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host='192.168.8.56',
            port='5432'
        )
        self.cur = self.con.cursor()

    def execute(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()

    def commit(self):
        self.con.commit()

    def close(self):
        self.con.close()

class Frame1(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        label_main = QLabel(' SHOP', self)
        label_main.setMinimumSize(200, 100)
        label_main.setFont(font)
        label_main.setAlignment(Qt.AlignCenter)

        label_login = QLabel('Введите логин:', self)
        label_login.setMinimumSize(100, 50)

        label_login.setFont(font3)

        self.input_login = QLineEdit(self)
        self.input_login.setMinimumSize(300, 60)
        self.input_login.setMaximumSize(300, 60)
        self.input_login.setFont(font2)

        label_password = QLabel('Введите пароль:', self)
        label_password.setMinimumSize(100, 50)
        label_password.setFont(font3)

        self.input_password = QLineEdit(self)
        self.input_password.setMinimumSize(300, 60)
        self.input_password.setMaximumSize(300, 60)
        self.input_password.setFont(font2)

        self.error_label = QLabel('', self)
        self.error_label.setMinimumSize(100, 50)
        self.error_label.setFont(font4)
        self.error_label.setStyleSheet('color: red')

        button = QPushButton('BUTTON', self)
        button.setMinimumSize(200, 100)
        button.clicked.connect(self.come_to_frame2)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(label_main)
        self.main_layout.addWidget(label_login)
        self.main_layout.addWidget(self.input_login)
        self.main_layout.addWidget(label_password)
        self.main_layout.addWidget(self.input_password)
        self.main_layout.addWidget(self.error_label)
        self.main_layout.addWidget(button)
        self.main_layout.setAlignment(Qt.AlignCenter)

    def come_to_frame2(self):
        #db = DataBase('safu', 'afu_main_admin', 'Ar')
        #t = db.execute('select login, password from safu_admins_auth')
        table = [('vish', 'f61CT5dW'), ('vshent', 'E82sYprb'), ('vshsgnmk', 'bpc3hXb4'),
                 ('vsheup', 'A5kC3za7'), ('vshitas', '1qU0vR9a'), ('vshppfk', '8DrgZWv9'),
                 ('vsheng', 'hoFQ3a4U'), ('vshrmt', '4nANr0gF'), ('vshitas', '111')]
        #db.close()
        text1 = self.input_login.text()
        text2 = self.input_password.text()

        if (text1, text2) in table:
            self.parent().setCurrentIndex(1)
        else:
            self.error_label.setText('Неверный логин или пароль!')

class Frame2(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        info = [('pictures/logo.png', 'decription1'), ('image2', 'decription2'), ('image3', 'decription3'),
                ('image4', 'decription4'), ('image5', 'decription5'), ('image6', 'decription6'),
                ('image4', 'decription4'), ('image5', 'decription5'), ('image6', 'decription6'),
                ('image4', 'decription4'), ('image5', 'decription5'), ('image6', 'decription6'),
                ('image4', 'decription4'), ('image5', 'decription5'), ('image6', 'decription6'),
                ('image4', 'decription4'), ('image5', 'decription5'), ('image6', 'decription6'),
                ('image4', 'decription4'), ('image5', 'decription5'), ('image6', 'decription6'),
                ('image4', 'decription4'), ('image5', 'decription5'), ('image6', 'decription6')]

        button = QPushButton('<---')
        button.setFixedSize(500, 50)
        button.setFont(font2)
        button.clicked.connect(self.back_to_frame2)

        scroll_area = QScrollArea()
        scroll_area.setMinimumSize(1000, 500)
        scroll_area.setMaximumSize(1000, 500)
        scroll_area.setWidgetResizable(True)

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout()

        for image, description in info:
            image_label = QLabel()
            image_label.setPixmap(QPixmap(image))
            image_label.setScaledContents(True)
            image_label.setFixedSize(60, 60)

            description_label = QLabel(description)
            description_label.setWordWrap(True)

            h_layout = QHBoxLayout()
            h_layout.addWidget(image_label)
            h_layout.addWidget(description_label)

            scroll_layout.addLayout(h_layout)

        scroll_content.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_content)

        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll_area)
        main_layout.addWidget(button)

        self.setLayout(main_layout)

    def back_to_frame2(self):
        self.parent().setCurrentIndex(0)

class APP(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 150, 1200, 800)

        self.Frame1 = Frame1()
        self.Frame2 = Frame2()

        self.addWidget(self.Frame1)
        self.addWidget(self.Frame2)

        self.setCurrentIndex(1)

if '__main__' == __name__:
    MAIN = QApplication(sys.argv)
    ex = APP()
    ex.show()
    sys.exit(MAIN.exec())