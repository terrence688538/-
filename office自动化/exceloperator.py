from 自动化.UI.noname import ExcelOperator
import xlwings as xw
from xlwings.constants import AutoFillType
import wx
import datetime
class MyFrame(ExcelOperator):                 #类的继承
    def __init__(self,parent):
        ExcelOperator.__init__(self,parent)            #调用父类的__init__() 方法进行初始化
    def OpenExcelFile(self,file):
        self.app=xw.App(visible=True,add_book=False)
        self.app.display_alerts=True
        self.app.screen_updating=True
        self.wb=self.app.books.open(file)
        self.sheet=self.wb.sheets['sheet1']
    def LoadDataFromeRow(self,address):
        result=self.sheet[address].value
        return result
    def SaveDataToRow(self,address,data):
        self.sheet[address].value=data
    def m_button1OnButtonClick(self,event):
        print(self.LoadDataFromeRow('A1'))
        self.m_textCtrl1.Value=str(self.LoadDataFromeRow('B1'))
    def m_button2OnButtonClick(self, event):
        data = self.m_textCtrl2.Value
        self.SaveDataToRow('E1',data)
    def m_button3OnButtonClick( self, event ):
        self.DragAndDropFormulaToRow('sheet1',147,'d')
    def DragAndDropFormulaToRow(self,sheetName,row,columns):
        self.sheet=self.wb.sheets[sheetName]
        address=columns+str(row-1)
        rowDrawDown='{0}{1}:{2}{3}'.format(columns,row-1,columns,row)
        self.sheet.range(address).api.AutoFIll(self.sheet.range(rowDrawDown).api,AutoFillType.xlFillDefault)#AutoFillType.xlFillDefault是填充方式
    def CloseExcel(self):
        self.wb.save()
        self.wb.close()
        self.app.quit()
        exit()
    def ExcelOperatorOnClose( self, event ):
        self.CloseExcel()