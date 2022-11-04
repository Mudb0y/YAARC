import os
import wx
from lib import authlib
from lib import ui, authui

# Main WX event-loop.
class App(wx.App):
    def OnInit(self):

        self.frame = ui.main_window(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        if not os.path.isfile("tokan.auth"):
            auth_dialog = authui.no_token(self.frame)
            auth_dialog.ShowModal()
        else:
            authlib.authorise()
        return True

if __name__ == "__main__":
    app = App(0)
    app.MainLoop()