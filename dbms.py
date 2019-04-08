import wx
import random


class SuperMarket(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(SuperMarket, self).__init__(*args, **kwargs)
        self.Mbar()
        self.SetPosition((20, 20))
        self.SetTitle('Super Market')
        self.Center()
        # self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)

    def Mbar(self):
        menubar = wx.MenuBar()
        # File Menu
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW, '&New')
        fileMenu.Append(wx.ID_OPEN, '&Open')
        fileMenu.Append(wx.ID_SAVE, '&Save')
        fileMenu.AppendSeparator()

        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import files')
        imp.Append(wx.ID_ANY, 'Import images')
        imp.Append(wx.ID_ANY, 'Import audio or video')

        fileMenu.AppendMenu(wx.ID_ANY, 'I&mport', imp)
        fileItem = fileMenu.Append(wx.ID_EXIT, '&Quit')

        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

        # Edit Menu
        editMenu = wx.Menu()
        editMenu.Append(wx.ID_COPY, '&Copy')
        editMenu.Append(wx.ID_CUT, '&Cut')
        editMenu.Append(wx.ID_PASTE, '&Paste')
        editMenu.AppendSeparator()
        editMenu.Append(wx.ID_SELECTALL, 'Select All')
        editMenu.Append(wx.ID_PREFERENCES, 'Preferences')

        # view menu
        viewMenu = wx.Menu()
        self.shtl = viewMenu.Append(
            wx.ID_ANY, 'Show ToolBar', kind=wx.ITEM_CHECK)
        self.shst = viewMenu.Append(
            wx.ID_ANY, 'Show StatusBar', kind=wx.ITEM_CHECK)

        viewMenu.Check(self.shtl.GetId(), True)
        viewMenu.Check(self.shst.GetId(), True)

        self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.shtl)
        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shst)

        self.toolbar = self.CreateToolBar()
        self.toolbar.Realize()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')

        # tableMenu
        tableMenu = wx.Menu()
        tableItem1 = tableMenu.Append(
            wx.ID_ANY, 'Products')
        tableItem2 = tableMenu.Append(
            wx.ID_ANY, 'Customers')
        tableItem3 = tableMenu.Append(
            wx.ID_ANY, 'Employees')
        tableItem4 = tableMenu.Append(
            wx.ID_ANY, 'Payment')

        # tableMenu.Check(self.tableItem1.GetId(), False)
        # tableMenu.Check(self.tableItem2.GetId(), False)
        # tableMenu.Check(self.tableItem3.GetId(), False)
        # tableMenu.Check(self.tableItem4.GetId(), False)

        self.Bind(wx.EVT_MENU, self.Onclicked1, tableItem1)
        self.Bind(wx.EVT_MENU, self.Onclicked1, tableItem2)
        self.Bind(wx.EVT_MENU, self.Onclicked1, tableItem3)
        self.Bind(wx.EVT_MENU, self.Onclicked1, tableItem4)

        menubar.Append(fileMenu, '&File')
        menubar.Append(editMenu, '&Edit')
        menubar.Append(viewMenu, '&View')
        menubar.Append(tableMenu, '&Tables')
        self.SetMenuBar(menubar)

    def Onclicked1(self, e):
       # panel = wx.Panel(self)
       # panel.SetBackgroundColour('grey')
       #  hbox5 = wx.BoxSizer(wx.HORIZONTAL)
      #  btn1 = wx.Button(panel, label='Insert', size=(70, 30))
       # hbox5.Add(btn1)
      #  btn2 = wx.Button(panel, label='Update', size=(70, 30))
      #  hbox5.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=5)
       # vbox.Add(hbox5, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)
   #     panel.SetSizer(vbox)
   
        wx.Panel.__init__(self)

        colors = ["red", "blue", "gray", "yellow", "green"]
        self.SetBackgroundColour(random.choice(colors))


        btn = wx.Button(self, label="table")
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(btn, 0, wx.ALL, 10)
        self.SetSizer(sizer)
        wx.Frame.__init__(self, None, wx.ID_ANY,
        "Notebook Tutorial",
        size=(600,400))
                          
        panel = wx.Panel(self)

        notebook = wx.Notebook(panel)
        tabOne = TabPanel(notebook)
        notebook.AddPage(tabOne, "Tab 1")

        tabTwo = TabPanel(notebook)
        notebook.AddPage(tabTwo, "Tab 2")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        panel.SetSizer(sizer)
        self.Layout()

        self.Show()

    # def Onclicked2(self, e):
    #     panel = wx.Panel(self)
    #     panel.SetBackgroundColour('red')
    #     vbox = wx.BoxSizer(wx.VERTICAL)
    #     hbox5 = wx.BoxSizer(wx.HORIZONTAL)
    #     btn1 = wx.Button(panel, label='Insert', size=(70, 30))
    #     hbox5.Add(btn1)
    #     btn2 = wx.Button(panel, label='Update', size=(70, 30))
    #     hbox5.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=5)
    #     vbox.Add(hbox5, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)
    #     panel.SetSizer(vbox)

    # def Onclicked3(self, e):
    #     panel = wx.Panel(self)
    #     panel.SetBackgroundColour('yellow')
    #     vbox = wx.BoxSizer(wx.VERTICAL)
    #     hbox5 = wx.BoxSizer(wx.HORIZONTAL)
    #     btn1 = wx.Button(panel, label='Insert', size=(70, 30))
    #     hbox5.Add(btn1)
    #     btn2 = wx.Button(panel, label='Update', size=(70, 30))
    #     hbox5.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=5)
    #     vbox.Add(hbox5, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)
    #     panel.SetSizer(vbox)

    # def Onclicked4(self, e):
    #     panel = wx.Panel(self)
    #     panel.SetBackgroundColour('white')
    #     vbox = wx.BoxSizer(wx.VERTICAL)
    #     hbox5 = wx.BoxSizer(wx.HORIZONTAL)
    #     btn1 = wx.Button(panel, label='Insert', size=(70, 30))
    #     hbox5.Add(btn1)
    #     btn2 = wx.Button(panel, label='Update', size=(70, 30))
    #     hbox5.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=5)
    #     vbox.Add(hbox5, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)
    #     panel.SetSizer(vbox)

    def OnQuit(self, e):
        self.Close()

    def ToggleToolBar(self, e):
        if self.shtl.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()

    def ToggleStatusBar(self, e):
        if self.shst.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()


def main():
    app = wx.App()
    p = SuperMarket(None)
    p.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
