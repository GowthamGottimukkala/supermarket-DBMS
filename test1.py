import wx 

ID_MENU_PRODUCT = wx.NewId()
ID_MENU_CUSTOMER = wx.NewId()
ID_MENU_EMPLOY = wx.NewId()
ID_MENU_PAYMENT = wx.NewId()

class SuperMarket(wx.Frame):
	def __init__(self,*args, **kwargs):
		super(SuperMarket,self).__init__(*args, **kwargs)
		
		self.Mbar()
	
	def Mbar(self):
	
		menubar=wx.MenuBar()
		#tables
		tableMenu=wx.Menu()
		tableMenu.Append(ID_MENU_PRODUCT,'Product')
		tableMenu.Append(ID_MENU_CUSTOMER,'Customer')
		tableMenu.Append(ID_MENU_EMPLOY,'Employees')
		tableMenu.Append(ID_MENU_PAYMENT,'Paymemt')

		self.Bind(wx.EVT_MENU,self.Onclicked,id=ID_MENU_PRODUCT)
		self.Bind(wx.EVT_MENU,self.Onclicked,id=ID_MENU_CUSTOMER)		
		self.Bind(wx.EVT_MENU,self.Onclicked,id=ID_MENU_EMPLOY)
		self.Bind(wx.EVT_MENU,self.Onclicked,id=ID_MENU_PAYMENT)		

		menubar.Append(tableMenu,'&Tables')
		self.SetMenuBar(menubar)
		
		self.SetSize((500,500))
		self.SetTitle('Super Market')
		self.Center()

	def Onclicked(self,e):
		panel = wx.Panel(self, size=(300,300))
		panel.SetBackgroundColour('#4f5049')
		vbox = wx.BoxSizer(wx.VERTICAL)
		hbox4 = 
		hbox5 = wx.BoxSizer(wx.HORIZONTAL)
		btn1 = wx.Button(panel, label='Ok', size=(70, 30))
		hbox5.Add(btn1)
		btn2 = wx.Button(panel, label='Close', size=(70, 30))
		hbox5.Add(btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
		vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
		
		panel.SetSizer(vbox)
			
	def OnQuit(self,e):
		self.Close()
		
def main():
	app=wx.App()
	p=SuperMarket(None)
	p.Show()
	app.MainLoop()
	
if __name__ == '__main__':
	main()	
		
