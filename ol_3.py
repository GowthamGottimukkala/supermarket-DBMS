import wx
import random
import MySQLdb
import sys

# Open database connection
db = MySQLdb.connect("localhost","shravan","shravan","supermarket" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

class SuperMarket(wx.Frame):
    def __init__(self,*args, **kwargs):
        super(SuperMarket,self).__init__(*args, **kwargs)
        self.Maximize()

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
        notebook.AddPage(tabOne, "products")

        tabTwo = TabPanel2(notebook)
        notebook.AddPage(tabTwo, "customers")

        tabThree = TabPanel3(notebook)
        notebook.AddPage(tabThree, "payments")

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
        #self.SetBackgroundColour("yellow")
        font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(13)
        gbs=wx.GridBagSizer(5,5)

        attributes = ['p_ID', 'p_Name', 'MRP','stock','d_ID']
        st=wx.StaticText(self,label="search by")
        self.combo = wx.ComboBox(self,choices = attributes,style=wx.CB_READONLY)
        self.searchControl = wx.SearchCtrl(self, -1, style=wx.TE_PROCESS_ENTER)
        btn1=wx.Button(self,label="search")
        st.SetFont(font)
        gbs.Add(st, pos = (1, 2), flag = wx.ALL, border = 5)
        gbs.Add(self.combo,pos=(1,3),span=(1,3),flag=wx.EXPAND|wx.ALL,border=5)
        gbs.Add(self.searchControl, pos = (1, 6), span=(1,5),flag = wx.EXPAND|wx.ALL, border = 2)
        gbs.Add(btn1, pos = (1, 11), flag = wx.ALL, border = 5)
        self.Bind(wx.EVT_BUTTON, self.search, id = btn1.GetId())

        # execute SQL query using execute() method.
        sql="select * from products"
        cursor = self.query(sql)
        records = cursor.fetchall()
        width,height=wx.GetDisplaySize()
        self.list = wx.ListCtrl(self, -1, size=(-1,400),style = wx.LC_REPORT)
        self.list.InsertColumn(0, 'p_ID',wx.LIST_FORMAT_CENTER, width/5-27)
        self.list.InsertColumn(1, 'p_Name', wx.LIST_FORMAT_CENTER, width/5-27)
        self.list.InsertColumn(2, 'MRP', wx.LIST_FORMAT_CENTER, width/5-27)
        self.list.InsertColumn(3, 'stock', wx.LIST_FORMAT_CENTER, width/5-27)
        self.list.InsertColumn(4, 'd_ID', wx.LIST_FORMAT_CENTER, width/5-27)
        for i in records:
           k1=str(i[0])
           k2=str(i[1])
           k3=str(i[2])
           k4=str(i[3])
           k5=str(i[4])
           index = self.list.InsertStringItem(sys.maxint,k1)
           self.list.SetStringItem(index, 1, k2)
           self.list.SetStringItem(index, 2, k3)
           self.list.SetStringItem(index, 3, k4)
           self.list.SetStringItem(index, 4, k5)
        gbs.Add(self.list, pos = (3,0),span=(7,14),flag = wx.ALL, border = 5)

        btn2=wx.Button(self,label="back",size=(80,40))
        gbs.Add(btn2, pos = (11, 0), flag = wx.ALIGN_LEFT|wx.ALL, border = 5)

        btn3=wx.Button(self,label="update",size=(80,40))
        gbs.Add(btn3, pos = (11, 13), flag = wx.ALIGN_CENTER|wx.ALL, border = 5)
        self.Bind(wx.EVT_BUTTON, self.update, id = btn3.GetId())

        self.SetSizerAndFit(gbs)

    def search(self,e):
        searchby=self.combo.GetValue()
        value=self.searchControl.GetValue()
        sql="select * from products where %s='%s'" %(searchby,value)
        cursor = self.query(sql)
        x=cursor.fetchone()
        print x

    def update(self,e):
        Update(self,"update")

    def connect(self):
        self.conn = MySQLdb.connect("localhost","shravan","shravan","supermarket")

    def query(self, sql):
        try:
          cursor = self.conn.cursor()
          cursor.execute(sql)
          self.conn.commit()
        except (AttributeError, MySQLdb.OperationalError):
          self.connect()
          cursor = self.conn.cursor()
          cursor.execute(sql)
          self.conn.commit()
        return cursor

class Update(wx.Frame):
    def __init__(self, parent,title):
        super(Update,self).__init__(parent,title=title)

        self.Maximize()

        font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(17)
        self.gbs=wx.GridBagSizer(5,5)

        self.st1= wx.StaticText(self,label = "PRODUCTS" ,style = wx.ALIGN_CENTRE)
        self.st1.SetFont(font)
        self.st2= wx.StaticText(self,label = "p_ID:" )
        self.st2.SetFont(font)
        self.tc2=wx.TextCtrl(self,-1,"")
        self.btn1=wx.Button(self,label="OK")
        self.Bind(wx.EVT_BUTTON, self.okay, self.btn1)

        self.gbs.Add(self.st1, pos = (5,30),flag =wx.ALIGN_CENTER| wx.ALL, border = 5)
        self.gbs.Add(self.st2,pos=(7,25),flag=wx.ALIGN_RIGHT|wx.ALL,border=5)
        self.gbs.Add(self.tc2, pos = (7, 29), span=(1,3),flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 5)
        self.gbs.Add(self.btn1, pos = (7, 35), flag = wx.ALIGN_RIGHT|wx.ALL, border = 5)

        self.SetSizerAndFit(self.gbs)
        self.Centre()
        self.Show()


    def okay(self,e):
        if self.tc2.GetValue() == "" :
            wx.MessageBox("p_ID field is Empty!")
        else:
            font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
            font.SetPointSize(17)
            sql="select * from products where pid=%s" %(self.tc2.GetValue())
            cursor = self.query(sql)
            x=cursor.fetchone()
            st3=wx.StaticText(self,label="p_Name:")
            st3.SetFont(font)
            self.tc3=wx.TextCtrl(self,-1,str(x[1]))
            st4=wx.StaticText(self,label="MRP:")
            st4.SetFont(font)
            self.tc4=wx.TextCtrl(self,-1,str(x[2]))
            st5=wx.StaticText(self,label="stock:")
            st5.SetFont(font)
            self.tc5=wx.TextCtrl(self,-1,str(x[3]))
            st6=wx.StaticText(self,label="d_ID:")
            st6.SetFont(font)
            self.tc6=wx.TextCtrl(self,-1,str(x[4]))
            update=wx.Button(self,label="update")
            self.gbs.Add(st3, pos = (9,25),flag =wx.ALIGN_RIGHT|wx.ALL, border = 1)
            self.gbs.Add(self.tc3, pos = (9, 29),span=(1,3), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
            self.gbs.Add(st4, pos = (10, 25),flag = wx.ALIGN_LEFT|wx.ALL, border = 1)
            self.gbs.Add(self.tc4, pos = (10,29), span=(1,3), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
            self.gbs.Add(st5, pos = (11,25),flag =wx.ALIGN_RIGHT|wx.ALL, border = 1)
            self.gbs.Add(self.tc5, pos = (11, 29),span=(1,3), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
            self.gbs.Add(st6, pos = (12,25),flag =wx.ALIGN_RIGHT|wx.ALL, border = 1)
            self.gbs.Add(self.tc6, pos = (12, 29),span=(1,3), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
            self.gbs.Add(update, pos = (14,35), flag =wx.ALIGN_RIGHT| wx.ALL, border = 1)

            self.SetSizerAndFit(self.gbs)
            self.Bind(wx.EVT_BUTTON, self.update, update)

    def update(self,e):
        sql="update products set pname='%s',MRP=%s, stock=%s, Did=%s where pid=%s" %(self.tc3.GetValue(),self.tc4.GetValue(),self.tc5.GetValue(),self.tc6.GetValue(),self.tc2.GetValue())
        cur = self.query(sql)
        SuperMarket(None)

    def connect(self):
        self.conn = MySQLdb.connect("localhost","shravan","shravan","supermarket")

    def query(self, sql):
        try:
          cursor = self.conn.cursor()
          cursor.execute(sql)
          self.conn.commit()
        except (AttributeError, MySQLdb.OperationalError):
          self.connect()
          cursor = self.conn.cursor()
          cursor.execute(sql)
          self.conn.commit()
        return cursor

class TabPanel2(wx.Panel):
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """"""
        wx.Panel.__init__(self, parent=parent)

        colors = ["red", "blue", "gray", "yellow", "green"]
        #self.SetBackgroundColour("yellow")
        font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(13)
        gbs=wx.GridBagSizer(5,5)

        attributes = ['c_ID', 'c_Name', 'phNo']
        st=wx.StaticText(self,label="search by")
        self.combo = wx.ComboBox(self,choices = attributes,style=wx.CB_READONLY)
        self.searchControl = wx.SearchCtrl(self, -1, style=wx.TE_PROCESS_ENTER)
        btn1=wx.Button(self,label="search")
        st.SetFont(font)
        gbs.Add(st, pos = (1, 2), flag = wx.ALL, border = 5)
        gbs.Add(self.combo,pos=(1,3),span=(1,3),flag=wx.EXPAND|wx.ALL,border=5)
        gbs.Add(self.searchControl, pos = (1, 6), span=(1,5),flag = wx.EXPAND|wx.ALL, border = 2)
        gbs.Add(btn1, pos = (1, 11), flag = wx.ALL, border = 5)
        self.Bind(wx.EVT_BUTTON, self.search, id = btn1.GetId())

        # execute SQL query using execute() method.
        sql="select * from customers"
        cursor = self.query(sql)
        records = cursor.fetchall()
        width,height=wx.GetDisplaySize()
        self.list = wx.ListCtrl(self, -1, size=(-1,400),style = wx.LC_REPORT)
        self.list.InsertColumn(0, 'c_ID',wx.LIST_FORMAT_CENTER, width/3-27)
        self.list.InsertColumn(1, 'c_Name', wx.LIST_FORMAT_CENTER, width/3-27)
        self.list.InsertColumn(2, 'phNo', wx.LIST_FORMAT_CENTER, width/3-27)
        for i in records:
           k1=str(i[0])
           k2=str(i[1])
           k3=str(i[2])
           index = self.list.InsertStringItem(sys.maxint,k1)
           self.list.SetStringItem(index, 1, k2)
           self.list.SetStringItem(index, 2, k3)
           
           
          
        gbs.Add(self.list, pos = (3,0),span=(7,14),flag = wx.ALL, border = 5)

        btn2=wx.Button(self,label="back",size=(80,40))
        gbs.Add(btn2, pos = (11, 0), flag = wx.ALIGN_LEFT|wx.ALL, border = 5)

        btn3=wx.Button(self,label="update",size=(80,40))
        gbs.Add(btn3, pos = (11, 13), flag = wx.ALIGN_CENTER|wx.ALL, border = 5) 
        self.Bind(wx.EVT_BUTTON, self.update, id = btn3.GetId())

        self.SetSizerAndFit(gbs)

    def search(self,e):
        searchby=self.combo.GetValue()
        value=self.searchControl.GetValue()
        sql="select * from customers where %s='%s'" %(searchby,value)
        cursor = self.query(sql)
        x=cursor.fetchone()
        print x

    def update(self,e):
        Update2(self,"update")

    def connect(self):
        self.conn = MySQLdb.connect("localhost","shravan","shravan","supermarket")

    def query(self, sql):
        try:
          cursor = self.conn.cursor()
          cursor.execute(sql)
          self.conn.commit()
        except (AttributeError, MySQLdb.OperationalError):
          self.connect()
          cursor = self.conn.cursor()
          cursor.execute(sql)
          self.conn.commit()
        return cursor

class Update2(wx.Frame):
    def __init__(self, parent,title):
        super(Update2,self).__init__(parent,title=title)

        self.Maximize()

        font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(17)
        self.gbs=wx.GridBagSizer(5,5)

        self.st1= wx.StaticText(self,label = "CUSTOMERS" ,style = wx.ALIGN_CENTRE)
        self.st1.SetFont(font)
        self.st2= wx.StaticText(self,label = "c_ID:" )
        self.st2.SetFont(font)
        self.tc2=wx.TextCtrl(self,-1,"")
        self.btn1=wx.Button(self,label="OK")
        self.Bind(wx.EVT_BUTTON, self.okay, self.btn1)

        self.gbs.Add(self.st1, pos = (5,30),flag =wx.ALIGN_CENTER| wx.ALL, border = 5)
        self.gbs.Add(self.st2,pos=(7,25),flag=wx.ALIGN_RIGHT|wx.ALL,border=5)
        self.gbs.Add(self.tc2, pos = (7, 29), span=(1,3),flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 5)
        self.gbs.Add(self.btn1, pos = (7, 35), flag = wx.ALIGN_RIGHT|wx.ALL, border = 5)

        self.SetSizerAndFit(self.gbs)
        self.Centre()
        self.Show()


    def okay(self,e):
        if self.tc2.GetValue() == "" :
            wx.MessageBox("c_ID field is Empty!")
        else:
            font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
            font.SetPointSize(17)
            sql="select * from customers where c_ID=%s" %(self.tc2.GetValue())
            cursor = self.query(sql)
            x=cursor.fetchone()
            st3=wx.StaticText(self,label="c_Name:")
            st3.SetFont(font)
            self.tc3=wx.TextCtrl(self,-1,str(x[1]))
            st4=wx.StaticText(self,label="phNo:")
            st4.SetFont(font)
            self.tc4=wx.TextCtrl(self,-1,str(x[2]))
            
            update=wx.Button(self,label="update")
            self.gbs.Add(st3, pos = (9,25),flag =wx.ALIGN_RIGHT|wx.ALL, border = 1)
            self.gbs.Add(self.tc3, pos = (9, 29),span=(1,3), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
            self.gbs.Add(st4, pos = (10, 25),flag = wx.ALIGN_LEFT|wx.ALL, border = 1)
            self.gbs.Add(self.tc4, pos = (10,29), span=(1,3), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
            
            self.gbs.Add(update, pos = (12,35), flag =wx.ALIGN_RIGHT| wx.ALL, border = 1)

            self.SetSizerAndFit(self.gbs)
            self.Bind(wx.EVT_BUTTON, self.update, update)

    def update(self,e):
        sql="update customers set cname='%s',mnumber=%s where cid=%s" %(self.tc3.GetValue(),self.tc4.GetValue(),self.tc2.GetValue())
        cur = self.query(sql)
        SuperMarket(None)

    def connect(self):
        self.conn = MySQLdb.connect("localhost","shravan","shravan","supermarket")

    def query(self, sql):
        try:
          cursor = self.conn.cursor()
          cursor.execute(sql)
          self.conn.commit()
        except (AttributeError, MySQLdb.OperationalError):
          self.connect()
          cursor = self.conn.cursor()
          cursor.execute(sql)
          self.conn.commit()
        return cursor

class TabPanel3(wx.Panel):
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """"""
        wx.Panel.__init__(self, parent=parent)

        colors = ["red", "blue", "gray", "yellow", "green"]
        #self.SetBackgroundColour("yellow")
        font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(13)
        gbs=wx.GridBagSizer(5,5)

        attributes = ['b_ID', 'm_number', 'c_ID','p_date','amount']
        st=wx.StaticText(self,label="search by")
        self.combo = wx.ComboBox(self,choices = attributes,style=wx.CB_READONLY)
        self.searchControl = wx.SearchCtrl(self, -1, style=wx.TE_PROCESS_ENTER)
        btn1=wx.Button(self,label="search")
        st.SetFont(font)
        gbs.Add(st, pos = (1, 2), flag = wx.ALL, border = 5)
        gbs.Add(self.combo,pos=(1,3),span=(1,3),flag=wx.EXPAND|wx.ALL,border=5)
        gbs.Add(self.searchControl, pos = (1, 6), span=(1,5),flag = wx.EXPAND|wx.ALL, border = 2)
        gbs.Add(btn1, pos = (1, 11), flag = wx.ALL, border = 5)
        self.Bind(wx.EVT_BUTTON, self.search, id = btn1.GetId())

        # execute SQL query using execute() method.
        sql="select * from payment"
        cursor = self.query(sql)
        records = cursor.fetchall()
        width,height=wx.GetDisplaySize()
        self.list = wx.ListCtrl(self, -1, size=(-1,400),style = wx.LC_REPORT)
        self.list.InsertColumn(0, 'b_ID',wx.LIST_FORMAT_CENTER, width/5-27)
        self.list.InsertColumn(1, 'm_number', wx.LIST_FORMAT_CENTER, width/5-27)
        self.list.InsertColumn(2, 'c_ID', wx.LIST_FORMAT_CENTER, width/5-27)
        self.list.InsertColumn(3, 'p_date', wx.LIST_FORMAT_CENTER, width/5-27)
        self.list.InsertColumn(4, 'amount', wx.LIST_FORMAT_CENTER, width/5-27)
        for i in records:
           k1=str(i[0])
           k2=str(i[1])
           k3=str(i[2])
           k4=str(i[3])
           k5=str(i[4])
           index = self.list.InsertStringItem(sys.maxint,k1)
           self.list.SetStringItem(index, 1, k2)
           self.list.SetStringItem(index, 2, k3)
           self.list.SetStringItem(index, 3, k4)
           self.list.SetStringItem(index, 4, k5)
        gbs.Add(self.list, pos = (3,0),span=(7,14),flag = wx.ALL, border = 5)

        btn2=wx.Button(self,label="back",size=(80,40))
        gbs.Add(btn2, pos = (11, 0), flag = wx.ALIGN_LEFT|wx.ALL, border = 5)

        btn3=wx.Button(self,label="update",size=(80,40))
        gbs.Add(btn3, pos = (11, 13), flag = wx.ALIGN_CENTER|wx.ALL, border = 5)
        self.Bind(wx.EVT_BUTTON, self.update, id = btn3.GetId())

        self.SetSizerAndFit(gbs)

    def search(self,e):
        searchby=self.combo.GetValue()
        value=self.searchControl.GetValue()
        sql="select * from payment where %s='%s'" %(searchby,value)
        cursor = self.query(sql)
        x=cursor.fetchone()
        print x

    def update(self,e):
        Update3(self,"update")

    def connect(self):
        self.conn = MySQLdb.connect("localhost","shravan","shravan","supermarket")

    def query(self, sql):
        try:
          cursor = self.conn.cursor()
          cursor.execute(sql)
          self.conn.commit()
        except (AttributeError, MySQLdb.OperationalError):
          self.connect()
          cursor = self.conn.cursor()
          cursor.execute(sql)
          self.conn.commit()
        return cursor

class Update3(wx.Frame):
    def __init__(self, parent,title):
        super(Update3,self).__init__(parent,title=title)

        self.Maximize()

        font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(17)
        self.gbs=wx.GridBagSizer(5,5)

        self.st1= wx.StaticText(self,label = "PAYMENTS" ,style = wx.ALIGN_CENTRE)
        self.st1.SetFont(font)
        self.st2= wx.StaticText(self,label = "b_ID:" )
        self.st2.SetFont(font)
        self.tc2=wx.TextCtrl(self,-1,"")
        self.btn1=wx.Button(self,label="OK")
        self.Bind(wx.EVT_BUTTON, self.okay, self.btn1)

        self.gbs.Add(self.st1, pos = (5,30),flag =wx.ALIGN_CENTER| wx.ALL, border = 5)
        self.gbs.Add(self.st2,pos=(7,25),flag=wx.ALIGN_RIGHT|wx.ALL,border=5)
        self.gbs.Add(self.tc2, pos = (7, 29), span=(1,3),flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 5)
        self.gbs.Add(self.btn1, pos = (7, 35), flag = wx.ALIGN_RIGHT|wx.ALL, border = 5)

        self.SetSizerAndFit(self.gbs)
        self.Centre()
        self.Show()


    def okay(self,e):
        if self.tc2.GetValue() == "" :
            wx.MessageBox("b_ID field is Empty!")
        else:
            font=wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
            font.SetPointSize(17)
            sql="select * from payment where bid=%s" %(self.tc2.GetValue())
            cursor = self.query(sql)
            x=cursor.fetchone()
            st3=wx.StaticText(self,label="m_number:")
            st3.SetFont(font)
            self.tc3=wx.TextCtrl(self,-1,str(x[1]))
            st4=wx.StaticText(self,label="c_ID:")
            st4.SetFont(font)
            self.tc4=wx.TextCtrl(self,-1,str(x[2]))
            st5=wx.StaticText(self,label="p_date:")
            st5.SetFont(font)
            self.tc5=wx.TextCtrl(self,-1,str(x[3]))
            st6=wx.StaticText(self,label="amount:")
            st6.SetFont(font)
            self.tc6=wx.TextCtrl(self,-1,str(x[4]))
            update=wx.Button(self,label="update")
            self.gbs.Add(st3, pos = (9,25),flag =wx.ALIGN_RIGHT|wx.ALL, border = 1)
            self.gbs.Add(self.tc3, pos = (9, 29),span=(1,3), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
            self.gbs.Add(st4, pos = (10, 25),flag = wx.ALIGN_LEFT|wx.ALL, border = 1)
            self.gbs.Add(self.tc4, pos = (10,29), span=(1,3), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
            self.gbs.Add(st5, pos = (11,25),flag =wx.ALIGN_RIGHT|wx.ALL, border = 1)
            self.gbs.Add(self.tc5, pos = (11, 29),span=(1,3), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
            self.gbs.Add(st6, pos = (12,25),flag =wx.ALIGN_RIGHT|wx.ALL, border = 1)
            self.gbs.Add(self.tc6, pos = (12, 29),span=(1,3), flag = wx.ALIGN_LEFT|wx.EXPAND|wx.ALL, border = 1)
            self.gbs.Add(update, pos = (14,35), flag =wx.ALIGN_RIGHT| wx.ALL, border = 1)

            self.SetSizerAndFit(self.gbs)
            self.Bind(wx.EVT_BUTTON, self.update, update)

    def update(self,e):
        sql="update payment set mnumber=%s,cid=%s,pdate=%s,amount=%s where bid=%s" %(self.tc3.GetValue(),self.tc4.GetValue(),self.tc5.GetValue(),self.tc2.GetValue())
        cur = self.query(sql)
        SuperMarket(None)

    def connect(self):
        self.conn = MySQLdb.connect("localhost","shravan","shravan","supermarket")

    def query(self, sql):
        try:
          cursor = self.conn.cursor()
          cursor.execute(sql)
          self.conn.commit()
        except (AttributeError, MySQLdb.OperationalError):
          self.connect()
          cursor = self.conn.cursor()
          cursor.execute(sql)
          self.conn.commit()
        return cursor


db.close()




def main():
	app=wx.App()
	p=SuperMarket(None)
	p.Show()
	#frame = DemoFrame()
	app.MainLoop()

if __name__ == '__main__':
	main()
