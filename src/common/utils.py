import datetime
import os
import time


def logWrite(wb, controllername, sort, msg):
    sh = wb['log']
    # row_now = sh.max_row
    content = [controllername, datetime.datetime.now(), sort, msg]
    sh.append(content)


def createSheet(wb, sh_name, sh_index, sh_title):
    '''
    wb: workbook实例
    sh_name:要创建的表格名字
    sh_index:sheet的index
    sh_title: sheet第一行标题，为列表
    '''

    wb.create_sheet(title=sh_name, index=sh_index)
    sh = wb[sh_name]
    sh.append(sh_title)
    return


# def logTrash(controllername, msg):
#     log = open(PATH_TRASH + '\\' + LOG_TARSH_NAME, 'a')


def logWriteTitle(file, msg):
    log = open(file, 'a')
    log.write('==============================' + msg + '==============================' + '\r\n')
    log.close()


# 　　'''把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12'''
def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)


def getFileSize(filePath):
    size = os.path.getsize(filePath)  # 返回的是字节大小
    '''
    为了更好地显示，应该时刻保持显示一定整数形式，即单位自适应
    '''
    if size < 1000:
        return '%i' % size + ' size'
    elif 1000 <= size < 1000000:
        return '%.1f' % float(size / 1000) + ' KB'
    elif 1000000 <= size < 1000000000:
        return '%.1f' % float(size / 1000000) + ' MB'
    elif 1000000000 <= size < 1000000000000:
        return '%.1f' % float(size / 1000000000) + ' GB'
    elif 1000000000000 <= size:
        return '%.1f' % float(size / 1000000000000) + ' TB'


def createFolder(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
        pass


def backSignalSort(signal):
    if signal.startswith('E'):
        return 'E-输入端'
    elif signal.startswith('A'):
        return 'A-输出端'
    elif signal.startswith('M'):
        return 'M-标记器'
    elif signal.startswith('I'):
        return 'I-计数器'
    elif signal.startswith('ana'):
        return 'ana-模拟输出端'
    elif signal.startswith('bin'):
        return 'bin-二进制输出端'
    elif signal.startswith('t'):
        return 't-计数器'
    elif signal.startswith('F'):
        return 'F-旗标'
    elif signal.startswith('T'):
        return 'T-计时器旗标'
    elif signal.startswith('Makro'):
        return 'Makro-宏'
    elif signal.startswith('UP'):
        return 'UP-子程序'
    elif signal.startswith('cell'):
        return 'cell'
    else:
        return None


def process_bar(percent, start_str='', end_str='', total_length=0):
    bar = ''.join(["\033[31m%s\033[0m" % '   '] * int(percent * total_length)) + ''
    bar = '\r' + start_str + bar.ljust(total_length) + ' {:0>4.1f}%|'.format(percent * 100) + end_str
    print(bar, end='', flush=True)


# def textBrowser_rob_backup_reform_init(model, workspace_path, ):
#     ret = ''
#     local_time = time.localtime()
#     local_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
#     print(local_time)
#     content = '''
#       <div class='rpc-init'>
#         <div class="title" style="display: flex;">
#           <div class="label" style="flex: 1;">机器人备份重组详情</div>
#           <div class="time">{0}</div>
#         </div>
#         <div class='content'>
#           <div>工作模式：{1}</div>
#           <div>工作空间根目录： {2}</div>
#           <div>机器人备份路径：{3}</div>
#           <div>机器人输出报告路径：F:/ws1/report/rob_backup_reform</div>
#           <div>机器人备份乱序池路径：F:/ws1/rob_dicorder_pool</div>
#           <div>机器人配置文件：F:/ws1/configure/location_map.json</div>
#         </div>
#       </div>
#     '''.format('[' + local_time + ']', model, workspace_path, rob_backup_path)

