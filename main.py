import os
import pyglet
import praw
from lib import speech
from lib import oauth

window = pyglet.window.Window()

if not os.path.isfile ("auth.token"):
    oauth.authorise ()
    
pyglet.app.run()