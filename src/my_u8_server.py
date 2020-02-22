

class U8_Server():
	"U8系统中的表，列对应的值"

	#PO_Podetails:id == rdrecords01:iPOsID == PU_ArrivalVouchs:iPOsID

	def __init__(self):
		# 物料 code -> name
		self.Inventory = 'Inventory'#存货档案
		self.Inventory_code = 'cInvCode'#存货编码
		self.Inventory_name = 'cInvName'#存货名称
		self.Inventory_keys = [self.Inventory_code,self.Inventory_name]

		# 请购人 code -> name
		self.Person = 'Person'#职员档案
		self.Person_code = 'cPersonCode'
		self.Person_name = 'cPersonName'
		self.Person_keys = [self.Person_code,self.Person_name]

		# 供应商 code -> name
		self.Vendor = 'Vendor'#供应商信息
		self.Vendor_code = 'cVenCode'
		self.Vendor_name = 'cVenAbbName'
		self.Vendor_keys = [self.Vendor_code,self.Vendor_name]

		#逐行读取信息，从该表中记录请购单号，行标识，物料编码
		self.PU_AppVouchs = 'PU_AppVouchs'#请购单子表
		self.PU_AppVouchs_AutoID = 'AutoID' #采购请购单子表标识 *
		self.PU_AppVouchs_cbsysbarcode = 'cbsysbarcode' #包括请购单号 cbsysbarcode:||pupr|JHT-QG200211006|9 [7:22] [23:]		
		self.PU_AppVouchs_cInvCode = 'cInvCode' #物料编码		
		self.PU_AppVouchs_dRequirDate = 'dRequirDate' #需求时间
		self.PU_AppVouchs_fQuantity = 'fQuantity' #需求数量
		self.PU_AppVouchs_cDefine22 = 'cDefine22' #批次信息
		self.PU_AppVouchs_keys = [self.PU_AppVouchs_AutoID,self.PU_AppVouchs_cInvCode,self.PU_AppVouchs_cbsysbarcode,self.PU_AppVouchs_dRequirDate,self.PU_AppVouchs_fQuantity,self.PU_AppVouchs_cDefine22]

		#由请购单号映射请购人,请购等级,制表时间,审核时间
		self.PU_AppVouch = 'PU_AppVouch'#请购单主表
		self.PU_AppVouch_cCode = 'cCode' #请购单号 "key"
		self.PU_AppVouch_cPersonCode = 'cPersonCode' #请购人
		self.PU_AppVouch_cDefine11 = 'cDefine11' #优先，紧急？
		self.PU_AppVouch_cMakeTime = 'cMakeTime' #制表时间
		self.PU_AppVouch_cAuditTime = 'cAuditTime' #审批时间
		self.PU_AppVouch_keys = [self.PU_AppVouch_cCode,self.PU_AppVouch_cPersonCode,self.PU_AppVouch_cDefine11,self.PU_AppVouch_cMakeTime,self.PU_AppVouch_cAuditTime]

		#由采购订单子表标识映射采购订单号,计划到货日期,请购数量
		self.PO_Podetails = 'PO_Podetails'#采购订单信息，子表
		self.PO_Podetails_iAppIds = 'iAppIds' #采购订单子表标识 "key"
		self.PO_Podetails_ID = 'ID' #采购订单子表标识 "key"
		self.PO_Podetails_cbsysbarcode = 'cbsysbarcode' #中包含采购单号
		self.PO_Podetails_iQuantity = 'iQuantity' #采购数量
		self.PO_Podetails_dArriveDate = 'dArriveDate'  #计划到货日期
		self.PO_Podetails_cupsocode = 'cupsocode' #请购单号 not used
		self.PO_Podetails_cInvCode = 'cInvCode' #物料编码		
		self.PO_Podetails_keys = [self.PO_Podetails_iAppIds,self.PO_Podetails_ID,self.PO_Podetails_cbsysbarcode,self.PO_Podetails_iQuantity,self.PO_Podetails_dArriveDate,self.PO_Podetails_cupsocode,self.PO_Podetails_cInvCode]

		#由采购订单号映射制单/审核时间，供应商
		self.PO_Pomain = 'PO_Pomain'#请购订单信息总表
		self.PO_Pomain_cPOID = 'cPOID' #采购单号 "key"
		self.PO_Pomain_cmaketime = 'cmaketime' #采购单创建时间
		self.PO_Pomain_cVenCode = 'cVenCode' #供应商代码
		self.PO_Pomain_cAuditTime = 'cAuditTime' #采购审核时间
		#self.PO_Pomain_cPersonCode = 'cPersonCode' #请购人
		#self.PO_Pomain_cappcode = 'cappcode' #请购单号
		self.PO_Pomain_keys = [self.PO_Pomain_cPOID,self.PO_Pomain_cmaketime,self.PO_Pomain_cVenCode,self.PO_Pomain_cAuditTime]

		#由采购订单子表标识为key统计到货单号，可以为多个。统计每一个的到货单号，到货数量
		self.PU_ArrivalVouchs = 'PU_ArrivalVouchs'#采购到货单子表
		self.PU_ArrivalVouchs_iPOsID = 'iPOsID' #采购订单子表标识 "key"
		self.PU_ArrivalVouchs_Autoid = 'Autoid' #
		self.PU_ArrivalVouchs_cbsysbarcode = 'cbsysbarcode' #包含到货单号  cbsysbarcode:||pudh|JHT-DHQC20011705|1 [7:23]
		self.PU_ArrivalVouchs_iQuantity = 'iQuantity' #数量
		#self.PU_ArrivalVouchs_cInvCode = 'cInvCode' #物料编码
		#self.PU_ArrivalVouchs_cordercode = 'cordercode' #采购单号
		self.PU_ArrivalVouchs_keys = [self.PU_ArrivalVouchs_iPOsID,self.PU_ArrivalVouchs_Autoid,self.PU_ArrivalVouchs_cbsysbarcode,self.PU_ArrivalVouchs_iQuantity]

		#由到货单号映射制表/审核时间,唯一关系
		self.PU_ArrivalVouch = 'PU_ArrivalVouch'#采购到货主表
		self.PU_ArrivalVouch_cCode = 'cCode' #到货单号
		self.PU_ArrivalVouch_cMakeTime = 'cMakeTime' #到货制表时间
		self.PU_ArrivalVouch_caudittime = 'caudittime' #到货审批时间
		self.PU_ArrivalVouch_keys = [self.PU_ArrivalVouch_cCode,self.PU_ArrivalVouch_cMakeTime,self.PU_ArrivalVouch_caudittime]

		#由到货单号映射入库单号及入库数量,唯一关系
		self.rdrecords01 = 'rdrecords01'#采购入库单子表
		self.rdrecords01_iArrsId = 'iArrsId' #
		self.rdrecords01_cbarvcode = 'cbarvcode' #到货单号
		self.rdrecords01_cbsysbarcode = 'cbsysbarcode' #包含入库单号，cbsysbarcode:||st01|JHT-CGRK200118107|2 [7:24][25:0]
		self.rdrecords01_iQuantity = 'iQuantity' #入库数量
		#self.rdrecords01_cInvCode = 'cInvCode' #物料编码
		#self.rdrecords01_chVencode = 'chVencode' #供应商编码
		#self.rdrecords01_cPOID = 'cPOID' #采购单号
		#self.rdrecords01_iPOsID = 'iPOsID' #采购订单子表标识 不唯一，可能同一ID对应多个到货/入库单号
		self.rdrecords01_keys = [self.rdrecords01_iArrsId,self.rdrecords01_cbarvcode,self.rdrecords01_cbsysbarcode,self.rdrecords01_iQuantity]

		#由入库单号映射制单/审核时间
		self.RdRecord01 = 'RdRecord01'#采购入库单主表
		self.RdRecord01_cCode = 'cCode' #入库单号
		self.RdRecord01_dnmaketime = 'dnmaketime' #制单日期
		self.RdRecord01_dnverifytime = 'dnverifytime' #审核时间
		#self.RdRecord01_cOrderCode = 'cOrderCode' #采购单号
		#self.RdRecord01_cARVCode = 'cARVCode' #到货单号
		#self.RdRecord01_dARVDate = 'dARVDate' #到货日期
		self.RdRecord01_keys = [self.RdRecord01_cCode,self.RdRecord01_dnmaketime,self.RdRecord01_dnverifytime]
		

