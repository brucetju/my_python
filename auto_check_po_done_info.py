# -*- coding: utf-8 -*-
from src.my_u8_apps import *
from datetime import *
from src.my_email import *

def get_email_add(name):
    if(name == "季宏薪"):
        return "jihonxin@jht-design.com"
    elif(name == "郑东"):
        return "zhengdong@jht-design.com"
    elif(name == "蔡雷"):
        return "cailei@jht-design.com"
    elif(name == "郝雄"):
        return "haoxiong@jht-design.com"
    elif(name == "李磊"):
        return "lilei@jht-design.com"
    elif(name == "郑锐"):
        return "zhengrui@jht-design.com"
    elif(name == "吕勇"):
        return "lvyong@jht-design.com"
    elif(name == "李彦樟"):
        return "liyanzhang@jht-design.com"
    elif(name == "石家全"):
        return "shijiaquan@jht-design.com"
    elif(name == "彭煜"):
        return "pengyu@jht-design.com"
    elif(name == "卢壮壮"):
        return "luzhuangzhuang@jht-design.com"
    elif(name == "吕克振"):
        return "lvkezhen@jht-design.com"
    elif(name == "贺怀珍"):
        return "hehuaizhen@jht-design.com"
    elif(name == "任彬"):
        return "renbin@jht-design.com"
    elif(name == "杨文宝"):
        return "yangwenbao@jht-design.com"
    elif(name == "孙毅俊"):
        return "syj@jht-design.com"
    elif(name == "张钊海"):
        return "zhangzhaohai@jht-design.com"
    elif(name == "陈锟辉"):
        return "chenkunhui@jht-design.com"
    elif(name == "沈程"):
        return "shencheng@jht-design.com"
    elif(name == "孟飞"):
        return "mengfei@jht-design.com"
    elif(name == "龙波"):
        return "long.bo@jht-design.com"

    return ""

cur_path = "/home/python/po_exec_info/my_python/"
#cur_path = ""
sql_server = connect(cur_path + "config.ini")

all_lines = get_qg_exec_info(sql_server)

lst_po_done_old = read_txt_to_list(cur_path + "po_done_result.txt")
dic_po_done_old = dict()
for po_done_info in lst_po_done_old:
    po = po_done_info.split(',')[0]
    dic_po_done_old[po] = 1

all_msg = ""
to_list = list()
dic_po_done_new = dict()
for index,each_line in enumerate(all_lines):
    if(not dic_po_done_old.__contains__(each_line.qg_code)):
       if(get_email_add(each_line.qg_person_name) != ""):
           if(not to_list.__contains__(each_line.qg_person_name)):
               to_list.append(get_email_add(each_line.qg_person_name))
       lst_msg = each_line.get_info()
       for msg in lst_msg:
           all_msg += str(msg)+","
       all_msg+="\r\n"

lst_po_done_new = list()
for index,po in enumerate(all_lines):
    if(not lst_po_done_new.__contains__(po.qg_code+",1")):
        lst_po_done_new.append(po.qg_code + ",1")
write_list_to_txt(lst_po_done_new,cur_path + "po_done_result.txt")

if(all_msg != ""):
    my_email = MyEmail("smtp.mxhichina.com",25,"jhtdesign@jht-design.com","Jhtdesignteam01")
    to_list.append("pengyu@jht-design.com")
    to_list.append("yfzl_a@jht-design.com")
    to_list.append("shenqian@jht-design.com")
    to_list.append("liujie@jht-design.com)
    for email in to_list:
        my_email.config_text_email("jhtdesign@jht-design.com",[email],"请购单已入库通知",all_msg)
        my_email.send()

#    my_email.config_text_email("jhtdesign@jht-design.com",["pengyu@jht-design.com"],"请购单已入库通知",all_msg)
#    my_email.send()
#    my_email.config_text_email("jhtdesign@jht-design.com",["yfzl_a@jht-design.com"],"请购单已入库通知",all_msg)
#    my_email.send()
#    my_email.config_text_email("jhtdesign@jht-design.com",["shenqian@jht-design.com"],"请购单已入库通知",all_msg)
#    my_email.send()
#    my_email.config_text_email("jhtdesign@jht-design.com",["qiuwei@jht-design.com"],"请购单已入库通知",all_msg)
#    my_email.send()
#    my_email.config_text_email("jhtdesign@jht-design.com",["liujie@jht-design.com"],"请购单已入库通知",all_msg)
#    my_email.send()

write_list_to_txt([all_msg],cur_path + "last_added_po_done_result.txt")
#print(all_msg)
