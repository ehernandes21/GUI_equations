import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from ttkthemes import ThemedTk

from Transferencia_calor import *

class GUI(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.master.title('Main')
        # create the button and set the command
        self.radiacion = ttk.Button(self, text="Radiacion", command=self.window_radia)
        self.reynolds = ttk.Button(self, text="Reynolds")
        self.nusselt = ttk.Button(self, text="Nusselt", command=self.window_nusselt)
        self.quit = ttk.Button(self, text="Quit", command=self.master.destroy)
        # Grid the buttons
        self.Grid_set()

    def Grid_set(self):
        self.radiacion.grid(row=0, column=0)
        self.reynolds.grid(row=1, column=0)
        self.nusselt.grid(row=2, column=0)
        self.quit.grid(row=3, column=0)

    def window_radia(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry('500x500')
        self.newWindow.title('Radiacion')
        self.app = window_radiacion(self.newWindow)

    # def window_reynolds(self):
    #     self.newWindow = tk.Toplevel(self.master)
    #     self.newWindow.geometry('500x500')
    #     self.app = window_radiacion(self.newWindow)

    def window_nusselt(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry('500x500')
        self.newWindow.title('Nusselt')
        self.app = window_Nusselt(self.newWindow)

#---------------------------------------------Radiacion------------------------------------------
class window_radiacion(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # Images 
        self.images()
        # Widgets
        self.labels_pictures()
        self.Entries()
        self.Buttons()


    def labels_pictures(self):
        # create the button and set the command
        # Title
        ttk.Label(self, text='Radiacion').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.radia1).grid(row=1, column=0, columnspan=2)
        # Variables
        ttk.Label(self, text='q').grid(row=3, column=0)
        ttk.Label(self, text='E').grid(row=4, column=0)
        ttk.Label(self, text='A').grid(row=5, column=0)
        ttk.Label(self, text='T1').grid(row=6, column=0)
        ttk.Label(self, text='T2').grid(row=7, column=0)
        # button to q
        ttk.Button(self, text="Quit", command=self.master.destroy).grid(row=11,column=0)


    def Entries(self):
        # labels for entries
        self.q = ttk.Entry(self)
        self.q.grid(row=3, column=1, columnspan=2)

        self.E = ttk.Entry(self)
        self.E.grid(row=4, column=1, columnspan=2)

        self.A = ttk.Entry(self)
        self.A.grid(row=5, column=1, columnspan=2)

        self.T1 = ttk.Entry(self)
        self.T1.grid(row=6, column=1, columnspan=2)

        self.T2 = ttk.Entry(self)
        self.T2.grid(row=7, column=1, columnspan=2)
    


    def get_entries(self):
        self.dict_entries = {'q': self.q.get(), 'E': self.E.get(), 'A': self.A.get(), 'T1': self.T1.get(), 'T2': self.T2.get()}
        for item, value in self.dict_entries.items():
            if value == 'None':
                self.dict_entries[item] = None
            elif type(value) is str:
                self.dict_entries[item] = float(value)
        self.equation(**self.dict_entries)


    def Buttons(self):
        save = ttk.Button(self, text='Save', command=self.get_entries)
        show = ttk.Button(self, text='Show', command=self.show)
        save.grid(row=10, column=4)
        show.grid(row=10, column=5)


    def images(self):
        # image 1
        self.radia1 = Image.open("images\\radia1.PNG")
        self.radia1 = self.radia1.resize((200, 200))
        self.radia1 = ImageTk.PhotoImage(self.radia1)

    def equation(self, q, E, A, T1, T2):
        self.Radia_1 = Radiacion(q=q, A=A, T1=T1, T2=T2, E=E)

    def show(self):
        ttk.Label(self, text=f'{self.Radia_1.solucion()}').grid(row=9, column=4)

#---------------------------------------------Reynolds------------------------------------------
# class window_Reynolds(ttk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.pack()
#         # Images 
#         self.images()
#         # Widgets
#         self.labels_pictures()
#         self.Entries()
#         self.Buttons()


#     def labels_pictures(self):
#         # create the button and set the command
#         # Title
#         ttk.Label(self, text='Reynolds').grid(row=0, column=1, columnspan=2)
#         # Images
#         ttk.Label(self, image=self.reynolds_1).grid(row=1, column=0, columnspan=2)
#         # Variables
#         ttk.Label(self, text='Re').grid(row=3, column=0)
#         ttk.Label(self, text='h').grid(row=4, column=0)
#         ttk.Label(self, text='d').grid(row=5, column=0)
#         ttk.Label(self, text='k').grid(row=6, column=0)
#         ttk.Label(self, text='Pr').grid(row=7, column=0)
#         ttk.Label(self, text='n').grid(row=8, column=0)
#         # button to q
#         ttk.Button(self, text="Quit", command=self.master.destroy).grid(row=11,column=0)


#     def Entries(self):
#         # labels for entries
#         self.Re = ttk.Entry(self)
#         self.Re.grid(row=3, column=1, columnspan=2)

#         self.h = ttk.Entry(self)
#         self.h.grid(row=4, column=1, columnspan=2)

#         self.d = ttk.Entry(self)
#         self.d.grid(row=5, column=1, columnspan=2)

#         self.k = ttk.Entry(self)
#         self.k.grid(row=6, column=1, columnspan=2)

#         self.Pr = ttk.Entry(self)
#         self.Pr.grid(row=7, column=1, columnspan=2)

#         self.n = ttk.Entry(self)
#         self.n.grid(row=8, column=1, columnspan=2)
    


#     def get_entries(self):
#         self.dict_entries = {'Re': self.Re.get(), 'h': self.h.get(), 'd': self.d.get(), 'k': self.k.get(), 'Pr': self.Pr.get(), 'n': self.n.get()}
#         for item, value in self.dict_entries.items():
#             if value == 'None':
#                 self.dict_entries[item] = None
#             elif type(value) is str:
#                 self.dict_entries[item] = float(value)
#         self.equation(**self.dict_entries)


#     def Buttons(self):
#         save = ttk.Button(self, text='Save', command=self.get_entries)
#         show = ttk.Button(self, text='Show', command=self.show)
#         save.grid(row=11, column=4)
#         show.grid(row=11, column=5)


#     def images(self):
#         # image 1
#         self.reynolds_1 = Image.open("images\\reynolds_1.PNG")
#         self.reynolds_1 = self.reynolds_1.resize((200, 200))
#         self.reynolds_1 = ImageTk.PhotoImage(self.reynolds_1)

#     def equation(self, q, E, A, T1, T2):
#         self.Reyn_1 = Reynolds(q=q, A=A, T1=T1, T2=T2, E=E)

#     def show(self):
#         ttk.Label(self, text=f'{self.Reyn_1.solucion()}').grid(row=9, column=4)
#---------------------------------------------Nusselt------------------------------------------
class window_Nusselt(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        # Images 
        self.images()
        # Widgets
        self.labels_pictures()
        self.Entries()
        self.Buttons()


    def labels_pictures(self):
        # create the button and set the command
        # Title
        ttk.Label(self, text='Nusselt').grid(row=0, column=1, columnspan=2)
        # Images
        ttk.Label(self, image=self.nuss_1).grid(row=1, column=0, columnspan=2)
        # Variables
        ttk.Label(self, text='Re').grid(row=3, column=0)
        ttk.Label(self, text='h').grid(row=4, column=0)
        ttk.Label(self, text='d').grid(row=5, column=0)
        ttk.Label(self, text='k').grid(row=6, column=0)
        ttk.Label(self, text='Pr').grid(row=7, column=0)
        ttk.Label(self, text='n').grid(row=8, column=0)
        # button to q
        ttk.Button(self, text="Quit", command=self.master.destroy).grid(row=11,column=0)


    def Entries(self):
        # labels for entries
        self.Re = ttk.Entry(self)
        self.Re.grid(row=3, column=1, columnspan=2)

        self.h = ttk.Entry(self)
        self.h.grid(row=4, column=1, columnspan=2)

        self.d = ttk.Entry(self)
        self.d.grid(row=5, column=1, columnspan=2)

        self.k = ttk.Entry(self)
        self.k.grid(row=6, column=1, columnspan=2)

        self.Pr = ttk.Entry(self)
        self.Pr.grid(row=7, column=1, columnspan=2)

        self.n = ttk.Entry(self)
        self.n.grid(row=8, column=1, columnspan=2)
    


    def get_entries(self):
        self.dict_entries = {'Re': self.Re.get(), 'h': self.h.get(), 'd': self.d.get(), 'k': self.k.get(), 'Pr': self.Pr.get(), 'n': self.n.get()}
        for item, value in self.dict_entries.items():
            if value == 'None':
                self.dict_entries[item] = None
            elif type(value) is str:
                self.dict_entries[item] = float(value)
        self.equation(**self.dict_entries)


    def Buttons(self):
        save = ttk.Button(self, text='Save', command=self.get_entries)
        show = ttk.Button(self, text='Show', command=self.show)
        save.grid(row=11, column=4)
        show.grid(row=11, column=5)


    def images(self):
        # image 1
        self.nuss_1 = Image.open("images\\nuss_1.PNG")
        self.nuss_1 = self.nuss_1.resize((200, 200))
        self.nuss_1 = ImageTk.PhotoImage(self.nuss_1)

    def equation(self, Re, h, d, k, Pr, n):
        self.Nusselt_1 = Nusselt(Re=Re,h=h, d=d, k=k, Pr=Pr, n=n)

    def show(self):
        ttk.Label(self, text=f'{self.Nusselt_1.solucion_total()}').grid(row=9, column=4)


master = ThemedTk(themebg=True)
#ubuntu
master.set_theme('breeze')
master.geometry('200x150')
app = GUI(master=master)
app.mainloop()



