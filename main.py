# -*- coding: utf-8 -*-
# @TIME     : 2019/2/19 下午 01:45
# @Author   : Marst


from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtWidgets import (QApplication,QDialog, QHBoxLayout, QLabel,QListView, QListWidget,
                             QListWidgetItem,QStackedWidget, QVBoxLayout, QWidget)

from npo_page import NPoPage
from setting_page import SettingPage
from information_page import InformationPage

class FraudFrame(QDialog):
    version = 'Fraud Detect Tool 1.0.0'

    def __init__(self, parent=None):
        super(FraudFrame, self).__init__(parent)

        self.contentsWidget = QListWidget()
        self.contentsWidget.setViewMode(QListView.IconMode)
        self.contentsWidget.setIconSize(QSize(120, 110))
        self.contentsWidget.setMovement(QListView.Static)
        self.contentsWidget.setMaximumWidth(130)
        self.contentsWidget.setSpacing(10)
        self.contentsWidget.setObjectName('left_widget')

        self.pagesWidget = QStackedWidget()
        self.pagesWidget.addWidget(NPoPage())
        self.pagesWidget.addWidget(NPoPage())
        self.pagesWidget.addWidget(NPoPage())
        self.pagesWidget.addWidget(SettingPage())
        self.pagesWidget.addWidget(InformationPage())
        self.pagesWidget.setObjectName('left_widget')

        self.logoLabel()

        vLayout = QVBoxLayout()
        vWidget = QWidget()
        vWidget.setObjectName('vWidget')
        vLayout.addWidget(self.left_label_1)
        vLayout.addWidget(self.contentsWidget)
        vWidget.setLayout(vLayout)

        horizontalLayout = QHBoxLayout()
        horizontalLayout.addWidget(vWidget)
        horizontalLayout.addWidget(self.pagesWidget, 1)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(horizontalLayout)
        mainLayout.addStretch(1)
        mainLayout.addSpacing(1)

        self.setStyleBetter()
        self.setLayout(mainLayout)
        self.createIcons()
        self.setWindowTitle(self.version)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)


    def changePage(self, current, previous):
        if not current:
            current = previous

        self.pagesWidget.setCurrentIndex(self.contentsWidget.row(current))

    def logoLabel(self):
        # # LOGO
        logo_jpg = QPixmap("logo.png")
        self.left_label_1 = QLabel(self)
        self.left_label_1.setObjectName('logo')
        self.left_label_1.setPixmap(logo_jpg)
        self.left_label_1.setAlignment(Qt.AlignCenter)

    def createIcons(self):

        poButton = QListWidgetItem(self.contentsWidget)
        # poButton.setIcon(QIcon('PO.jpg'))
        poButton.setIcon(QIcon('PO.png'))
        poButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        nPoButton = QListWidgetItem(self.contentsWidget)
        nPoButton.setIcon(QIcon('NPO.png'))
        nPoButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        moreButton = QListWidgetItem(self.contentsWidget)
        moreButton.setIcon(QIcon('MORE.png'))
        moreButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        moreButton.setToolTip('这是MORE按钮')

        settingButton = QListWidgetItem(self.contentsWidget)
        settingButton.setIcon(QIcon('Setting.png'))
        settingButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        settingButton.setToolTip('这是设定按钮')

        informationButton = QListWidgetItem(self.contentsWidget)
        informationButton.setIcon(QIcon('information.png'))
        informationButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        informationButton.setToolTip('这是工具信息按钮')
        # 为contentsWidget界面切换添加changePage响应
        self.contentsWidget.currentItemChanged.connect(self.changePage)

    def setStyleBetter(self):
        """
            @todo  border: 2px outset red
        :return:
        """

        # set style
        self.setStyleSheet(
            """ 
            QWidget{
            background:#15191C;
            }
                """)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    dialog = FraudFrame()
    sys.exit(dialog.exec_())
