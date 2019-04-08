import wx 

ID_MENU_PRODUCT = wx.NewId()
ID_MENU_CUSTOMER = wx.NewId()
ID_MENU_EMPLOY = wx.NewId()
ID_MENU_PAYMENT = wx.NewId()




class SuperMarket(wx.Frame):
	def __init__(self,*args, **kwargs):
		super(SuperMarket,self).__init__(*args, **kwargs)
		panel = wx.Panel(self)
		panel.SetBackgroundColour('grey')
		self.Mbar()
	
	def Mbar(self):
	
		menubar=wx.MenuBar()
		
		#File Menu
		fileMenu=wx.Menu()
		fileMenu.Append(wx.ID_NEW,'&New')
		fileMenu.Append(wx.ID_OPEN,'&Open')
		fileMenu.Append(wx.ID_SAVE,'&Save')
		fileMenu.AppendSeparator()
		
		imp=wx.Menu()
		imp.Append(wx.ID_ANY,'Import files')
		imp.Append(wx.ID_ANY,'Import images')
		imp.Append(wx.ID_ANY,'Import audio or video')
		
		fileMenu.AppendMenu(wx.ID_ANY,'I&mport',imp)
		fileItem=fileMenu.Append(wx.ID_EXIT,'&Quit')
		
		
		self.Bind(wx.EVT_MENU,self.OnQuit,fileItem)
		
		#Edit Menu
		editMenu = wx.Menu()
		editMenu.Append(wx.ID_COPY,'&Copy')
		editMenu.Append(wx.ID_CUT,'&Cut')
		editMenu.Append(wx.ID_PASTE,'&Paste')
		editMenu.AppendSeparator()
		editMenu.Append(wx.ID_SELECTALL,'Select All')
		editMenu.Append(wx.ID_PREFERENCES,'Preferences')
		   
		#view menu
		viewMenu=wx.Menu()
		self.shtl=viewMenu.Append(wx.ID_ANY,'Show ToolBar',kind=wx.ITEM_CHECK)
		self.shst=viewMenu.Append(wx.ID_ANY,'Show StatusBar',kind=wx.ITEM_CHECK)
		
		viewMenu.Check(self.shtl.GetId(),True)
		viewMenu.Check(self.shst.GetId(),True)
		
		self.Bind(wx.EVT_MENU,self.ToggleToolBar,self.shtl)
		self.Bind(wx.EVT_MENU,self.ToggleStatusBar,self.shst)
		
		self.toolbar=self.CreateToolBar()
		self.toolbar.Realize()
		
		self.statusbar=self.CreateStatusBar()
		self.statusbar.SetStatusText('Ready')
		
		#tables
		tableMenu=wx.Menu()
		self.shpl=tableMenu.Append(wx.ID_ANY,'Product',kind=wx.ITEM_CHECK)
		self.shcl=tableMenu.Append(wx.ID_ANY,'Customer',kind=wx.ITEM_CHECK)
		self.shel=tableMenu.Append(wx.ID_ANY,'Employees',kind=wx.ITEM_CHECK)
		self.shpal=tableMenu.Append(wx.ID_ANY,'Paymemt',kind=wx.ITEM_CHECK)

		tableMenu.Check(self.shpl.GetId(),True)
		tableMenu.Check(self.shcl.GetId(),False)
		tableMenu.Check(self.shel.GetId(),False)
		tableMenu.Check(self.shpal.GetId(),False)

		self.Bind(wx.EVT_MENU,self.Onclicked1,self.shpl)
		self.Bind(wx.EVT_MENU,self.Onclicked2,self.shcl)		
		self.Bind(wx.EVT_MENU,self.Onclicked3,self.shel)
		self.Bind(wx.EVT_MENU,self.Onclicked4,self.shpal)		

		menubar.Append(fileMenu,'&File')
		menubar.Append(editMenu, '&Edit')
		menubar.Append(viewMenu,'&View')
		menubar.Append(tableMenu,'&Tables')
		self.SetMenuBar(menubar)
		
		self.SetSize((500,500))
		self.SetTitle('Super Market')
		self.Center()

	def Onclicked1(self,e):
		if self.shpl.IsChecked():
			self.shpl.Show()
			self.shcl.Hide()
			self.shel.Hide()
			self.shpal.Hide()

		vbox = wx.BoxSizer(wx.HORIZONTAL)
		btn1 = wx.Button(panel, label='Insert', size=(7, 3))
		btn2 = wx.Button(panel, label='Update', size=(7, 3))
		btn3 = wx.Button(panel, label='Delete', size=(7, 3))
		vbox.Add(btn1, wx.ID_ANY, wx.EXPAND | wx.ALL, border=1)
		vbox.Add(btn2, wx.ID_ANY, wx.EXPAND | wx.ALL, border=1)
		vbox.Add(btn3, wx.ID_ANY, wx.EXPAND | wx.ALL, border=1)
		panel.SetSizer(vbox)
	def Onclicked2(self,e):
	   	if self.shcl.IsChecked():
			self.shpl.Hide()
			self.shcl.Show()
			self.shel.Hide()
			self.shpal.Hide()

		vbox = wx.BoxSizer(wx.HORIZONTAL)
		btn1 = wx.Button(panel, label='Insert', size=(7, 3))
		btn2 = wx.Button(panel, label='Update', size=(7, 3))
		btn3 = wx.Button(panel, label='Delete', size=(7, 3))
		vbox.Add(btn1, wx.ID_ANY, wx.EXPAND | wx.ALL, border=1)
		vbox.Add(btn2, wx.ID_ANY, wx.EXPAND | wx.ALL, border=1)
		vbox.Add(btn3, wx.ID_ANY, wx.EXPAND | wx.ALL, border=1)
		panel.SetSizer(vbox)
	def Onclicked3(self,e):
	   	if self.shel.IsChecked():
			self.shpl.Hide()
			self.shcl.Hide()
			self.shel.Show()
			self.shpal.Hide()

		vbox = wx.BoxSizer(wx.HORIZONTAL)
		btn1 = wx.Button(panel, label='Insert', size=(7, 3))
		btn2 = wx.Button(panel, label='Update', size=(7, 3))
		btn3 = wx.Button(panel, label='Delete', size=(7, 3))
		vbox.Add(btn1, wx.ID_ANY, wx.EXPAND | wx.ALL, border=1)
		vbox.Add(btn2, wx.ID_ANY, wx.EXPAND | wx.ALL, border=1)
		vbox.Add(btn3, wx.ID_ANY, wx.EXPAND | wx.ALL, border=1)
		panel.SetSizer(vbox)
	def Onclicked4(self,e):
	   	if self.shpal.IsChecked():
			self.shpl.Hide()
			self.shcl.Hide()
			self.shel.Hide()
			self.shpal.Show()

		vbox = wx.BoxSizer(wx.HORIZONTAL)
		btn1 = wx.Button(panel, label='Insert', size=(7, 3))
		btn2 = wx.Button(panel, label='Update', size=(7, 3))
		btn3 = wx.Button(panel, label='Delete', size=(7, 3))
		vbox.Add(btn1, wx.ID_ANY, wx.EXPAND | wx.ALL, border=1)
		vbox.Add(btn2, wx.ID_ANY, wx.EXPAND | wx.ALL, border=1)
		vbox.Add(btn3, wx.ID_ANY, wx.EXPAND | wx.ALL, border=1)
		panel.SetSizer(vbox)
	def OnQuit(self,e):
		self.Close()
		
	def ToggleToolBar(self,e):
		if self.shtl.IsChecked():
			self.toolbar.Show()
		else:
			self.toolbar.Hide()
			
	def ToggleStatusBar(self,e):
		if self.shst.IsChecked():
			self.statusbar.Show()
		else:
			self.statusbar.Hide()
		
def main():
	app=wx.App()
	p=SuperMarket(None)
	p.Show()
	app.MainLoop()
	
if __name__ == '__main__':
	main()	
		
