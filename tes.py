from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from selenium.webdriver.chrome.options import Options

from spiderfunc import *

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        #页面布局
        self.setWindowTitle('网易云评论获取')
        self.setFixedSize(960, 700)
        self.mainWidget = QtWidgets.QWidget()  # 创建窗口主部件
        self.mainLayout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.mainWidget.setLayout(self.mainLayout)  # 设置窗口主部件布局为网格布局


        self.maxbtn=QPushButton(qtawesome.icon('fa.plus-circle',color='white',size=1),'')
        self.minbtn=QPushButton(qtawesome.icon('fa.minus-circle',color='white',size=1),'')
        self.closebtn=QPushButton(qtawesome.icon('fa.times-circle',color='white',size=1),'')
        self.maxbtn.setFixedSize(15,15)
        self.minbtn.setFixedSize(15, 15)
        self.closebtn.setFixedSize(15, 15)

        self.leftWidget=QWidget()
        self.leftLayout = QtWidgets.QGridLayout()
        self.leftWidget.setLayout(self.leftLayout)# 创建左侧部件的网格布局层
        self.leftWidget.setObjectName('leftWidget')

        self.rightWidget=QWidget()
        self.rightLayout = QtWidgets.QVBoxLayout()
        self.rightWidget.setLayout(self.rightLayout)
        self.rightWidget.setObjectName('rightWidget')


        self.mainLayout.addWidget(self.leftWidget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.leftLayout.addWidget(self.closebtn, 1, 0, 1, 1)
        self.leftLayout.addWidget(self.maxbtn, 1, 1, 1, 1)
        self.leftLayout.addWidget(self.minbtn, 1, 2, 1, 1)
        self.mainLayout.addWidget(self.rightWidget,0, 2, 12, 10)
        self.setCentralWidget(self.mainWidget)  # 设置窗口主部件
        self.mainLayout.setSpacing(0)
        self.leftLayout.setSpacing(0)
        self.rightLayout.setSpacing(0)
        self.userbtn = QtWidgets.QPushButton(qtawesome.icon('fa.user', color='white'), " 登录帐号")
        self.userbtn.setObjectName('left_button')
        self.mySongbtn = QtWidgets.QPushButton(qtawesome.icon('fa.list', color='white'), " 我的音乐")
        self.mySongbtn.setObjectName('left_button')
        self.searchbtn = QtWidgets.QPushButton(qtawesome.icon('fa.commenting-o', color='white'), " 评论搜集")
        self.searchbtn.setObjectName('left_button')
        self.dwnldbtn = QtWidgets.QPushButton(qtawesome.icon('fa.download', color='white'), " 下载管理")
        self.dwnldbtn.setObjectName('left_button')
        self.backbtn = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), " 反馈建议")
        self.backbtn.setObjectName('left_button')

        self.leftLayout.addWidget(self.searchbtn, 2, 0, 1, 3)
        self.leftLayout.addWidget(self.userbtn, 4, 0, 1, 3)
        self.leftLayout.addWidget(self.mySongbtn,6,0,1,3)
        self.leftLayout.addWidget(self.dwnldbtn,8,0,1,3)
        self.leftLayout.addWidget(self.backbtn, 10, 0, 1, 3)

        def mousePressEvent(self, QMouseEvent):
            if QMouseEvent.button() == Qt.LeftButton:
                self.flag = True
                # 获取鼠标相对窗口的位置
                self.m_Position = QMouseEvent.globalPos() - self.pos()
                QMouseEvent.accept()
                # 更改鼠标图标
                self.setCursor(QCursor(Qt.OpenHandCursor))

        def mouseMoveEvent(self, QMouseEvent):
            if Qt.LeftButton and self.flag:
                # 更改窗口位置
                self.move(QMouseEvent.globalPos() - self.m_Position)
                QMouseEvent.accept()

        def mouseReleaseEvent(self, QMouseEvent):
            self.flag = False
            self.setCursor(QCursor(Qt.ArrowCursor))

        #QSS
        self.closebtn.setStyleSheet(
            '''QPushButton{background:#FF3333;}''')
        self.maxbtn.setStyleSheet(
            '''QPushButton{background:#FF3333;}''')
        self.minbtn.setStyleSheet(
            '''QPushButton{background:#FF3333;}''')
        self.leftWidget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_button:hover{border-left:4px solid white;font-weight:700;}
            QWidget#leftWidget{
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-left:1px solid darkGray;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
                background:#FF3333;
            }

        ''')
        self.rightWidget.setStyleSheet('''
            
        QWidget#rightWidget{
            color:#232C51;
            background:white;
            border-top:1px solid darkGray;
            border-bottom:1px solid darkGray;
            border-right:1px solid darkGray;
            border-top-right-radius:10px;
            border-bottom-right-radius:10px;
        }
        QLineEdit{
            border:1px solid gray;
            width:300px;
            border-radius:10px;
            padding:2px 4px;
        }
        QPushButton#rightbtn{border:none;color:red;}
        QPushButton#rightbtn:hover{border-left:4px solid red;font-weight:700;}
        QComboBox {background-color:#FF3333;color: white;border:1px solid white;border-width: 2px;border-color:#FF6666;border-top-left-radius: 13px;border-bottom-left-radius: 13px;}
        QComboBox::drop-down {width: 40px;border:0px solid gray;} 
        QComboBox::hover{border:2px solid #BF5A5D;color: #FF6666;}
        QComboBox::pressed{ color: #FF6666;}
        QComboBox::focus{color: white;background-color: #FF6666;}
        QComboBox::checked{background-color: #FF6666;color:white;}
        QComboBox QAbstractItemView {color: #FF6666;selection-color: white;selection-background-color: #FF6666;}
        QComboBox QAbstractItemView::item:selected{	color: white;} ''')
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明


        #登录界面
        self.user=QtWidgets.QWidget()
        self.userlayout=QtWidgets.QGridLayout()
        self.user.setLayout(self.userlayout)
        self.space=QtWidgets.QWidget()
        self.logntip=QLabel('登录网易云以爬取更多个人歌曲: ',self.user)
        self.save=QtWidgets.QPushButton(qtawesome.icon('fa.sign-in'),'登录')
        self.save.setObjectName('rightbtn')
        self.labLognUser = QLabel("帐户:", self.user)  # 帐户标签
        self.linLognUser = QLineEdit(self.user)  # 帐户录入框
        self.linLognUser.setPlaceholderText("请输入手机号")
        self.labLognPwd = QLabel("密码:", self.user)  # 密码标签
        self.linLognPwd = QLineEdit(self.user)  # 密码录入框
        self.linLognPwd.setPlaceholderText("请输入密码")
        self.linLognPwd.setEchoMode(QLineEdit.Password)  # 设置密文显示
        self.userlayout.addWidget(self.labLognUser,2,2,1,1)
        self.userlayout.addWidget(self.linLognUser,2,3,1,3)
        self.userlayout.addWidget(self.labLognPwd, 3, 2, 1, 1)
        self.userlayout.addWidget(self.linLognPwd,3,3,1,3)
        self.userlayout.addWidget(self.logntip, 0, 0, 1, 9)
        self.userlayout.addWidget(self.space, 9, 0, 1, 9)
        self.userlayout.addWidget(self.save,4,4,1,1)


        #我的音乐列表
        self.mySong=QtWidgets.QWidget()
        self.mySong.setStyleSheet("background-color:pink;")


        #搜索界面
        self.search=QtWidgets.QWidget()
        self.searchwid = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.searchlayout = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.search.setLayout(self.searchlayout)
        self.searchIcon = QPushButton(qtawesome.icon('fa.search'),'搜索')
        self.searchIcon.setObjectName('rightbtn')
        self.searchInput = QtWidgets.QLineEdit()
        self.searchInput.setPlaceholderText("请输入用户, 歌曲或歌单")
        self.searchcombo=QtWidgets.QComboBox()
        self.searchcombo.addItem('用户')
        self.searchcombo.addItem('歌曲')
        self.searchcombo.addItem('歌单')
        self.usertab=QTableWidget()
        self.usertab.setColumnCount(3)
        self.usertab.setHorizontalHeaderLabels(['序号','用户名','操作'])
        self.searchlayout.addWidget(self.searchIcon, 0, 7, 1, 1)
        self.searchlayout.addWidget(self.searchcombo,0,2,1,1)
        self.searchlayout.addWidget(self.searchInput, 0, 3, 1, 4)
        self.searchlayout.addWidget(self.usertab,1,1,1,9)
        self.searchlayout.addWidget(self.searchwid, 9, 0, 1, 9)


        #下载界面
        self.dwnld=QtWidgets.QWidget()
        self.dwnld.setStyleSheet('''background:blue;
            ''')


        #反馈界面
        self.back = QtWidgets.QWidget()
        self.backlayout=QGridLayout()
        self.back.setLayout(self.backlayout)
        self.back.setObjectName('back')
        self.backlab=QLabel(self.back)
        self.backlab.setText('''有bug或者建议请在: <a href="https://therightpath.gitee.io/Python/%E7%88%AC%E8%99%AB/Python%E7%88%AC%E5%8F%96%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90%E8%AF%84%E8%AE%BA%E6%94%B9/">网页链接</a>写下评论!''')
        self.backlab.setOpenExternalLinks(True)
        self.backlayout.addWidget(self.backlab,5,5,5,5)
        self.back.setStyleSheet('''
        QWidget#back{
            background:white;
            border:1px solid darkGray;
            border-radius:10px;
        }''')

        # #右侧QSS
        # self.searchInput.setStyleSheet(
        #     '''QLineEdit{
        #             border:1px solid gray;
        #             width:300px;
        #             border-radius:10px;
        #             padding:2px 4px;
        #     }''')

        #初始化
        self.rightLayout.addWidget(self.search)

        def Writting(tag):
            print('点到了第',tag,'项 ...')

        #操作
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        logn=False#判定是否已经登录
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        driver=webdriver.Chrome(chrome_options=chrome_options)
        url = "https://music.163.com/#/search/m/"
        driver.get(url)
        self.userdic={
            'user':'',
            'pwd':'',
            'name':'',
            'searchtype':0
        }

        #btn互动
        self.closebtn.clicked.connect(lambda: (driver.quit()))
        self.closebtn.clicked.connect(self.close)
        self.minbtn.clicked.connect(self.showMinimized)
        self.maxbtn.clicked.connect(self.showMaximized)

        self.userbtn.clicked.connect(lambda :(self.rightLayout.itemAt(0).widget().setParent(None),self.rightLayout.insertWidget(0, self.user)))
        self.mySongbtn.clicked.connect(lambda :(self.rightLayout.itemAt(0).widget().setParent(None),self.rightLayout.insertWidget(0, self.mySong)))
        self.searchbtn.clicked.connect(lambda: (self.rightLayout.itemAt(0).widget().setParent(None),self.rightLayout.insertWidget(0, self.search)))
        self.dwnldbtn.clicked.connect(lambda: (self.rightLayout.itemAt(0).widget().setParent(None), self.rightLayout.insertWidget(0, self.dwnld)))
        self.backbtn.clicked.connect(lambda: (self.rightLayout.itemAt(0).widget().setParent(None),self.rightLayout.insertWidget(0, self.back)))

        self.searchcombo.currentIndexChanged.connect(lambda: (giveValue(self.userdic,'searchtype',self.searchcombo.currentIndex())))
        self.searchIcon.clicked.connect(lambda :())

        self.save.clicked.connect(lambda: (giveValue(self.userdic,'user',self.linLognUser.text())))
        self.save.clicked.connect(lambda: (giveValue(self.userdic,'pwd', self.linLognPwd.text())))
        self.save.clicked.connect(lambda: (login(driver, self.linLognUser.text(), self.linLognPwd.text(), logn)))


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()