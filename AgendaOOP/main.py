# main.py

import tkinter as tk
from interface import AgendaApp

def main():
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

