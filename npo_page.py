# -*- coding: utf-8 -*-
# @TIME     : 2019/2/19 下午 02:38
# @Author   : Marst

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication,QPlainTextEdit,QGridLayout, QGroupBox,
                             QHBoxLayout, QLabel,QPushButton,QVBoxLayout, QWidget)

class NPoPage(QWidget):

    def __init__(self, parent = None):
        super(NPoPage,self).__init__(parent)
        # super().__init__()
        self.setFixedSize(850, 800)
        self.right_widget = QWidget() # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QGridLayout()
        self.right_layout.setSpacing(2)
        self.right_widget_show_npo()
        self.right_widget.setLayout(self.right_layout) # 设置右侧部件布局为网格

        self.setLayout(self.right_layout)  # 设置窗口主部件
        self.setWindowTitle('NPoPage')

    def right_widget_show_npo(self):
        npo_jpg = QPixmap("npo_phone.jpg")
        self.npo_image = QLabel(self)
        self.npo_image.setObjectName('npo_jpg')
        self.npo_image.setPixmap(npo_jpg)
        self.npo_image.setAlignment(Qt.AlignCenter)
        self.npo_image.setFixedSize(830, 480)

        text_edit_x = 360
        text_edit_y = 150
        # Add text field
        self.b = QPlainTextEdit(self)
        self.b.setObjectName('textEdit')
        self.b_text = '...'
        self.b.insertPlainText(self.b_text)
        self.b.setFixedSize(text_edit_x,text_edit_y)

        self.b2_text = "Connect….\n" \
                       "Capture...\n" \
                       "Idnetification\n"

        self.b2 = QPlainTextEdit(self)
        self.b2.insertPlainText(self.b2_text)
        self.b2.setObjectName('textEdit')
        self.b2.setFixedSize(text_edit_x, text_edit_y)
        # Run button
        self.run_button = QPushButton('Run')
        self.run_button.setObjectName('run_button')
        self.run_button.setFixedSize(830, 60)

        pox_x = 1
        pox_y = 0
        hLayout = QHBoxLayout()

        packageGroup = QGroupBox("Identification")
        vLayout = QVBoxLayout()
        vLayout.addWidget(self.b)
        packageGroup.setLayout(vLayout)
        packageGroup.setObjectName('textTitle')

        packageGroup2 = QGroupBox("Progress")
        vLayout2 = QVBoxLayout()
        vLayout2.addWidget(self.b2)
        packageGroup2.setLayout(vLayout2)
        packageGroup2.setObjectName('textTitle')

        hLayout_widget = QWidget()
        hLayout.addWidget(packageGroup)
        hLayout.addSpacing(5)
        hLayout.addWidget(packageGroup2)
        hLayout_widget.setLayout(hLayout)

        self.right_layout.addWidget(self.npo_image,pox_y,pox_x)
        self.right_layout.addWidget(hLayout_widget,pox_y+1, pox_x)
        self.right_layout.addWidget(self.run_button,pox_y+2, pox_x)

        self.setStyleSheet(
            """
            QWidget{
                background:#1F2227;
            }
            
            QWidget#textTitle{
                color:white;
                font-size:30px;
                font-weight:700;
            }

            QWidget#textEdit{
                color:white;
                background:#292E32;
                font-size:15px;
            }
            QPushButton#run_button{
                color:white;
                background:#444444;
                font-size:38px;
                font-weight:680;
                border-radius:5px;
            }
            QPushButton#run_button:hover{background:green;}
            QPushButton#run_button:pressed{background:#5D91F4;}
            """)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    gui = NPoPage()
    gui.show()
    sys.exit(app.exec_())
