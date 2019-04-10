import wx 
import random


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
	
		panel = wx.Panel(self)

		notebook = wx.Notebook(panel)
		tabOne = TabPanel(notebook)
		notebook.AddPage(tabOne, "Table 1")

		tabTwo = TabPanel2(notebook)
		notebook.AddPage(tabTwo, "Table 2")

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
		panel.SetSizer(sizer)
		self.Layout()

		self.Show()
		
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



class TabPanel(wx.Panel):
	#----------------------------------------------------------------------
	def __init__(self, parent):
		""""""
		wx.Panel.__init__(self, parent=parent)

		colors = ["red", "blue", "gray", "yellow", "green"]
		self.SetBackgroundColour(random.choice(colors))

		btn = wx.Button(self, label="insert")
		btn2 = wx.Button(self, label="delete")
		btn3 = wx.Button(self, label="update")
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer.Add(btn, 0, wx.ALIGN_LEFT|wx.ALL, 10)
		sizer.Add(btn2, 0, wx.ALIGN_LEFT|wx.ALL, 10)
		sizer.Add(btn3, 0, wx.ALIGN_LEFT|wx.ALL, 10)
		self.SetSizer(sizer)
class TabPanel2(wx.Panel):
	#----------------------------------------------------------------------
	def __init__(self, parent):
		""""""
		wx.Panel.__init__(self, parent=parent)

		colors = ["red", "blue", "gray", "yellow", "green"]
		self.SetBackgroundColour(random.choice(colors))

		btn = wx.Button(self, label="insert")
		btn2 = wx.Button(self, label="delete")
		btn3 = wx.Button(self, label="update")
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer.Add(btn, 0, wx.ALIGN_LEFT|wx.ALL, 10)
		sizer.Add(btn2, 0, wx.ALIGN_LEFT|wx.ALL, 10)
		sizer.Add(btn3, 0, wx.ALIGN_LEFT|wx.ALL, 10)
		self.SetSizer(sizer)
'''class DemoFrame(wx.Frame):
	"""
	Frame that holds all other widgets
	"""

	def __init__(self):
		"""Constructor"""        
		wx.Frame.__init__(self, None, wx.ID_ANY, 
						  "Notebook Tutorial",
						  size=(600,400)
						  )
		panel = wx.Panel(self)

		notebook = wx.Notebook(panel)
		tabOne = TabPanel(notebook)
		notebook.AddPage(tabOne, "Table 1")

		tabTwo = TabPanel2(notebook)
		notebook.AddPage(tabTwo, "Table 2")

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
		panel.SetSizer(sizer)
		self.Layout()

		self.Show()'''




		
def main():
	app=wx.App()
	p=SuperMarket(None)
	p.Show()
	#frame = DemoFrame()
	app.MainLoop()
	
if __name__ == '__main__':
	main()
	
		
