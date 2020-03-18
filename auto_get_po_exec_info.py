from src.my_u8_apps import *
from datetime import *

file_path =r"/mnt/server2_jht_design/JHT-CKP-CIP-文件管理中心/文件中心/12-U8数据查询/003-金海通正式账套/03-请购单执行列表-每日更新-王荣荣/"
file_name = datetime.now().strftime('%Y-%m-%d') + "请购执行列表.xls"
file_name = "test.xls"
sql_server = connect("config.ini")
get_qg_exec_info(sql_server,file_path + file_name)
