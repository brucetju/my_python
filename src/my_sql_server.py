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

	def searchwords(self,lst_word,tb_name = "",col_name = ""):
                '''
                找出某一字符出现的表/多个字符均出现的表
                lst_word 可以为一个值或多个值，类型为列表
                tb_name = "" 表示找所有的表
                col_name = ""表示找所有的列
                '''
                lst_search_tb_names = []
                lst_tb_names = [] #空列表，存放表名称

                file = open(lst_word[0]+".txt","w")
                with pymssql.connect(self.host_add, self.user_name, self.passwd, self.db_name,charset="utf8") as conn:
                        with conn.cursor(as_dict=True) as cursor:   # 数据存放到字典中
                                if(tb_name == ""):#搜索整个数据库
                                        cursor.execute('select name from sys.tables order by name')
                                        for row in cursor:
                                                lst_tb_names.append(row['name'])
                                        #print("total",str(len(lst_tb_names)),"tables in database.")
                                        lst_search_tb_names = lst_tb_names
                                else:
                                        lst_search_tb_names.append(tb_name)

                                tb_name2words = dict() #记录表中包含的搜索词，key=表名, value= 所在列名+所在行详细信息，字典，key为存在词， value为列名
                                
                                for current_tb_name in lst_search_tb_names: #枚举所有的表
                                        tb_name2words[current_tb_name] = dict()
                                        lst_search_col_names = []
                                        lst_col_names = []
                                        
                                        cmd = "select name from syscolumns where id=object_id('"+ current_tb_name + "')"
                                        cursor.execute(cmd)
                                        #print(cmd)
                                        for line in cursor:
                                                lst_col_names.append(line['name'])
                                        #print("total",str(len(lst_col_names)),"cols in",current_tb_name)
                                                
                                        if(col_name == ""):#搜索整张表
                                                lst_search_col_names = lst_col_names
                                        else:
                                                lst_search_col_names.append(col_name)

                                        for word in lst_word:
                                                tb_name2words[current_tb_name][word] = list()
                                                
                                                for col_index,current_col_name in enumerate(lst_search_col_names): #枚举所有的列
                                                        
                                                        cmd = "select " + "*" + " from "+ current_tb_name +" where "+ str(current_col_name) +" like '%"+word+"%'"
                                                        try:
                                                                #print(cmd)
                                                                cursor.execute(cmd)
                                                                for line in cursor:
                                                                        #print("find with cmd:",cmd)
                                                                        all_info = "find " + word + "in col:" + current_col_name+":\r\n"
                                                                        for index,col in enumerate(lst_col_names):
                                                                                all_info += "||" + str(index) +":" + str(col) + ":" + str(line[col]) + "\r\n"
                                                                      
                                                                        tb_name2words[current_tb_name][word].append(all_info)
                                                        except Exception as e:
                                                                pass
                                                                print("error cmd: ",cmd)
                                for tb_name in tb_name2words:
                                        count = 0
                                        for word in lst_word:
                                                if(len(tb_name2words[tb_name][word]) != 0):
                                                        count += 1
                                        if(count==len(lst_word)):
                                                print("found all words in ",tb_name)
                                                file.write("found all words in " + tb_name)
                                                for word in lst_word:
                                                        for item in tb_name2words[tb_name][word]:
                                                                print(item)
                                                                file.write(item)
																
                file.close()
