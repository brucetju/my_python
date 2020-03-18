# -*- coding: utf-8 -*-
from src.my_u8_apps import *
from datetime import *
from src.my_email import *


cur_path = "/home/python/po_exec_info/my_python/"
#cur_path = ""
sql_server = connect(cur_path + "config.ini")

all_lines = get_qg_exec_info(sql_server)

lst_po_done_old = read_txt_to_list(cur_path + "po_done_result.txt")
dic_po_done_old = dict()
for po_done_info in lst_po_done_old:
    po = po_done_info.split(',')[0]
    done=po_done_info.split(",")[1]
    dic_po_done_old[po] = 1

all_msg = ""
dic_po_done_new = dict()
for index,each_line in enumerate(all_lines):
    if(index!=0):
        if(not dic_po_done_old.__contains__(each_line.qg_code)):
           lst_msg = each_line.get_info()
           for msg in lst_msg:
               all_msg += str(msg)+","
           all_msg+="\r\n"

lst_po_done_new = list()
for index,po in enumerate(all_lines):
    if(index!=0):
        if(not lst_po_done_new.__contains__(po.qg_code+",1")):
            lst_po_done_new.append(po.qg_code + ",1")
write_list_to_txt(lst_po_done_new,cur_path + "po_done_result.txt")

if(all_msg != ""):
    my_email = MyEmail("smtp.mxhichina.com",25,"jhtdesign@jht-design.com","Jhtdesignteam01")
    my_email.config_text_email("jhtdesign@jht-design.com",["pengyu@jht-design.com"],"po is ready",all_msg)
    my_email.send()
#    my_email.config_text_email("jhtdesign@jht-design.com",["yfzl_a@jht-design.com"],"po is ready",all_msg)
#    my_email.send()
#    my_email.config_text_email("jhtdesign@jht-design.com",["shenqian@jht-design.com"],"po is ready",all_msg)
#    my_email.send()
#    my_email.config_text_email("jhtdesign@jht-design.com",["qiuwei@jht-design.com"],"po is ready",all_msg)
#    my_email.send()
#    my_email.config_text_email("jhtdesign@jht-design.com",["liujie@jht-design.com"],"po is ready",all_msg)
#    my_email.send()

write_list_to_txt([all_msg],cur_path + "last_added_po_done_result.txt")
#print(all_msg)
