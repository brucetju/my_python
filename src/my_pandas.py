import pymssql
conn = pymssql.connect(server="192.168.1.60",user="sa",password="ADMINadmin2018",database="UFDATA_003_2017")

import pandas as pd

sql = "select * from BN_BizNotify_Log"
df0 = pd.read_sql(sql,conn)
df=pd.DataFrame(df0)
