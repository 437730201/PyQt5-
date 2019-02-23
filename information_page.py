# -*- coding: utf-8 -*-
# @TIME     : 2019/2/19 下午 05:26
# @Author   : Marst

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication,QGridLayout, QGroupBox,QLabel,QVBoxLayout, QWidget)

import qtawesome

class InformationPage(QWidget):

    def __init__(self, parent = None):
        super(InformationPage,self).__init__(parent)

        self.setFixedSize(850, 800)
        self.right_widget = QWidget() # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QGridLayout()

        self.right_widget_show_information()
        self.setInformationStyle()

        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格
        self.setLayout(self.right_layout)  # 设置窗口主部件
        self.setWindowTitle('informationPage')

    def right_widget_show_information(self):
        print('show information')
        self.is_right = True
        # LOGO
        logo_jpg = QPixmap("logo.png")
        self.left_label_1 = QLabel(self)
        self.left_label_1.setObjectName('logo')
        self.left_label_1.setPixmap(logo_jpg)
        self.left_label_1.setAlignment(Qt.AlignLeft)
        self.left_label_1.setFixedSize(250,300)

        self.title_icon = QLabel('Fraud Detect Tool')
        # self.title_icon.setFont(qtawesome.font('fa', 120))
        self.title_icon.setObjectName('Maintitle')
        self.title_icon.setAlignment(Qt.AlignVCenter)

        text0 = '   1.0.0 \n\n   February 15, 2019'
        text = '1. This application software is only available for maintenance and use by Apple Store...\n' \
               '2. If there is infringement, it will be sought through legal channels.......\n' \
               '\n' \
               '\n' \
               '\n'

        text2 = '1.\n' \
                '2.\n' \
                '3.\n' \

        self.text_icon0 = QLabel(text0)
        self.text_icon0.setFont(qtawesome.font('fa', 20))
        self.text_icon0.setObjectName('text')

        self.text_icon = QLabel(text)
        self.text_icon.setFont(qtawesome.font('fa', 20))
        self.text_icon.setObjectName('text')

        self.text_icon2 = QLabel(text2)
        self.text_icon2.setFont(qtawesome.font('fa', 20))
        self.text_icon2.setObjectName('text')

        icon_x = 720
        icon_y = 150
        self.title_icon2 = QGroupBox('Latest revision')
        vLayout2 = QVBoxLayout()
        vLayout2.addWidget(self.text_icon0)
        self.title_icon2.setFixedSize(icon_x, icon_y)
        self.title_icon2.setLayout(vLayout2)
        self.title_icon2.setObjectName('title')

        self.title_icon3 = QGroupBox('User Agreement')
        vLayout3 = QVBoxLayout()
        vLayout3.addWidget(self.text_icon)
        self.title_icon3.setLayout(vLayout3)
        self.title_icon3.setFixedSize(icon_x, icon_y)
        self.title_icon3.setObjectName('title')

        self.title_icon4 = QGroupBox('Privacy Policy')
        vLayout4 = QVBoxLayout()
        vLayout4.addWidget(self.text_icon2)
        self.title_icon4.setLayout(vLayout4)
        self.title_icon4.setFixedSize(icon_x, icon_y)
        self.title_icon4.setObjectName('title')

        copyright_text = 'Copyright © 2016-2019 Foxconn iDPBG NPI EERF All Rights Reserved.'
        self.copyright_icon = QLabel(copyright_text)
        self.copyright_icon.setFont(qtawesome.font('fa', 20))
        self.copyright_icon.setFixedSize(830, 30)
        self.copyright_icon.setObjectName('copyright')
        self.copyright_icon.setAlignment(Qt.AlignCenter)

        logoWidget = QWidget()
        logoLayout =  QGridLayout()
        logoLayout.addWidget(self.left_label_1,0,0,12,2)
        logoLayout.addWidget(self.title_icon,0,1,12,10)
        logoWidget.setFixedSize(830,150)
        logoWidget.setLayout(logoLayout)

        iconWidget = QWidget()
        iconLayout = QVBoxLayout()
        iconLayout.addWidget(self.title_icon2)
        iconLayout.addWidget(self.title_icon3)
        iconLayout.addWidget(self.title_icon4)
        iconWidget.setLayout(iconLayout)

        self.right_layout.addWidget(logoWidget, 0, 0)
        self.right_layout.addWidget(iconWidget, 1, 0)
        self.right_layout.addWidget(self.copyright_icon, 12, 0)

    def setInformationStyle(self):

        self.setStyleSheet("""
            QWidget{
                background:#1F2227;
        
            }
            
            QWidget#copyright{
                color:white;
                font-size:20px;
            }
            QWidget#Maintitle{
                color:white;
                font-size:45px;
            }
            QWidget#title{
                color:white;
                font-size:28px;
            }
            QWidget#text{
                color:white;
                font-size:20px;
            }
            
        """)



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    gui = InformationPage()
    gui.show()
    sys.exit(app.exec_())
