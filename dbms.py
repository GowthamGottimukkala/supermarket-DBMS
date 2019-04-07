import wx 



class SuperMarket(wx.Frame):
	def __init__(self,*args, **kwargs):
		super(SuperMarket,self).__init__(*args, **kwargs)
		
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
		
				
		menubar.Append(fileMenu,'&File')
		menubar.Append(editMenu, '&Edit')
		menubar.Append(viewMenu,'&View')
		self.SetMenuBar(menubar)
		
		
		
		self.SetSize((500,500))
		self.SetTitle('Super Market')
		self.Center()
		
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
	
		
