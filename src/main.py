import json

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QFileDialog, QApplication

from src.common.setting import *
from src.functions.robBackupReform.rob_backup_reform import robBackupReform


class load_conf():
    def __init__(self):
        with open(path_json, 'r', encoding='utf-8') as f:
            PATH_JSON = json.load(f)
            # 净化配置文件
            # setting.path_conf 中存在，PATH_JSON中不存在的元素，需要新增并赋值初始设定值
            for pc in path_conf:
                if pc not in PATH_JSON:
                    PATH_JSON[pc] = origin_path_json[pc]
            # setting.path_conf 中不存在，PATH_JSON中存的元素，需要删除
            for p in list(PATH_JSON.keys()):
                if p not in path_conf:
                    PATH_JSON.pop(p)
            self.PATH_JSON = PATH_JSON
            f.close()

    def updatePath(self):
        with open(path_json, 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.PATH_JSON))
            f.close()


class Ui_Mainwindows():
    def __init__(self):
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(main_ui_path)
        global conf
        conf = load_conf()
        self.process()

    def process(self):
        # 载入配置文件
        self.loadConfigure()
        # widgetInit状态初始化
        self.widgetInit()

    def loadConfigure(self):
        self.ui.lineEdit_workspace_path.setText(conf.PATH_JSON[WORKSPACE_PATH])
        self.ui.lineEdit_rob_backup.setText(conf.PATH_JSON[ROB_BACKUP_PATH])
        self.ui.lineEdit_disorder_pool.setText(conf.PATH_JSON[ROB_DISORDER_POOL_PATH])
        self.ui.lineEdit_report_path.setText(conf.PATH_JSON[REPORT_PATH][ROB_BACKUP_REFORM])
        self.ui.lineEdit_configure.setText(conf.PATH_JSON[LOCATION_MAP_CONF_JSON])

    def widgetInit(self):
        # pushButton初始化
        self.ui.pushButton_edit_configure.setEnabled(False)
        self.ui.pushButton_report.setEnabled(False)
        if conf.PATH_JSON[ROB_BACKUP_PATH] == '' or conf.PATH_JSON[ROB_DISORDER_POOL_PATH] == '' or \
                conf.PATH_JSON[REPORT_PATH][ROB_BACKUP_REFORM] == '' or conf.PATH_JSON[LOCATION_MAP_CONF_JSON] == '':
            self.ui.pushButton_start.setEnabled(False)
        # pushButton连接
        self.buttonConnect()
        # 进度条初始化
        self.ui.progressBar_result.setValue(0)

    def buttonConnect(self):
        # 推荐模式
        self.ui.pushButton_workspace_path.clicked.connect(lambda: self.selectPath(WORKSPACE_PATH))
        self.ui.pushButton_recommend.clicked.connect(lambda: self.setRecommend(ROB_BACKUP_REFORM))
        # 自定义模式
        self.ui.pushButton_rob_backup.clicked.connect(lambda: self.selectPath(ROB_BACKUP_PATH))
        self.ui.pushButton_disorder_pool.clicked.connect(lambda: self.selectPath(ROB_DISORDER_POOL_PATH))
        self.ui.pushButton_report_path.clicked.connect(lambda: self.selectPath(ROB_BACKUP_REFORM))

        self.ui.pushButton_configure.clicked.connect(lambda: self.selectFile(LOCATION_MAP_CONF_JSON))
        self.ui.pushButton_start.clicked.connect(lambda: robBackupReform(conf))

    def selectPath(self, target):
        folder_path = QFileDialog.getExistingDirectory(self.ui, "选择路径")
        if folder_path != '':
            if target == WORKSPACE_PATH:
                self.ui.lineEdit_workspace_path.setText(folder_path)
                conf.PATH_JSON[WORKSPACE_PATH] = folder_path
            elif target == ROB_BACKUP_PATH:
                self.ui.lineEdit_rob_backup.setText(folder_path)
                conf.PATH_JSON[ROB_BACKUP_PATH] = folder_path
            elif target == ROB_DISORDER_POOL_PATH:
                self.ui.lineEdit_disorder_pool.setText(folder_path)
                conf.PATH_JSON[ROB_DISORDER_POOL_PATH] = folder_path
            elif target == ROB_BACKUP_REFORM:
                self.ui.lineEdit_report_path.setText(folder_path)
                conf.PATH_JSON[REPORT_PATH][ROB_BACKUP_REFORM] = folder_path
            conf.updatePath()

    def selectFile(self, target):
        file_name = QFileDialog.getOpenFileName(self.ui, "选择路径", configure_path, 'json file(*.json)')
        if file_name[0] != '':
            if target == LOCATION_MAP_CONF_JSON:
                self.ui.lineEdit_configure.setText(file_name[0])
                conf.PATH_JSON[LOCATION_MAP_CONF_JSON] = file_name[0]
            conf.updatePath()

    def setRecommend(self, target):
        if target == ROB_BACKUP_REFORM:
            pass



def main():
    app = QApplication([])
    mainwindow = Ui_Mainwindows()
    mainwindow.ui.show()
    app.exec_()


if __name__ == '__main__':
    main()
