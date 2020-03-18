from src.my_sql_server import *
from src.my_u8_server import *
from src.my_txt import *

import xlrd
from  xlwt import *
from xlutils.copy import  copy

def connect(config):
    "连接到U8服务器，返回sql_server"
    config = read_txt_to_list(config)
    sql_server = SQL_Server(config[0] ,config[1],config[2],config[3])

    return sql_server

def write_from_list(lst_alllines,file_name):
    '''
    写入excel文件，检查已到货项并返回
    '''
    
    workbook = Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('请购执行进度表')
    for row, exec_line in enumerate(lst_alllines):
        if(row != 0):
            for col, value in enumerate(exec_line.get_info()):
                worksheet.write(row, col, value)
                width = (len(str(value)) + 2) * 256
                if (worksheet.col(col).width < width):
                    worksheet.col(col).width = width
        else:
            for col, value in enumerate(exec_line):
                worksheet.write(row, col, value)
                width = (len(str(value)) + 2) * 256
                if (worksheet.col(col).width < width):
                    worksheet.col(col).width = width
    workbook.save(file_name)

def write_from_list1(lst_alllines,file_name = ""):
    '''
    写入excel文件，检查已到货项并返回
    '''
#    dic_po_done = dict()
##    dic_po_wl_qg_quant = dict()
#    dic_po_wl_rk_quant = dict()
#    last_qg_code = ""
#
#    for row, exec_line in enumerate(lst_alllines):
#        if(row != 0):
#            if(not dic_po_done.__contains__(exec_line.qg_code)):
#                dic_po_done[exec_line.qg_code] = 1
#
#                if(last_qg_code != ""):
#                    #检查是否到齐
#                    for wl_code in dic_po_wl_qg_quant:
#                        if(dic_po_wl_qg_quant[wl_code] > dic_po_wl_rk_quant[wl_code]):
#                            #print("qg_quant",str(dic_po_wl_qg_quant[wl_code]))
#                            #print("rk_quant",str(dic_po_wl_rk_quant[wl_code]))
#                            dic_po_done[last_qg_code] = 0
#                dic_po_wl_qg_quant = dict()
#                dic_po_wl_rk_quant = dict()
#                last_qg_code = exec_line.qg_code
#            if(str(exec_line.wl_quant) == ""):
#                exec_line.wl_quant = 0
#            if(str(exec_line.rk_quant) == ""):
#                exec_line.rk_quant = 0
#            dic_po_wl_qg_quant[exec_line.wl_code] = int(exec_line.wl_quant)
#            if(dic_po_wl_rk_quant.__contains__(exec_line.wl_code)):
#                dic_po_wl_rk_quant[exec_line.wl_code] += int(exec_line.rk_quant)
#            else:
#                dic_po_wl_rk_quant[exec_line.wl_code] = int(exec_line.rk_quant)
#    #最后一项的检查
#    for wl_code in dic_po_wl_qg_quant:
#        if(dic_po_wl_qg_quant[wl_code] < dic_po_wl_rk_quant[wl_code]):
#            dic_po_done[last_qg_code] = 0

    dic_qg_done = dict()
    dic_qg_details=dict()
    for row,exec_line in enumerate(lst_alllines):
        if(row !=0):
            if(not dic_qg_details.__contains__(exec_line.qg_code)):
                dic_qg_details[exec_line.qg_code] = dict()
            if(not dic_qg_details[exec_line.qg_code].__contains__(exec_line.wl_code)):
                dic_qg_details[exec_line.qg_code][exec_line.wl_code] = int(exec_line.wl_quant)
                if (exec_line.rk_quant == ""):
                    exec_line.rk_quant = 0
                dic_qg_details[exec_line.qg_code][exec_line.wl_code] -= int(exec_line.rk_quant)
            else:
                if(exec_line.rk_quant == ""):
                    exec_line.rk_quant = 0
                dic_qg_details[exec_line.qg_code][exec_line.wl_code] -= int(exec_line.rk_quant)

    for qg_code in dic_qg_details:
        dic_qg_done[qg_code] = 1
        for wl_code in dic_qg_details[qg_code]:
            if(dic_qg_details[qg_code][wl_code] != 0):
                dic_qg_done[qg_code] = 0

    dic_qg_done_line = list()
    for row,exec_line in enumerate(lst_alllines):
        if(row!=0):
            if(dic_qg_done.__contains__(exec_line.qg_code) and dic_qg_done[exec_line.qg_code] == 1):
                dic_qg_done_line.append((exec_line))

    if(file_name != ""):
        done_style = XFStyle()
        notdone_style = XFStyle()
    
        pattern1 = Pattern()
        pattern1.pattern =Pattern.SOLID_PATTERN
        pattern1.pattern_fore_colour = Style.colour_map['green']
        done_style.pattern = pattern1

        pattern2 = Pattern()
        pattern2.pattern =Pattern.SOLID_PATTERN
        pattern2.pattern_fore_colour = Style.colour_map['white']
        notdone_style.pattern = pattern2

        dic_po_style = dict()
        for qg_code in dic_qg_done:
            if(dic_qg_done[qg_code] ==1):
                dic_po_style[qg_code] = done_style
                #print("done")
            else:
                dic_po_style[qg_code] = notdone_style


        workbook = Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('请购执行进度表')
        for row, exec_line in enumerate(lst_alllines):
            if(row != 0):
                for col, value in enumerate(exec_line.get_info()):
                    worksheet.write(row, col, value,dic_po_style[exec_line.qg_code])
                    width = (len(str(value)) + 2) * 256
                    if (worksheet.col(col).width < width):
                        worksheet.col(col).width = width
            else:
                for col, value in enumerate(exec_line):
                    worksheet.write(row, col, value)
                    width = (len(str(value)) + 2) * 256
                    if (worksheet.col(col).width < width):
                        worksheet.col(col).width = width
        workbook.save(file_name)
    return dic_qg_done_line
    
