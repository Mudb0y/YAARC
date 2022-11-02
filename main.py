import os
from lib import speech
import pyglet
import praw

window = pyglet.window.Window()

if not os.path.isfile ("auth.token"):
    from lib import oauth

pyglet.app.run()