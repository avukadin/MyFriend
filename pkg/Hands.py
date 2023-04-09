from pynput.keyboard import Controller, Key
import tkinter as tk
import platform

class Hands():
    keyboard: Controller

    def __init__(self):
        self.keyboard = Controller()

    def copy_highlighted(self):

        modifier = Key.cmd if platform.system()=='Darwin'\
                   else Key.ctrl # mac/else

        with self.keyboard.pressed(modifier):
            self.keyboard.press('c')  
            self.keyboard.release('c')

        return tk.Tk().clipboard_get()

    def paste(self, text):

        modifier = Key.cmd if platform.system()=='Darwin'\
                else Key.ctrl # mac/else

        with self.keyboard.pressed(modifier):
            self.keyboard.press('v')  
            self.keyboard.release('v')

