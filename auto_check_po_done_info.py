from src.my_u8_apps import *
from datetime import *
from src.my_email import *

sql_server = connect("config.ini")

all_lines = get_qg_exec_info(sql_server)

lst_po_done_old = read_txt_to_list("po_done_result.txt")
dic_po_done_old = dict()
for po_done_info in lst_po_done_old:
    po = po_done_info.split(',')[0]
    done=po_done_info.split(",")[1]
    dic_po_done_old[po] = int(done)

dic_po_done_new = dict()
for index,each_line in enumerate(all_lines):
    if(index!=0):
        if(not dic_po_done_new.__contains__(each_line[0])):
            dic_po_done_new[each_line[0]] = 1
        #print("+",each_line[28],",")
        #print(each_line[29])
        if(each_line[28] == ""):
            each_line[28]=0
        if(int(each_line[28])< int(each_line[29])):
            dic_po_done_new[each_line[0]] = 0;

lst_po_done_new = list()
for po in dic_po_done_new:
    lst_po_done_new.append(po+","+ str(dic_po_done_new[po]))
write_list_to_txt(lst_po_done_new,"po_done_result.txt")

dic_po_done_added = dict()
for po in dic_po_done_new:
    if(dic_po_done_new[po] == 1):
        if(dic_po_done_old.__contains__(po) and dic_po_done_old[po] ==0 ):
            dic_po_done_added[po]=1
            #print(po)
        elif(not dic_po_done_old.__contains__(po)):
            dic_po_done_added[po]=1
            #print(po)

all_msg = ""
if(dic_po_done_added.__len__ != 0):
    for po in dic_po_done_added:
        all_msg += po +","

if(all_msg != ""):
    my_email = MyEmail("smtp.mxhichina.com",25,"jhtdesign@jht-design.com","Jhtdesignteam01")
    my_email.config_text_email("jhtdesign@jht-design.com",["pengyu@jht-design.com"],
                               "po is ready",all_msg)
    my_email.send()

write_list_to_txt(dic_po_done_added,"last_added_po_done_result.txt")
print(all_msg)
