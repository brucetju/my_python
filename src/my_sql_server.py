import pymssql

class SQL_Server():
	"sql server"
	def __init__(self,host_add,user_name,passwd,db_name):
		self.host_add = host_add
		self.user_name = user_name
		self.passwd = passwd
		self.db_name = db_name
		
	def readinto_list(self,tb_name,lst_cols,inc_col = "",desc_col = ""):
		"从对应表单中选择需要的列,并将每一行当成一个元素放入对应的列表中"
		select_items = ""
		for index,item in enumerate(lst_cols):
			select_items += item
			if (index != len(lst_cols) -1):#最后一项后不需要添加，
				select_items += ","
		
		lst_all_values = list()
		with pymssql.connect(self.host_add, self.user_name, self.passwd, self.db_name,charset="utf8") as conn:
			with conn.cursor(as_dict=True) as cursor:
				cmd = "select "+ select_items +" from " + tb_name
				if(inc_col != ""):
					cmd +=  " order by "+inc_col+" "
				if(desc_col != ""):
					cmd +=  " order by "+desc_col+" DESC"
				
				#if(tb_name == 'PU_AppVouchs'):#处理PO_Detail表时，根据请购单号进行排序
				#	cmd += " order by AutoID DESC"#" order by cbsysbarcode DESC"
				cursor.execute(cmd)
				print(cmd)
				for line in cursor:
					lst_all_values.append(line)
		print("find items num:",str(len(lst_all_values)))
		return lst_all_values