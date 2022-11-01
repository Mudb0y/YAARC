import pyglet
import speech

window = pyglet.window.Window()

@window.event
def on_key_press (symbol, modifiers):
    speech.speak ("A key was pressed")
    