def get_qg_exec_info(sql_server,file_name=""):
    '''
    获取请购执行列表，并存入file_name文件.
    bug:
    solved: 同一采购单号中的同一物料编码，对应多个到货入库单号（如：采购单号JHT-CG19120330） solved
    solved: 请购单号并不均再Po_Details表中，如JHT-QG200211006中的 EI40002 solved
    solved: 请购人名字需要对应 solved
    solved: 供应商名字需要对应 solved
    solved: JHT-CGRK191223131 入库数量记录有问题，数据库值为4，写入值为6 solved,入库数量应找出对应到货单号+物料编码的表
    solved: JHT-CG19050097 同一采购单可以对应不同请购单,所以找对应到货单号时会出问题。 solved,PO_Podetails:id == rdrecords01:iPOsID == PU_ArrivalVouchs:iPOsID,用该ID做索引
    solved: 入库单号重复，同一请购单中的一行可能会多次到货，不可以用行标识符去找入库单，替换为用到货单号查找入货单号
    bug: u8系统可能有问题,JHT-QG190814092中EZQ0001的采购分了3次，JHT-CG20020141/JHT-CG19120161/JHT-CG19110183但只记录了2次
    bug: u8系统选择的订单有没有过滤条件？JHT-QG190226049请购订单在u8导出来的文件中只出现了3次，但实际请购种类远大于3次。
    执行逻辑：
	PU_AppVouchs:AutoID 可对应多个 PO_Podetails:iAppIds 
	PO_Podetails:ID 可对应多个 PU_ArrivalVouchs:iPOsID
	PU_ArrivalVouchs:Autoid 可对应多个 rdrecords01:iArrsId,如JHT-CGRK191014132
	
    1. 购单子表(PU_AppVouchs)中存储请购单的每一行信息，并拥有唯一标识为AutoID<采购请购单子表标识>,根据请购单号在请购单总表(PU_AppVouch)中找出时间等信息
    2. 在采购订单子表(PO_Podetails)中，根据<采购请购单子表标识>查找记录的采购信息，再用采购订单号再采购总表(PO_Pomain)中找出时间等信息
    3. 在到货子表(PU_ArrivalVouchs)中，依次找出<采购请购单子表标识>对应的一次，或多次到货单号，记录对应的信息，再利用到货单号，再到货总表(PU_ArrivalVouch)中找出时间等信息
    4. 在入库子表(rdrecords01)中，根据到货单号找出入库单号等信息，记录入库详细信息，再利用入库单号再入库总表(RdRecord01)中找出时间等其他信息
    '''
    u8_server = U8_Server()

    tb_Inventory  = sql_server.readinto_list(u8_server.Inventory,u8_server.Inventory_keys)
    dic_InvCode2Name = dict()

    tb_Person  = sql_server.readinto_list(u8_server.Person,u8_server.Person_keys)
    dic_PersonCode2Name = dict()

    tb_Vendor  = sql_server.readinto_list(u8_server.Vendor,u8_server.Vendor_keys)
    dic_VendorCode2Name = dict()

    #根据<采购请购单子表标识>倒序排列
    tb_PU_AppVouchs  = sql_server.readinto_list(u8_server.PU_AppVouchs,u8_server.PU_AppVouchs_keys,"",u8_server.PU_AppVouchs_AutoID)

    tb_PU_AppVouch  = sql_server.readinto_list(u8_server.PU_AppVouch,u8_server.PU_AppVouch_keys)
    dic_qg_zd_time = dict()  # 请购单号->制单时间
    dic_qg_sh_time = dict()  # 请购单号->审核时间
    dic_qg_dj = dict()  # 请购单号->请购等级
    dic_qg_name = dict()  # 请购单号为key>请购人

    tb_PO_Podetails  = sql_server.readinto_list(u8_server.PO_Podetails,u8_server.PO_Podetails_keys)
    dic_cg_code = dict() #一级key为请购单号，二级key为物料代码，值为采购单号
    dic_cg_sub_code = dict() #一级key为请购单号，二级key为物料代码，值为采购单号
    dic_cg_jh_time = dict() #一级key为请购单号，二级key为物料代码，值为计划到货时间
    dic_cg_quant = dict() #一级key为请购单号，二级key为物料代码，值为计划到货时间
    dic_dh_keys = dict()

    #dic_sub_order_id2CGCode = dict() #<采购请购单子表标识> ->采购单号
    #dic_sub_order_id2CGsubCode = dict()#<采购请购单子表标识> ->采购子单号
    #dic_sub_order_id2jh_time = dict()#<采购请购单子表标识> ->采购计划时间
    #dic_sub_order_id2cg_quant = dict()#<采购请购单子表标识> ->采购数量

    tb_PO_Pomain  = sql_server.readinto_list(u8_server.PO_Pomain,u8_server.PO_Pomain_keys)
    dic_cg_zd_time = dict()  # 采购单号->制单时间
    dic_cg_vendor = dict()  # 采购单号->供应商
    dic_cg_sh_time = dict()  # 采购单号->审核时间
    
    tb_PU_ArrivalVouchs = sql_server.readinto_list(u8_server.PU_ArrivalVouchs,u8_server.PU_ArrivalVouchs_keys)
    dic_dh_code = dict()  # <采购请购单子表标识>->到货单号序列，同一<采购请购单子表标识>可能会对应不同到货单号
    dic_dh_sub_code = dict()  # <采购请购单子表标识>->到货子单号序列，同一<采购请购单子表标识>可能会对应不同到货单号
    dic_dh_quant = dict()  # <采购请购单子表标识>->到货数量序列，同一<采购请购单子表标识>可能会对应不同到货单号
    dic_rk_keys = dict()
	
    tb_PU_ArrivalVouch = sql_server.readinto_list(u8_server.PU_ArrivalVouch,u8_server.PU_ArrivalVouch_keys)
    dic_dh_zd_time = dict()  # 到货单号->制单时间
    dic_dh_sh_time = dict()  # 到货单号->审核时间

    tb_rdrecords01  = sql_server.readinto_list(u8_server.rdrecords01,u8_server.rdrecords01_keys)
    dic_rk_code = dict() # 到货单号->入库单号
    dic_rk_sub_code = dict() # 到货单号->入库子单号
    dic_rk_quant = dict() # 到货单号->入库数量

    tb_RdRecord01  = sql_server.readinto_list(u8_server.RdRecord01,u8_server.RdRecord01_keys)
    dic_rk_zd_time = dict()#入库单号 ->制单时间
    dic_rk_sh_time =dict()#入库单号 ->审核时间



    # 处理物料编码与物料名称的关系
    for line in tb_Inventory:
        dic_InvCode2Name[line[u8_server.Inventory_code]] = line[u8_server.Inventory_name]

    # 请购人名字
    for line in tb_Person:
        dic_PersonCode2Name[line[u8_server.Person_code]] = line[u8_server.Person_name]

    # 供应商名字
    for line in tb_Vendor:
        dic_VendorCode2Name[line[u8_server.Vendor_code]] = line[u8_server.Vendor_name]

    # 处理请购单主表信息
    for line in tb_PU_AppVouch:
        dic_qg_zd_time[line[u8_server.PU_AppVouch_cCode]] = line[u8_server.PU_AppVouch_cMakeTime]
        dic_qg_sh_time[line[u8_server.PU_AppVouch_cCode]] = line[u8_server.PU_AppVouch_cAuditTime]
        dic_qg_dj[line[u8_server.PU_AppVouch_cCode]] = line[u8_server.PU_AppVouch_cDefine11]
        dic_qg_name[line[u8_server.PU_AppVouch_cCode]] = line[u8_server.PU_AppVouch_cPersonCode]

    # 采购订单信息中获取请购单对应的采购单号及计划到货日期
    for line in tb_PO_Podetails:
        cg_key = line[u8_server.PO_Podetails_iAppIds]
        temp = line[u8_server.PO_Podetails_cbsysbarcode].split('|')
        if (len(temp) == 5):
            code = temp[-2]
            sub_code = temp[-1]
        else:
            code = temp[-1]
            sub_code = 0
			
        if(not dic_cg_code.__contains__(cg_key)):
            dic_cg_code[cg_key] = list()
            dic_cg_sub_code[cg_key] = list()
            dic_cg_jh_time[cg_key] = list()
            dic_cg_quant[cg_key] = list()
            dic_dh_keys[cg_key] = list()

        dic_cg_code[cg_key].append(code)
        dic_cg_sub_code[cg_key].append(sub_code)
        dic_cg_jh_time[cg_key].append(line[u8_server.PO_Podetails_dArriveDate])
        dic_cg_quant[cg_key].append(line[u8_server.PO_Podetails_iQuantity])
        dic_dh_keys[cg_key].append(line[u8_server.PO_Podetails_ID])
	