class ExecLine():
    """
    对应请购执行列表中的每一行,
    PO_Podetails 表中的cupsocode为请购单号，请购单号重复时，创建多个对象
    """
    def __init__(self,qg_code,qg_sub_code):
        self.qg_code = qg_code #请购单号 PO_Podetails:cupsocode,PO_Pomain:cappcode
        self.qg_sub_code = qg_sub_code # 请购单子编号

    def set_Inventory_info(self,wl_name):#通过物料编码
        self.wl_name = wl_name #Inventory:cInvName

    def set_Person_info(self,qg_person_name):
        self.qg_person_name = qg_person_name

    def set_Vendor_info(self,cg_vender_name):
        self.cg_vender_name = cg_vender_name

    def set_Pu_AppVouchs_info(self,wl_code,wl_quant,xq_date,pc_code):
        self.wl_code = wl_code #物料编码
        self.wl_quant = wl_quant #物料需求量
        self.xq_date = xq_date #需求日期
        self.pc_code = pc_code #批次信息

    def set_PU_AppVouch_info(self, qg_zd_time, qg_sh_time, qg_dj, qg_person_code):
        self.qg_zd_time = qg_zd_time  # 请购制单时间
        self.qg_sh_time = qg_sh_time  # 请购审核时间
        self.qg_dj = qg_dj  # 请购优先等级
        self.qg_person_code = qg_person_code  # 请购人

    def set_PO_Podetails_info(self,cg_code,cg_sub_code,cg_jh_time,cg_quant):#通过请购单号
        self.cg_code = cg_code #po_pomain:cpoid(采购订单号) 需要做处理: cbsysbarcode:||pupo|jht-cg20010230|1
        self.cg_sub_code = cg_sub_code
        self.cg_jh_time = cg_jh_time #计划到货日期
        self.cg_quant = cg_quant
		
    def set_PO_Pomain_info(self,cg_dd_date,cg_vendor_code,cg_sh_date):#通过请购单号
        self.cg_dd_date = cg_dd_date
        self.cg_vendor_code = cg_vendor_code
        self.cg_sh_date = cg_sh_date
        pass
    
    def set_PU_ArrivalVouchs_info(self,dh_code,dh_sub_code,dh_quant):
        self.dh_code = dh_code
        self.dh_sub_code = dh_sub_code
        self.dh_quant = dh_quant

    def set_PU_ArrivalVouch_info(self,dh_zd_time,dh_sh_time):
        self.dh_zd_time = dh_zd_time
        self.dh_sh_time = dh_sh_time

    def set_rdrecords01_info(self,rk_code,rk_sub_code,rk_quant):
        self.rk_code = rk_code
        self.rk_sub_code = rk_sub_code
        self.rk_quant = rk_quant
        pass
    
    def set_RdRecord01_info(self,rk_zd_time,rk_sh_time):
        self.rk_zd_time = rk_zd_time #RdRecord01：dnmaketime
        self.rk_sh_time = rk_sh_time #RdRecord01：dnverifytime
        pass

    def set_BN_BizNotify_Log_info(self):
        pass

    def get_col_names():
        first_line = ['请购单号', "子单号", '请购日期', "审核日期", "请购人", "请购等级", '物料编码', '物料名称', '需求日期', '需求数量', '批次信息', \
                      '采购单号', "子单号", '订单日期', "计划日期", '采购供应商', '采购审核日期', '采购数量', \
                      '到货单号', '子单号', '到货制单时间', '到货审核时间', '到货数量', "需求数量", \
                      '仓库入库单号', '子单号', '入库制单时间', '入库审核时间', '入库数量', "需求数量"]
        return first_line

    def get_info(self):
        values = list();
        values.append(self.qg_code)
        values.append(self.qg_sub_code)
        values.append(str(self.qg_zd_time)[0:10])
        values.append(str(self.qg_sh_time)[0:10])
        values.append(self.qg_person_name)
        values.append(self.qg_dj)
        values.append(self.wl_code)
        values.append(self.wl_name)
        values.append(str(self.xq_date)[0:10])
        values.append(self.wl_quant)
        values.append(self.pc_code)
        values.append(self.cg_code)
        values.append(self.cg_sub_code)
        values.append(str(self.cg_dd_date)[0:10])
        values.append(str(self.cg_jh_time)[0:10])
        values.append(self.cg_vender_name)
        values.append(str(self.cg_sh_date)[0:10])
        values.append(self.cg_quant)
        values.append(self.dh_code)
        values.append(self.dh_sub_code)
        values.append(str(self.dh_zd_time)[0:10])
        values.append(str(self.dh_sh_time)[0:10])
        values.append(self.dh_quant)
        values.append(self.wl_quant)
        values.append(self.rk_code)
        values.append(self.rk_sub_code)
        values.append(str(self.rk_zd_time)[0:10])
        values.append(str(self.rk_sh_time)[0:10])
        values.append(self.rk_quant)
        values.append(self.wl_quant)
        return values
