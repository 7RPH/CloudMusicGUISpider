"""
在这个例子中我们实现了如下功能：
选中复选框，点击提交，其对应的复选框内容将通过QMessageBox弹出
具备全选的功能
全选的复选框能够实时呈现（全选、半选、未选）下面复选框的选择情况
"""
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton,QMessageBox
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #新建4个复选框对象
        self.cb1 = QCheckBox('全选',self)
        self.cb2 = QCheckBox('你是',self)
        self.cb3 = QCheckBox('我的',self)
        self.cb4 = QCheckBox('宝贝',self)

        bt = QPushButton('提交',self)

        self.resize(300,200)
        self.setWindowTitle('早点毕业吧--复选框')

        self.cb1.move(20,20)
        self.cb2.move(30,50)
        self.cb3.move(30,80)
        self.cb4.move(30,110)

        bt.move(20,160)
        self.cb1.stateChanged.connect(self.changecb1)
        self.cb2.stateChanged.connect(self.changecb2)
        self.cb3.stateChanged.connect(self.changecb2)
        self.cb4.stateChanged.connect(self.changecb2)
        bt.clicked.connect(self.go)

        self.show()
    def go(self):
        if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self,'I Love U','你是我的宝贝！')
        elif self.cb2.isChecked() and self.cb3.isChecked():
            QMessageBox.information(self,'I Love U','你是我的！')
        elif self.cb2.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self,'I Love U','你是宝贝！')
        elif self.cb3.isChecked() and self.cb4.isChecked():
            QMessageBox.information(self,'I Love U','我的宝贝！')
        elif self.cb2.isChecked():
            QMessageBox.information(self,'I Love U','你是！')
        elif self.cb3.isChecked():
            QMessageBox.information(self,'I Love U','我的！')
        elif self.cb4.isChecked():
            QMessageBox.information(self,'I Love U','宝贝！')
        else:
            QMessageBox.information(self,'I Love U','貌似你没有勾选啊！')

    def changecb1(self):
        if self.cb1.checkState() == Qt.Checked:
            self.cb2.setChecked(True)
            self.cb3.setChecked(True)
            self.cb4.setChecked(True)
        elif self.cb1.checkState() == Qt.Unchecked:
            self.cb2.setChecked(False)
            self.cb3.setChecked(False)
            self.cb4.setChecked(False)
            """
isChecked()主要是判断复选框是否被选中，要是选中就返回True，否则返回False。
            """
    def changecb2(self):
        if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
            self.cb1.setCheckState(Qt.Checked)
        elif self.cb2.isChecked() or self.cb3.isChecked() or self.cb4.isChecked():
            self.cb1.setTristate()
            self.cb1.setCheckState(Qt.PartiallyChecked)
        else:
            self.cb1.setTristate(False)
            self.cb1.setCheckState(Qt.Unchecked)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())