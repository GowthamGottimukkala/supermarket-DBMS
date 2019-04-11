import wx
import random


class LoginDialog(wx.Dialog):
    """
    Class to define login dialog
    """

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Dialog.__init__(self, None, title="Login")
        self.logged_in = False

        # user info
        user_sizer = wx.BoxSizer(wx.HORIZONTAL)

        user_lbl = wx.StaticText(self, label="Username:")
        user_sizer.Add(user_lbl, 0, wx.ALL | wx.CENTER, 5)
        self.user = wx.TextCtrl(self)
        user_sizer.Add(self.user, 0, wx.ALL, 5)

        # pass info
        p_sizer = wx.BoxSizer(wx.HORIZONTAL)

        p_lbl = wx.StaticText(self, label="Password:")
        p_sizer.Add(p_lbl, 0, wx.ALL | wx.CENTER, 5)
        self.password = wx.TextCtrl(
            self, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        self.password.Bind(wx.EVT_TEXT_ENTER, self.onLogin)
        p_sizer.Add(self.password, 0, wx.ALL, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(user_sizer, 0, wx.ALL, 5)
        main_sizer.Add(p_sizer, 0, wx.ALL, 5)

        btn = wx.Button(self, label="Login")
        btn.Bind(wx.EVT_BUTTON, self.onLogin)
        main_sizer.Add(btn, 0, wx.ALL | wx.CENTER, 5)

        self.SetSizer(main_sizer)

    # ----------------------------------------------------------------------
    def onLogin(self, event):
        """
        Check credentials and login
        """
        stupid_password = "crazy"
        user_password = self.password.GetValue()
        if user_password == stupid_password:
            print("You are now logged in!")
            self.logged_in = True
            self.Close()
        else:
            wx.MessageBox('Username or password is incorrect!',
                          'Enter Again', wx.OK | wx.ICON_INFORMATION)
            print("Username or password is incorrect!")


class SuperMarket(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(SuperMarket, self).__init__(*args, **kwargs)

        self.Mbar()

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

        # table Menu
        tableMenu = wx.Menu()
        tableItem=tableMenu.Append(wx.ID_ANY,'&show')

        self.Bind(wx.EVT_MENU, self.Onclicked, id=tableItem.GetId())

        menubar.Append(fileMenu, '&File')
        menubar.Append(editMenu, '&Edit')
        menubar.Append(viewMenu, '&View')
        menubar.Append(tableMenu, '&Tables')

        self.SetMenuBar(menubar)

        self.SetSize((500, 500))
        self.SetTitle('Super Market')
        self.Center()
        self.Maximize()

        width, height = wx.GetDisplaySize()
        self.two = wx.Panel(self,size=(width, height))
        self.two.SetBackgroundColour('black')
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        font = wx.Font(30, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        heading = wx.StaticText(self, -1, "Welcome to our supermarket", (100, 50), (width,height), wx.ALIGN_CENTER)
        heading.SetFont(font)
        # btn1 = wx.Button(self.two, label='Insert', size=(70, 30))
        hbox4.Add(heading)
        # btn2 = wx.Button(self.two, label='Update', size=(70, 30))
        # hbox4.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=5,)
        vbox.Add(hbox4)
        self.two.SetSizer(vbox)


        width, height = wx.GetDisplaySize()
        self.table = wx.Panel(self,size=(width, height))
        self.table.Hide()
        notebook = wx.Notebook(self.table)
        tabOne = TabPanel(notebook)
        notebook.AddPage(tabOne, "Table 1")

        tabTwo = TabPanel2(notebook)
        notebook.AddPage(tabTwo, "Table 2")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.ALL | wx.EXPAND, 5)
        self.table.SetSizer(sizer)

        dlg = LoginDialog()
        dlg.ShowModal()
        authenticated = dlg.logged_in
        if not authenticated:
            self.Close()

        self.two.Show()

        self.Layout()

    def Onclicked(self,e):
        self.two.Hide()
        if self.table.IsShown():
            self.two.Show()
            self.table.Hide()
        else:
            self.table.Show()
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


class TabPanel(wx.Panel):
    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """"""
        wx.Panel.__init__(self, parent=parent)

        colors = ["red", "blue", "gray", "yellow", "green"]
        self.SetBackgroundColour(random.choice(colors))

        btn = wx.Button(self, label="insert")
        btn2 = wx.Button(self, label="delete")
        btn3 = wx.Button(self, label="update")
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(btn, 0, wx.ALIGN_LEFT | wx.ALL, 10)
        sizer.Add(btn2, 0, wx.ALIGN_LEFT | wx.ALL, 10)
        sizer.Add(btn3, 0, wx.ALIGN_LEFT | wx.ALL, 10)
        self.SetSizer(sizer)


class TabPanel2(wx.Panel):
    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """"""
        wx.Panel.__init__(self, parent=parent)

        colors = ["red", "blue", "gray", "yellow", "green"]
        self.SetBackgroundColour(random.choice(colors))

        btn = wx.Button(self, label="insert")
        btn2 = wx.Button(self, label="delete")
        btn3 = wx.Button(self, label="update")
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(btn, 0, wx.ALIGN_LEFT | wx.ALL, 10)
        sizer.Add(btn2, 0, wx.ALIGN_LEFT | wx.ALL, 10)
        sizer.Add(btn3, 0, wx.ALIGN_LEFT | wx.ALL, 10)
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
    app = wx.App()
    p = SuperMarket(None)
    p.Show()
    # frame = DemoFrame()
    app.MainLoop()


if __name__ == '__main__':
    main()
