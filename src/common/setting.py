# 获取根目录
from os.path import dirname, abspath

base_dir = dirname(dirname(abspath(__file__)))

path_json = 'configure/path.json'
main_ui_path = 'ui/main.ui'
configure_path = '/configure/'

path_conf = [
    'workspace_path',
    'rob_backup_path',
    'rob_dicorder_pool_path',
    'report_path',
    'location_map_conf_path'
]

origin_path_json = {
    'workspace_path': '',
    'database_path': '',
    'rob_backup_path': '',
    'rob_dicorder_pool_path': '',
    'report_path': {
        'robBackupReform': ''
    },
    'location_map_conf_path': ''
}


class origin_setting():
    def __init__(self):
        self.path = {
            'workspace_path': '',
            'database_path': self.path['workspace_path'] + '/database',
            'rob_backup_path': self.path['workspace_path'] + '/rob_backup_reform',
            'rob_dicorder_pool_path': self.path['workspace_path'] + '/rob_dicorder_pool',
            'report_path': {
                'robBackupReform': self.path['workspace_path'] + '/report/rob_dicorder_pool'
            },
            'configure_path': self.path['workspace_path'] + '/configure',
            'location_map_conf_path': self.path['workspace_path'] + '/configure/location_map.json'
        }

    WORKSPACE_PATH = 'workspace_path'
    ROB_BACKUP_REFORM = 'rob_backup_reform'
    ROB_BACKUP_PATH = 'rob_backup_path'
    ROB_DISORDER_POOL_PATH = 'rob_dicorder_pool_path'
    REPORT_PATH = 'report_path'
    LOCATION_MAP_CONF_JSON = 'location_map_conf_path'
