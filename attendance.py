# -*- coding: utf-8 -*- 
import xdrlib
import sys
import xlrd
def open_excel(file= '20141224.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print (e)
#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file= '20141224.xls',colnameindex=1,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):

         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i] 
                list.append(app)
            #   print (i)
                if colnames[i]=='Name':
                    print (app[colnames[i]])
                elif  colnames[i]=='Total\nExtra Hours':
                    print (app[colnames[i]])
            #    print (colnames[i])
            #    print (app[colnames[i]])
           #  print (app)
    return list

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file= '20141224.xls',colnameindex=0,by_name=u'20141126--20141224'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数 
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list

def main():
   tables = excel_table_byindex()
#   tables.sort()
#   for row in tables:
#       print (row)

#   tables = excel_table_byname()
#   for row in tables:
#     print (row)

if __name__=="__main__":
    main()
