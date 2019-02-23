# -*- coding: utf-8 -*-
# @TIME     : 2019/2/19 下午 04:12
# @Author   : Marst
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QGridLayout, QGroupBox,
                             QLineEdit,QPushButton,QVBoxLayout, QWidget)

class SettingPage(QWidget):

    def __init__(self, parent = None):
        super(SettingPage,self).__init__(parent)

        self.setFixedSize(850, 800)
        self.right_widget = QWidget() # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QGridLayout()
        self.right_layout.setSpacing(1)
        self.right_widget_show_setting()
        self.right_addWidget_setting()
        self.setSettingStyle()

        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格
        self.setLayout(self.right_layout)  # 设置窗口主部件
        self.setWindowTitle('SettingPage')

    def right_widget_show_setting(self):
        self.right_bar_widget = QWidget()  # 右侧顶部框部件
        self.right_bar_layout = QVBoxLayout()  # 右侧顶部网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)

        v_x  = 800
        v_y = 70
        vv_x = 780
        vv_y = 140
        self.right_bar_widget_input = QLineEdit()
        self.right_bar_widget_input.setPlaceholderText("127.0.0.1")
        self.right_bar_widget_input.setFixedSize(vv_x, v_y)
        self.right_bar_widget_input.setObjectName('right_edit')

        self.right_bar_widget_input2 = QLineEdit()
        self.right_bar_widget_input2.setPlaceholderText("D:\MSO4045B\CSD")
        self.right_bar_widget_input2.setFixedSize(vv_x, v_y)
        self.right_bar_widget_input2.setObjectName('right_edit')

        self.packageGroup = QGroupBox('Oscilloscope IP  ')
        vLayout = QVBoxLayout()
        vLayout.addWidget(self.right_bar_widget_input,0,Qt.AlignCenter)
        self.packageGroup.setFixedSize(v_x,vv_y)
        self.packageGroup.setLayout(vLayout)
        self.packageGroup.setObjectName('group')
        self.packageGroup.setToolTip('设定Oscilloscope IP')

        self.packageGroup2 = QGroupBox('Picture Path  ')
        vLayout2 = QVBoxLayout()
        vLayout2.addWidget(self.right_bar_widget_input2,0,Qt.AlignCenter)
        self.packageGroup2.setFixedSize(v_x, vv_y)
        self.packageGroup2.setLayout(vLayout2)
        self.packageGroup2.setObjectName('group')
        self.packageGroup2.setToolTip('设定图片存储路径.')

        self.confirm_button = QPushButton('Confirm')
        self.confirm_button.setObjectName('right_button')
        self.confirm_button.setFixedSize(280, 80)
        self.confirm_button.setToolTip('保存设定信息.')

        self.vWidget3 = QWidget()
        vLayout3 = QVBoxLayout()
        vLayout3.addWidget(self.confirm_button,0,Qt.AlignCenter|Qt.AlignBottom)
        self.vWidget3.setLayout(vLayout3)

    def right_addWidget_setting(self):

        self.right_layout.addWidget(self.packageGroup,0,0)
        self.right_layout.addWidget(self.packageGroup2,1,0)
        self.right_layout.addWidget(self.vWidget3,2,0)

    def setSettingStyle(self):
        """
        right_edit
        :return:
        """
        self.setStyleSheet("""
            QWidget{
                background:#1F2227;
                margin:1px;
                border:1px solid;
            }
            QWidget#right_button{
                color : white;
                background:#444444;
                font-size:38px;
                font-weight:1000;
                border-radius:20px;
            }
            QWidget#right_edit{
                background:white;
                font-size:23px;
                font-weight:680;
                border-radius:20px;
            }
            QWidget#group{
            color : white;
            font-size:23px;
            font-weight:680;
            }
        
            """)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    gui = SettingPage()
    gui.show()
    sys.exit(app.exec_())
