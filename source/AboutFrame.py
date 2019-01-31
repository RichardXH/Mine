import wx

class AboutPanel(wx.Panel):
    def __init__(self, parent, style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX) | wx.STAY_ON_TOP):
        '''create the demopanel.'''
        wx.Panel.__init__(self, parent, style=style)

        msg = wx.StaticText(self, 1, "Mine write by Richard", wx.Point(15, 30))
        msg1 = wx.StaticText(self, 2, " Enjoy! ", wx.Point(15, 30))
        msg2 = wx.StaticText(self, 3, "Vision 1.1", wx.Point(15, 30))
        msg3 = wx.StaticText(self, 4, "Date:2019.01.31", wx.Point(15, 30))

        closeBtn = wx.Button(self, label='Close')
        closeBtn.Bind(wx.EVT_BUTTON, parent.close)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(msg)
        Sizer.Add(msg1)
        Sizer.Add(msg2)
        Sizer.Add(msg3)
        Sizer.Add(closeBtn)

        self.SetSizerAndFit(Sizer)


class AboutFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        wx.Frame.__init__(self, parent, *args, **kwargs)

        # Add the Widget Panel
        self.Panel = AboutPanel(self)
        self.Fit()
        self.Center()

    def close(self, event=None):
        'Exit application.'
        self.Hide()


# Only for test
if __name__ == '__main__':
    app = wx.App()
    frame = AboutFrame(None, title="About Mine")
    frame.SetSize((300, 200))
    frame.Show()
    app.MainLoop()