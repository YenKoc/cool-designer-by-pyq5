import sys
import typing

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QDockWidget
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWin, self).__init__(parent)
        #设置主窗口标题
        self.setWindowTitle("第一个窗口应用")
        #设置窗口的尺寸
        self.resize(400,300)
        #获取状态栏
        self.status=self.statusBar()

        self.status.showMessage("只存在5秒的消息",5000)
if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/Dragon.ico'))
    main=FirstMainWin()
    main.show()
    sys.exit(app.exec_())