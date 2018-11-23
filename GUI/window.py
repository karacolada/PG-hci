#!/bin/python

import wx
import time

class FiredrillFrame(wx.Frame):

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(FiredrillFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)

        st = wx.StaticText(pnl, label="PLACEHOLDER", pos=(25,25))
        font = st.GetFont()
        font.PointSize += 8
        font = font.Bold()
        st.SetFont(font)

        # create a menu bar
        self.makeMenuBar()
        self.makeButtons()

    def makeButtons(self):
        startDrillButton = wx.Button(self, wx.ID_ANY, "Start new firedrill", pos=(25,60))
        endDrillButton = wx.Button(self, wx.ID_ANY, "End firedrill", pos=(25,90))
        hintButton = wx.Button(self,wx.ID_ANY, "Hint",pos=(25,120))

        self.Bind(wx.EVT_BUTTON, self.OnStartDrill, startDrillButton)
        
    def OnStartDrill(self,event):
        dlg = wx.MessageDialog(self,"Something in your system broke. Find out what it is! Time is running...")
        dlg.ShowModal()
        # starts Stop Watch
        self.watch = wx.StopWatch()


    def OnEndDrill(self,event):
        watch.Pause()
        dlg = wx.MessageDialog(self,"Checking whether your fix was successful...",caption = "Checking...")
        dlg.ShowModal()
        # replace with call to checkSystemFixed-bash script
        time.sleep(10)
        dlg.wx.MessageDialog(self,"Your system is alright!")
        dlg.ShowModal()







    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """
    
        # The "\t..." syntax defines an accelerator key that also triggers the same event:
        # helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H","Help string shown in status bar for this menu item")

        statsMenu = wx.Menu()
        timesItem = statsMenu.Append(wx.ID_ANY, "&Display Statistics...")

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)
        helpMenu.AppendSeparator()
        exitItem = helpMenu.Append(wx.ID_EXIT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(statsMenu, "&Statistics")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.OnTimes, timesItem)

    def OnTimes(self,event):
        # Supposed to display new frame/module/etc showing statistics of different kinds?
        wx.MessageBox("Will be implemented soon. Will show the statistics of your past firedrills.")

    def OnExit(self, event):
        # Close the frame, terminating the application.
        self.Close(True)

    def OnAbout(self, event):
        # Display an About Dialog
        wx.MessageBox("This is the prototype for a firedrill application supposed to be used in the work environment of system administrators.")


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = FiredrillFrame(None, title='Firedrill')
    frm.Show()
    app.MainLoop()