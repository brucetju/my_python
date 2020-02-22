from src.my_u8_apps import *
from datetime import *

file_name = datetime.now().strftime('%Y-%m-%d') + "请购执行列表.xls"

sql_server = connect("config.ini")
get_qg_exec_info(sql_server,file_name)