##    for cg_key in dic_dh_keys:
##        if(len(dic_dh_keys[cg_key])>1):
##            print("cg_code ",cg_key," -> ",str(len(dic_dh_keys[cg_key]))," dh_key: ")
##            for dh_key in dic_dh_keys[cg_key]:
##                print(dh_key)
	
	
    # 处理请购单号对应的采购单号的详细信息
    for line in tb_PO_Pomain:
        if (not dic_cg_zd_time.__contains__(line[u8_server.PO_Pomain_cPOID])):
            dic_cg_zd_time[line[u8_server.PO_Pomain_cPOID]] = dict()
            dic_cg_vendor[line[u8_server.PO_Pomain_cPOID]] = dict()
            dic_cg_sh_time[line[u8_server.PO_Pomain_cPOID]] = dict()

        dic_cg_zd_time[line[u8_server.PO_Pomain_cPOID]] = line[u8_server.PO_Pomain_cmaketime]
        dic_cg_vendor[line[u8_server.PO_Pomain_cPOID]] = line[u8_server.PO_Pomain_cVenCode]
        dic_cg_sh_time[line[u8_server.PO_Pomain_cPOID]] = line[u8_server.PO_Pomain_cAuditTime]

    # 到货子单
    for line in tb_PU_ArrivalVouchs:
        dh_key = line[u8_server.PU_ArrivalVouchs_iPOsID]
        if (str(line[u8_server.PU_ArrivalVouchs_cbsysbarcode]) != 'None'):
            temp = line[u8_server.PU_ArrivalVouchs_cbsysbarcode].split('|')
        if (len(temp) == 5):
            code = temp[-2]
            sub_code = temp[-1]
        else:
            code = temp[-1]
            sub_code = 0
                            
        if (not dic_dh_code.__contains__(dh_key)):
            dic_dh_code[dh_key] = list()
            dic_dh_sub_code[dh_key] = list()
            dic_dh_quant[dh_key] = list()
            dic_rk_keys[dh_key] = list()

        dic_dh_code[dh_key].append(code)
        dic_dh_sub_code[dh_key].append(sub_code)
        dic_dh_quant[dh_key].append(line[u8_server.PU_ArrivalVouchs_iQuantity])
        dic_rk_keys[dh_key].append(line[u8_server.PU_ArrivalVouchs_Autoid])

