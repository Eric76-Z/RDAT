from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QFileDialog


class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('test.ui')

        self.ui.pushButton.clicked.connect(self.selectPath)

    def selectPath(self):
        filePath = QFileDialog.getExistingDirectory(self.ui, "选择存储路径")
        self.ui.lineEdit.setText(filePath)


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
