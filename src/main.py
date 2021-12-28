import json

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QFileDialog, QApplication

from src.common.setting import *
from src.functions.robBackupReform.rob_backup_reform import robBackupReform


class load_conf():
    def __init__(self):
        # 路径配置
        path_conf = load_path_conf()
        self.path_conf = path_conf
        # 缓存配置
        cache_conf = load_cache_conf()
        self.cache_conf = cache_conf

    def updateAll(self):
        pass


class load_path_conf():
    def __init__(self):
        with open(path_json, 'r', encoding='utf-8') as f:
            try:
                PATH_JSON = json.load(f)
                # 净化配置文件
                # setting.path_conf 中存在，PATH_JSON中不存在的元素，需要新增并赋值初始设定值
                for o in origin_setting['path_conf']:
                    if o not in PATH_JSON:
                        PATH_JSON[o] = origin_setting['path_conf'][o]
                # setting.path_conf 中不存在，PATH_JSON中存的元素，需要删除
                for p in list(PATH_JSON.keys()):
                    if p not in origin_setting['path_conf']:
                        PATH_JSON.pop(p)
            except:
                PATH_JSON = self.reset()
            f.close()
        self.PATH_JSON = PATH_JSON
        self.updatePath()

    def reset(self):
        ret = {}
        for o in origin_setting['path_conf']:
            ret[o] = origin_setting['path_conf'][o]
        return ret

    def updatePath(self):
        with open(path_json, 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.PATH_JSON))
            f.close()

    def isRecommend(self):
        database_path = self.PATH_JSON['database_path']
        re_database_path = self.PATH_JSON['workspace_path'] + '/database'
        rob_backup_path = self.PATH_JSON['rob_backup_path']
        re_rob_backup_path = self.PATH_JSON['workspace_path'] + '/rob_backup_reform'
        rob_dicorder_pool_path = self.PATH_JSON['rob_dicorder_pool_path']
        re_rob_dicorder_pool_path = self.PATH_JSON['workspace_path'] + '/rob_dicorder_pool'
        report_path = self.PATH_JSON['report_path']
        re_report_path = {
            'rob_backup_reform': self.PATH_JSON['workspace_path'] + '/report/rob_backup_reform'
        }
        configure_path = self.PATH_JSON['configure_path']
        re_configure_path = self.PATH_JSON['workspace_path'] + '/configure'
        location_map_conf_path = self.PATH_JSON['location_map_conf_path']
        re_location_map_conf_path = self.PATH_JSON['workspace_path'] + '/configure/location_map.json'

        if database_path != re_database_path and rob_backup_path != re_rob_backup_path and rob_dicorder_pool_path != re_rob_dicorder_pool_path and report_path != re_report_path and configure_path != re_configure_path and location_map_conf_path != re_location_map_conf_path:
            self.PATH_JSON['is_recommend'] = False