##    for dh_key in dic_rk_keys:
##        if(len(dic_rk_keys[dh_key])>1):
##            print("dh_code:",dh_key," -> ",str(len(dic_rk_keys[dh_key]))," rk_key: ")
##            for rk_key in dic_rk_keys[dh_key]:
##                print(rk_key)
    
    # 处理到货单号的时间信息
    for line in tb_PU_ArrivalVouch:
        dic_dh_zd_time[line[u8_server.PU_ArrivalVouch_cCode]] = line[u8_server.PU_ArrivalVouch_cMakeTime]
        dic_dh_sh_time[line[u8_server.PU_ArrivalVouch_cCode]] = line[u8_server.PU_ArrivalVouch_caudittime]

    # 处理到货单号与创建时间，审核时间的关系，处理入库单号与创建时间，审核时间的关系
    for line in tb_rdrecords01:
        rk_key = line[u8_server.rdrecords01_iArrsId]
        if (str(line[u8_server.rdrecords01_cbsysbarcode]) == 'None'):
            # print(line['cbarvcode'],line['cbsysbarcode'])
            continue
        temp = str(line[u8_server.rdrecords01_cbsysbarcode]).split('|')
        if (len(temp) == 5):
            code = temp[-2]
            sub_code = temp[-1]
        else:
            code = temp[-1]
            sub_code = 0

        if(not dic_rk_code.__contains__(rk_key)):
            dic_rk_code[rk_key] = list()
            dic_rk_sub_code[rk_key] = list()
            dic_rk_quant[rk_key] = list()
        else:
            pass
            #print("more than one rk_code for dh_code",code)
        
        dic_rk_code[rk_key].append(code)
        dic_rk_sub_code[rk_key].append(sub_code)
        dic_rk_quant[rk_key].append(line[u8_server.rdrecords01_iQuantity])

    # 处理入库单号的时间信息
    for line in tb_RdRecord01:
        dic_rk_zd_time[line[u8_server.RdRecord01_cCode]] = line[u8_server.RdRecord01_dnmaketime]
        dic_rk_sh_time[line[u8_server.RdRecord01_cCode]] = line[u8_server.RdRecord01_dnverifytime]

    '''
    最终请购执行列表的每一行
    '''
    lst_exec_lines = list()
    lst_exec_lines.append(ExecLine.get_col_names())

    for line in tb_PU_AppVouchs:  # 所有请购列表
        temp = line[u8_server.PU_AppVouchs_cbsysbarcode].split('|')
        if (len(temp) == 5):
            code = temp[-2]
            sub_code = temp[-1]
        else:
            code = temp[-1]
            sub_code = 0
        qg_code = code
        qg_sub_code = sub_code
        
        wl_code = line[u8_server.PU_AppVouchs_cInvCode]

        # 初始化当前行
        exec_line = ExecLine(qg_code, qg_sub_code)

        '''
        tb_Inventory
        '''
        exec_line.set_Inventory_info(dic_InvCode2Name[wl_code])

        """
        tb_PU_AppVouchs，tb_PU_AppVouch
        """
        exec_line.set_Pu_AppVouchs_info(wl_code, line[u8_server.PU_AppVouchs_fQuantity],
                                        line[u8_server.PU_AppVouchs_dRequirDate], line[u8_server.PU_AppVouchs_cDefine22])
        exec_line.set_PU_AppVouch_info(dic_qg_zd_time[qg_code], dic_qg_sh_time[qg_code],
                                       dic_qg_dj[qg_code], dic_qg_name[qg_code])

        '''
        tb_Person
        '''
        if (dic_PersonCode2Name.__contains__(exec_line.qg_person_code)):
            exec_line.set_Person_info(dic_PersonCode2Name[exec_line.qg_person_code])
        else:
            exec_line.set_Person_info("")

        cg_key = line[u8_server.PU_AppVouchs_AutoID]
        if(dic_cg_code.__contains__(cg_key)):
            for cg_index,cg_code in enumerate(dic_cg_code[cg_key]):
                #采购单子/主表信息
                exec_line.set_PO_Podetails_info(dic_cg_code[cg_key][cg_index],dic_cg_sub_code[cg_key][cg_index],
                                                dic_cg_jh_time[cg_key][cg_index],dic_cg_quant[cg_key][cg_index])
                exec_line.set_PO_Pomain_info(dic_cg_zd_time[cg_code], dic_cg_vendor[cg_code],dic_cg_sh_time[cg_code])

                if(dic_VendorCode2Name.__contains__(exec_line.cg_vendor_code)):
                    exec_line.set_Vendor_info(dic_VendorCode2Name[exec_line.cg_vendor_code])
                else:
                    exec_line.set_Vendor_info("")
        
                dh_key = dic_dh_keys[cg_key][cg_index]
                if(dic_dh_code.__contains__(dh_key)):
                    for dh_index,dh_code in enumerate(dic_dh_code[dh_key]):
                        #到货单子表/主表信息
                        exec_line.set_PU_ArrivalVouchs_info(dh_code,dic_dh_sub_code[dh_key][dh_index],dic_dh_quant[dh_key][dh_index])
                        exec_line.set_PU_ArrivalVouch_info(dic_dh_zd_time[dh_code], dic_dh_sh_time[dh_code])

                        rk_key = dic_rk_keys[dh_key][dh_index]
                        if(dic_rk_code.__contains__(rk_key)):
                            for rk_index,rk_code in enumerate(dic_rk_code[rk_key]):
                                #入库单子表/主表信息
                                exec_line.set_rdrecords01_info(rk_code,dic_rk_sub_code[rk_key][rk_index],dic_rk_quant[rk_key][rk_index])
                                if(dic_rk_zd_time.__contains__(rk_code)):
                                    exec_line.set_RdRecord01_info(dic_rk_zd_time[rk_code], dic_rk_sh_time[rk_code])
                                else:
                                    exec_line.set_RdRecord01_info("", "")

                                lst_exec_lines.append(exec_line)
                        else:
                            exec_line.set_rdrecords01_info("", "", "")
                            exec_line.set_RdRecord01_info("", "")

                            lst_exec_lines.append(exec_line)
                            
                else:
                    exec_line.set_PU_ArrivalVouchs_info("","","")
                    exec_line.set_PU_ArrivalVouch_info("", "")
                    exec_line.set_rdrecords01_info("", "", "")
                    exec_line.set_RdRecord01_info("", "")

                    lst_exec_lines.append(exec_line)
                    
        else:
            exec_line.set_PO_Podetails_info("","","","")
            exec_line.set_PO_Pomain_info("", "","")
            exec_line.set_Vendor_info("")
            exec_line.set_PU_ArrivalVouchs_info("","","")
            exec_line.set_PU_ArrivalVouch_info("", "")
            exec_line.set_rdrecords01_info("", "", "")
            exec_line.set_RdRecord01_info("", "")
            
            lst_exec_lines.append(exec_line)

    lst_qg_done = write_from_list1(lst_exec_lines,file_name)
    print("成功生成请购执行列表:",file_name)

    return lst_qg_done
