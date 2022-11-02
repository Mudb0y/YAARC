import os
import pyglet
import praw
from lib import speech
from lib import oauth

window = pyglet.window.Window()

if not os.path.isfile ("token.auth"):
    print ("No saved token is found.\nWaiting for authorisation...")
    speech.speak ("It looks like you're running YAARC for the first time! For the full functionality of this app to work, you need to authorise the program with your Reddit account. Press enter to open the authorisation website in your default browser.")    
    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == pyglet.window.key.ENTER:
            oauth.authorise()
else:
    speech.speak ("Welcome to YAARC!")

pyglet.app.run()