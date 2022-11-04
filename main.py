import wx
from lib import authlib
from lib import ui

# Main WX event-loop.
class App(wx.App):
    def OnInit(self):
        self.frame = ui.main_window(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = App(0)
    app.MainLoop()