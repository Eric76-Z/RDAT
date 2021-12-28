# 获取根目录
from os.path import dirname, abspath

base_dir = dirname(dirname(abspath(__file__)))

path_json = 'configure/path.json'
cache_json = 'configure/cache.json'
main_ui_path = 'ui/main.ui'
configure_path = '/configure/'

path_conf = [
    'workspace_path',
    'rob_backup_path',
    'rob_dicorder_pool_path',
    'report_path',
    'location_map_conf_path'
]

origin_setting = {
    'path_conf': {
        'workspace_path': '',
        'database_path': '',
        'rob_backup_path': '',
        'rob_dicorder_pool_path': '',
        'report_path': {
            'rob_backup_reform': ''
        },
        'configure_path': '',
        'location_map_conf_path': ''
    },
    'cache_conf': {
        'tabWidget_rob_backup_reform': {
            'curr_index': 0,
        }
    }
}

# class origin_setting():
#     def __init__(self):
#         self.path = {
#             'workspace_path': '',
#             'database_path': '',
#             'rob_backup_path': '',
#             'rob_dicorder_pool_path': '',
#             'report_path': {
#                 'robBackupReform': ''
#             },
#             'configure_path': '',
#             'location_map_conf_path': ''
#         }
#         self.state = 'outsync'
#
#     def syncPath(self):
#         if self.state == 'outsync':
#             self.path['database_path'] = self.path['workspace_path'] + '/database'
#             self.path['rob_backup_path'] = self.path['workspace_path'] + '/rob_backup_reform'
#             self.path['rob_dicorder_pool_path'] = self.path['workspace_path'] + '/rob_dicorder_pool'
#             self.path['report_path'] = {
#                 'robBackupReform': self.path['workspace_path'] + '/report/rob_backup_reform'
#             }
#             self.path['configure_path'] = self.path['workspace_path'] + '/configure'
#             self.path['location_map_conf_path'] = self.path['workspace_path'] + '/configure/location_map.json'
#             self.state = 'sync'
#         print(self.path)


WORKSPACE_PATH = 'workspace_path'
ROB_BACKUP_REFORM = 'rob_backup_reform'
ROB_BACKUP_PATH = 'rob_backup_path'
ROB_DISORDER_POOL_PATH = 'rob_dicorder_pool_path'
REPORT_PATH = 'report_path'
LOCATION_MAP_CONF_JSON = 'location_map_conf_path'

content = '''
  <div class='rpc-init'>
    <div class="title" style="display: flex;">
      <div class="label" style="flex: 1;">机器人备份重组详情</div>
      <div class="time">[2021-12-28 14:03:26]</div>
    </div>
    <div class='content'>
      <div>工作模式：推荐模式</div>
      <div>工作空间根目录： F:/ws1</div>
      <div>机器人备份路径：F:/ws1/rob_backup_reform</div>
      <div>机器人输出报告路径：F:/ws1/report/rob_backup_reform</div>
      <div>机器人备份乱序池路径：F:/ws1/rob_dicorder_pool</div>
      <div>机器人配置文件：F:/ws1/configure/location_map.json</div>
    </div>
  </div>
'''
style = '''
.rpc-init .title {
  display: flex;
}
.rpc-init .title .label {
  flex: 1;
}

'''
