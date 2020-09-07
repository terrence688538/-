import xlwings as xw

# 设为程序可见， 不新建工作薄
#app = xw.App(visible=True, add_book=False)

wb = xw.Book()          # 新建文档，保存
wb.save(r'C:\Users\Mechrevo\Desktop\test.xlsx')
wb=xw.Book(r'C:\Users\Mechrevo\Desktop\test.xlsx')        #打开
sht0 = wb.sheets[0]        #  进入第一张工作表
sht0.range('A1').value = '人生'
# 取单元格值
value = sht0.range('A1').value
# 获取已打开的文档的单元格值，不需要实例化，文档没打开会报错
value_1 = xw.Range('A1').value
# 获取已打开的文档名
wb = xw.books.active

# 取列表值
list_value = sht0.range('A1:B2').value            #表的左上和右下确定范围

# 批量写入 从左上角A1开始
titles = [['时间', '地点', '人'], [1, 2, 3]]
sht0.range('C1').value = titles
# 写入列有两种方法
sht0.range('A4').options(transpose=True).value = [1,2,3,4]
titles = [[1], [2], [3], [4]]
# 批量插入单元格，和插入数据
for i in range(5):
    sht0.range('a1:c4').api.Insert()           #插入
    sht0.range('a1').value = titles

sht0.range('d8').value = titles
sht0.range('a1:c4').api.Insert()
# 保存，关闭，结束进程
wb.save(path=None)
wb.close()
#app.quit()

# 清除sheet的内容和格式
sht0.clear()

# 加入超链接
a1 = xw.Range('A1')
a1.add_hyperlink(r'www.baidu.com', '百度', '提示：点击即链接到百度')

a1.color = (255, 255, 255)

# 获取超链接
hyperlink = a1.hyperlink

# 新建工作薄，sheet
xw.books.add()
xw.sheets.add()


wb=xw.Book(r'D:\资源\数据科学\机器学习实战\回归\longley.xlsx')                 #建立excel表连接,自动打开表
sht = wb.sheets["vvv"]                #实例化工作表对象
wb.fullname                    #返回绝对路径
sht.range("A1:D1").api.font.size = 15  # 设置单元格字体大小
sht.range("A1:C3").api.font.name = "微软雅黑"  # 设置字体
sht.range("A1").api.font.bold = True  # 设置单元格字体是否加粗
sht.range("A1").api.font.color = 0x0000FF  # 设置字体颜色
print(sht.range("A1").api.font.name)  # 返回指定单元格中字体的名字，默认为 宋体
sht.range("A1:D1").api.HorizontalAlignment = -4131  # -4108 水平居中。 -4131 靠左，-4152 靠右
sht.range("A14:B14").api.merge()  # 进行单元格合并
sht.range("A14").api.unmerge()  # 取消合并单元格
"""设置边框"""
# Borders(9) 底部边框，LineStyle = 1 直线。
b3 = sht.range('b3')
b3.api.Borders(9).LineStyle = 1
b3.api.Borders(9).Weight = 3                # 设置边框粗细。

# Borders(7) 左边框，LineStyle = 2 虚线。
b3.api.Borders(7).LineStyle = 2
b3.api.Borders(7).Weight = 3

# Borders(8) 顶部框，LineStyle = 5 双点划线。
b3.api.Borders(8).LineStyle = 5
b3.api.Borders(8).Weight = 3

# Borders(10) 右边框，LineStyle = 4 点划线。
b3.api.Borders(10).LineStyle = 4
b3.api.Borders(10).Weight = 3

# Borders(5) 单元格内从左上角 到 右下角。
b3.api.Borders(5).LineStyle = 1
b3.api.Borders(5).Weight = 3

# Borders(6) 单元格内从左下角 到 右上角。
b3.api.Borders(6).LineStyle = 1
b3.api.Borders(6).Weight = 3

"""如果是一个区域的单元格，内部边框设置如下"""
# # Borders(11) 内部垂直边线。
# b3.api.Borders(11).LineStyle = 1
# b3.api.Borders(11).Weight = 3
#
# # Borders(12) 内部水平边线。
# b3.api.Borders(12).LineStyle = 1
# b3.api.Borders(12).Weight = 3

sht.name                         #返回工作部的名字
sht.range('A1').value = "xlwings"    #在单元格写东西
sht.range('B5').value='daidai'
sht.range('A1').clear()                #清空单元格内容
sht.range('A1').column         #返回列数
sht.range('F5').column
sht.range('A1').row           #返回行数
sht.range('B6').row

sht.range('A1').row_height   #行高
sht.range('A1').column_width  #列宽

sht.range('A1').columns.autofit()       #列宽自适应
sht.range('B5').columns.autofit()

sht.range('B5').rows.autofit()         #行高自适应
sht.range('A1:A11').color = (34,139,34)         #格子上颜色
sht.range('B5').color =(255,242,204)
sht.range('B5').color                     #获取颜色
sht.range('A1').color = None            #清除单元格颜色

sht.range('D6').formula='=SUM(B6:B7)'         #输入公式，相应单元格会出现计算结果
sht.range('D1').formula_array                 #获取单元格公式

sht.range('D2').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0],[10.0, 20.0, 30.0]]  #在单元格中写入批量数据，只需要指定起始单元格位置即可

sht.range('D2').expand().value            #读取表中批量数据，使用expand()方法


xw.Range("E1").value = "r'D:\资源\数据科学\机器学习实战\回归\longley.xlsx'"

import numpy as np

np_data = np.array((1,2,3))
sht.range('F1').value = np_data     #以F1为起点

import pandas as pd
df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])
sht.range('B17').value = df

aaa=sht.range('H8').options(pd.DataFrame,expand='table').value

import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot([1, 2, 3, 4, 5])
sht.pictures.add(fig, name='MyPlot', update=True)


#另一种读取方法
app=xw.App(visible=True,add_book=False)
wb=app.books.add()
wb.sheets.add()
wb=app.books.open(r'C:\Users\Mechrevo\Desktop\test.xlsx')
wb.close()
app.quit()

sht1=wb.sheets['Sheet1']
sht1.range('A3').value='呆头'
aa=xw.books.active
rng=sht1['A1:B5']
sht1.delete()















