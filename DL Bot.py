from mainWindow import MainWindow
from tkinter import Tk
import os

script_dir=os.path.dirname(__file__)
img_path=os.path.join(script_dir,"assets","gema.ico")

def main():
    root=Tk()
    root.wm_title("DL Farmer")
    root.wm_geometry("320x180")
    root.wm_iconbitmap(img_path)
    root.wm_resizable(False,False)
    app= MainWindow(root)
    app.mainloop()
    
if __name__=="__main__":
    main()