class load_cache_conf():
    def __init__(self):
        self.CACHE_JSON = {}
        with open(cache_json, 'r', encoding='utf-8') as f:
            try:
                CACHE_JSON = json.load(f)
            except:
                CACHE_JSON = self.reset()
            f.close()
        self.CACHE_JSON = CACHE_JSON
        self.updateCache()

    def reset(self):
        ret = {}
        for o in origin_setting['cache_conf']:
            ret[o] = origin_setting['cache_conf'][o]
        return ret

    def updateCache(self):
        with open(cache_json, 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.CACHE_JSON))
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
        self.syncConfigure()
        # pushButton连接
        self.signalConnect()
        # widgetInit状态初始化
        self.widgetInit()

    def syncConfigure(self):
        # 将界面显示与配置文件同步
        self.ui.lineEdit_workspace_path.setText(conf.path_conf.PATH_JSON[WORKSPACE_PATH])
        self.ui.lineEdit_rob_backup.setText(conf.path_conf.PATH_JSON[ROB_BACKUP_PATH])
        self.ui.lineEdit_disorder_pool.setText(conf.path_conf.PATH_JSON[ROB_DISORDER_POOL_PATH])
        self.ui.lineEdit_report_path.setText(conf.path_conf.PATH_JSON[REPORT_PATH][ROB_BACKUP_REFORM])
        self.ui.lineEdit_configure.setText(conf.path_conf.PATH_JSON[LOCATION_MAP_CONF_JSON])
        # widget状态同步， 控件做出相应改变
        self.syncWidget()

    def widgetInit(self):
        # pushButton初始化
        # 当未指定工作空间根目录时候，设置按钮不可用
        # if conf.path_conf.PATH_JSON[WORKSPACE_PATH] == '':
        #     self.ui.pushButton_recommend.setEnabled(False)
        # self.ui.pushButton_edit_configure.setEnabled(False)
        self.ui.pushButton_report.setEnabled(False)
        # if conf.path_conf.PATH_JSON[ROB_BACKUP_PATH] == '' or conf.path_conf.PATH_JSON[ROB_DISORDER_POOL_PATH] == '' or \
        #         conf.path_conf.PATH_JSON[REPORT_PATH][ROB_BACKUP_REFORM] == '' or conf.path_conf.PATH_JSON[
        #     LOCATION_MAP_CONF_JSON] == '':
        #     self.ui.pushButton_start.setEnabled(False)
        # 进度条初始化
        self.ui.progressBar_result.setValue(0)
        # 在信息框中打印当前状态
        self.setTextBorwser(target='log', conetnt=content)


    def syncWidget(self):
        # pushButton初始化
        # 当未指定工作空间根目录时候，设置按钮不可用
        if conf.path_conf.PATH_JSON[WORKSPACE_PATH] == '':
            self.ui.pushButton_recommend.setEnabled(False)
        else:
            self.ui.pushButton_recommend.setEnabled(True)
        # 选择配置文件
        if conf.path_conf.PATH_JSON[LOCATION_MAP_CONF_JSON] == '':
            self.ui.pushButton_edit_configure.setEnabled(False)
        else:
            self.ui.pushButton_edit_configure.setEnabled(True)
        # 开始按钮
        if (conf.path_conf.PATH_JSON[ROB_BACKUP_PATH] == '' or conf.path_conf.PATH_JSON[ROB_DISORDER_POOL_PATH] == '' or \
            conf.path_conf.PATH_JSON[REPORT_PATH][ROB_BACKUP_REFORM] == '' or conf.path_conf.PATH_JSON[
                LOCATION_MAP_CONF_JSON] == '') or (
                conf.path_conf.PATH_JSON[WORKSPACE_PATH] == '' or conf.path_conf.PATH_JSON[
            LOCATION_MAP_CONF_JSON] == ''):
            self.ui.pushButton_start.setEnabled(False)
        else:
            self.ui.pushButton_start.setEnabled(True)
        curr_index = conf.cache_conf.CACHE_JSON['tabWidget_rob_backup_reform']['curr_index']
        if curr_index == 0:
            if (conf.path_conf.PATH_JSON[WORKSPACE_PATH] != '' and conf.path_conf.PATH_JSON[WORKSPACE_PATH] and
                    conf.path_conf.PATH_JSON[
                        LOCATION_MAP_CONF_JSON] != ''):
                self.ui.pushButton_start.setEnabled(True)
            else:
                self.ui.pushButton_start.setEnabled(False)
        elif curr_index == 1:
            if (conf.path_conf.PATH_JSON[ROB_BACKUP_PATH] != '' and conf.path_conf.PATH_JSON[
                ROB_DISORDER_POOL_PATH] != '' and conf.path_conf.PATH_JSON[REPORT_PATH][ROB_BACKUP_REFORM] != '' and
                    conf.path_conf.PATH_JSON[LOCATION_MAP_CONF_JSON] != ''):
                self.ui.pushButton_start.setEnabled(True)
            else:
                self.ui.pushButton_start.setEnabled(False)
        else:
            pass

    def signalConnect(self):
        # =========机器人备份重组=========
        # 推荐模式
        self.ui.pushButton_workspace_path.clicked.connect(lambda: self.selectPath(WORKSPACE_PATH))
        self.ui.pushButton_recommend.clicked.connect(lambda: self.setRecommend(ROB_BACKUP_REFORM))
        # 自定义模式
        self.ui.pushButton_rob_backup.clicked.connect(lambda: self.selectPath(ROB_BACKUP_PATH))
        self.ui.pushButton_disorder_pool.clicked.connect(lambda: self.selectPath(ROB_DISORDER_POOL_PATH))
        self.ui.pushButton_report_path.clicked.connect(lambda: self.selectPath(ROB_BACKUP_REFORM))
        # 选择配置文件
        self.ui.pushButton_configure.clicked.connect(lambda: self.selectFile(LOCATION_MAP_CONF_JSON))
        # 开始重组
        self.ui.pushButton_start.clicked.connect(lambda: robBackupReform(conf))
        # tab标签
        self.ui.tabWidget_rob_backup_reform.currentChanged.connect(lambda: self.changeTab())

    def selectPath(self, target):
        folder_path = QFileDialog.getExistingDirectory(self.ui, "选择路径")
        if folder_path != '':
            if target == WORKSPACE_PATH:
                conf.path_conf.PATH_JSON[WORKSPACE_PATH] = folder_path
                # self.setTextBorwser('error')
            elif target == ROB_BACKUP_PATH:
                conf.path_conf.PATH_JSON[ROB_BACKUP_PATH] = folder_path
                self.setWorkspaceNull()
            elif target == ROB_DISORDER_POOL_PATH:
                conf.path_conf.PATH_JSON[ROB_DISORDER_POOL_PATH] = folder_path
                self.setWorkspaceNull()
            elif target == ROB_BACKUP_REFORM:
                conf.path_conf.PATH_JSON[REPORT_PATH][ROB_BACKUP_REFORM] = folder_path
                self.setWorkspaceNull()
            self.syncConfigure()
            conf.path_conf.updatePath()

    def selectFile(self, target):
        file_name = QFileDialog.getOpenFileName(self.ui, "选择路径", configure_path, 'json file(*.json)')
        if file_name[0] != '':
            if target == LOCATION_MAP_CONF_JSON:
                self.ui.lineEdit_configure.setText(file_name[0])
                conf.path_conf.PATH_JSON[LOCATION_MAP_CONF_JSON] = file_name[0]
            conf.path_conf.updatePath()

    def changeTab(self):
        conf.cache_conf.CACHE_JSON['tabWidget_rob_backup_reform'][
            'curr_index'] = self.ui.tabWidget_rob_backup_reform.currentIndex()
        self.syncConfigure()
        conf.cache_conf.updateCache()

    def setRecommend(self, target):
        if target == ROB_BACKUP_REFORM:
            if conf.path_conf.PATH_JSON[WORKSPACE_PATH] == '':
                print('没有指定更目录')
            else:
                if conf.path_conf.PATH_JSON['workspace_path'] != origin_setting['path_conf']['workspace_path']:
                    conf.path_conf.PATH_JSON['database_path'] = conf.path_conf.PATH_JSON['workspace_path'] + '/database'
                    conf.path_conf.PATH_JSON['rob_backup_path'] = conf.path_conf.PATH_JSON[
                                                                      'workspace_path'] + '/rob_backup_reform'
                    conf.path_conf.PATH_JSON['rob_dicorder_pool_path'] = conf.path_conf.PATH_JSON[
                                                                             'workspace_path'] + '/rob_dicorder_pool'
                    conf.path_conf.PATH_JSON['report_path'] = {
                        'rob_backup_reform': conf.path_conf.PATH_JSON['workspace_path'] + '/report/rob_backup_reform'
                    }
                    conf.path_conf.PATH_JSON['configure_path'] = conf.path_conf.PATH_JSON[
                                                                     'workspace_path'] + '/configure'
                    conf.path_conf.PATH_JSON['location_map_conf_path'] = conf.path_conf.PATH_JSON[
                                                                             'workspace_path'] + '/configure/location_map.json'
                    self.syncConfigure()
                    conf.path_conf.updatePath()
                    self.setTextBorwser('log', str)

    def setWorkspaceNull(self):
        # 设置工作空间根目录为空
        conf.path_conf.PATH_JSON[WORKSPACE_PATH] = ''
        self.ui.lineEdit_workspace_path.setText('')
        self.ui.pushButton_recommend.setEnabled(False)

    def setTextBorwser(self, target, conetnt):
        if target == 'error':
            self.ui.textBrowser_error.append(conetnt)
        elif target == 'log':
            self.ui.textBrowser_log.setHtml(conetnt)
            # self.ui.textBrowser_log.append(conetnt)
            # self.ui.textBrowser_log.setStyleSheet(style)

        else:
            print('写入未知错误')


def main():
    app = QApplication([])
    mainwindow = Ui_Mainwindows()
    mainwindow.ui.show()
    app.exec_()


if __name__ == '__main__':
    main()
