# main_estruturado.py

import tkinter as tk
from interface_estruturada import AgendaAppEstruturada

def main():
    root = tk.Tk()
    app = AgendaAppEstruturada(root)
    root.mainloop()

if __name__ == "__main__":
    main()

