from front.front import MyWindow
from tkinter import *

# Opening Window
window = Tk()
mywin = MyWindow(window)
window.title('EEG Processing Machine')
window.geometry("500x350")
window.mainloop()
